import requests
from datetime import datetime, timedelta
from requests.auth import HTTPBasicAuth
from utils import _extract_suffix, _unix_to_date_string, handle_children_IDs, parse_json_data, _extract_comments

class Reddit:
    def __init__(self, credentials):
        self.base_url = "https://oauth.reddit.com/api/info"
        self.credentials = credentials
        self.access_token = None
        self.access_token_expiration = None
    
    def determineAccessToken(self):
        if self.access_token_expiration is None:
            error = self.generate_token()
            return self.access_token, error

        token_expiration = datetime.fromisoformat(self.access_token_expiration)
        if datetime.now() > token_expiration:
            error = self.generate_token()
            return self.access_token, error

        return self.access_token, None

    def generate_token(self):
        data = {
            'grant_type': self.credentials["grant_type"],
            'username': self.credentials["username"],
            'password': self.credentials["password"]
        }
 
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/json',
        }
        
        response = requests.post(self.credentials['token_url'], data=data, headers=headers, auth=HTTPBasicAuth(self.credentials['client_id'], self.credentials['client_secret']))

        self.access_token = response.json().get('access_token')
        self.access_token_expiration = (datetime.now() + timedelta(hours=1)).isoformat()

        if response.status_code == 200:
            return None
        else:
            return response.text

    def handle_get_children_by_id(self, childrenIDs):
        token, error = self.determineAccessToken()
        if error is not None:
            return [], error

        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Accept': 'application/json',
            'Authorization': f'Bearer {token}',
        }
        url = f"{self.base_url}?id={','.join(childrenIDs)}"

        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            return [], response.text

        data = response.json()

        return parse_json_data(data), None

    def get_json_data(self, url):
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(f'{url}.json', headers=headers)
        if response.status_code == 200:
            return response.json()

        return {}

    def get_comments(self, json_data):
        data = json_data[1]["data"]["children"]
        comments = []
        cIDS = []

        for comment in data:
            data, childrenIDs = _extract_comments(comment['data'])
            comments.append(data)
            cIDS.extend(childrenIDs)

        chunk_size = 100
        for i in range(0, len(cIDS), chunk_size):
            chunk = cIDS[i:i + chunk_size]
            data, error = self.handle_get_children_by_id(chunk)
            
            if error is not None:
                return comments, error

            comments.extend(data)

        return comments, None
