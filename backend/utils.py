from datetime import datetime

def _extract_suffix(comment_id):
    return comment_id.split('_')[-1]

def _unix_to_date_string(unix_timestamp):
    date_time = datetime.utcfromtimestamp(unix_timestamp)
    return date_time.strftime('%Y-%m-%d %H:%M:%S')

def handle_children_IDs(comment_children):
    child_comment_ids = comment_children.get('children', [])
    return ['t1_' + id for id in child_comment_ids]

def parse_json_data(data):
    parsed_data = []
    children = data['data']['children']
    
    for child in children:
        comment_data = child['data']
        
        parsed_comment = {
            'author': comment_data['author'],
            'body': comment_data['body'],
            'created_utc': _unix_to_date_string(comment_data.get('created_utc', 0)),
            'id': comment_data['id'],
            'parent_id': comment_data['parent_id']
        }
        
        parsed_data.append(parsed_comment)
    
    return parsed_data

def _extract_comments(comment_data):
    childrenIDs = []
    comments = []
    
    if 'children' in comment_data:
        childrenIDs.extend(handle_children_IDs(comment_data))
        if not childrenIDs:
            return [], []

    comment = {
        'author': comment_data.get('author', 'undefined'),
        'body': comment_data.get('body', ''),
        'created_utc': _unix_to_date_string(comment_data.get('created_utc', 0)),
        'id': comment_data.get('id', 'No ID'),
        'parent_id': _extract_suffix(comment_data.get('parent_id', 'No Parent ID'))
    }

    comments.append(comment)

    if 'replies' in comment_data and comment_data['replies']:
        replies_data = comment_data['replies']['data']
        
        for child in replies_data['children']:
            child_comments, child_ids = _extract_comments(child['data'])
            comments.extend(child_comments)
            childrenIDs.extend(child_ids)
    
    return comments, childrenIDs

def filter_data(data):
    rowArray = []

    for i in data:
        if isinstance(i, list):
            # Filter elements in the list where the 'body' key is not ''
            filtered_elements = [element for element in i if element.get('body') != '' and element.get('author') != '[deleted]']
            rowArray.extend(filtered_elements)
        elif i.get('body') != ''and i.get('author') != '[deleted]':
            # Check if the item is a dict and the 'body' key is not ''
            rowArray.append(i)

    return rowArray

