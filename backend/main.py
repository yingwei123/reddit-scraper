from flask import Flask, request, redirect, abort, make_response, url_for, session, send_from_directory, jsonify
from dotenv import load_dotenv
from reddit import Reddit
from datetime import datetime, timedelta
import os
import secrets
from flask_cors import CORS
from datetime import timedelta, datetime
from utils import filter_data

app = Flask(__name__, static_folder='../frontend/build')
CORS(app, resources={r"/*": {"origins": "*", "supports_credentials": True}})

load_dotenv()

reddit = Reddit({
    'client_id' : os.getenv('CLIENT_ID'),
    'client_secret' : os.getenv('CLIENT_SECRET'),
    'redirect_uri' :  os.getenv('REDIRECT_URI'),
    'authorization_url' : os.getenv('AUTHORIZATION_URL'),
    'token_url' : os.getenv('TOKEN_URL'),
    'username': os.getenv('REDDIT_USERNAME'),
    'password':os.getenv('REDDIT_PASSWORD'),
    'grant_type':os.getenv('GRANT_TYPE')
})

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Route for serving static files like CSS and JS
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory(os.path.join(app.static_folder, 'static'), path)

@app.route('/reddit-data')
def serve_reddit_data():
    url =  request.args.get("reddit_url")

    json_data = reddit.get_json_data(url)
    
    data, error = reddit.get_comments(json_data)
    if(error is not None):
        abort(500, description=error)

    rowArray = filter_data(data)

    return rowArray

@app.errorhandler(500)
def internal_error(error):
    response = jsonify({
        "description": error.description
    })
    response.status_code = 500
    return response

if __name__ == '__main__':
    app.run(host='localhost', port=8001, debug=True)
