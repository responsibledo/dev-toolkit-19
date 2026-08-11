def clean_data(data):
    cleaned = []
    for item in data:
        if isinstance(item, str) and item.strip():
            cleaned.append(item.strip())
    return cleaned


def format_date(date_str):
    from datetime import datetime
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return None


def generate_unique_id(existing_ids):
    import uuid
    new_id = str(uuid.uuid4())
    while new_id in existing_ids:
        new_id = str(uuid.uuid4())
    return new_id


def filter_active_users(users):
    return [user for user in users if user.get('active', False)]


def sort_users_by_creation_date(users):
    return sorted(users, key=lambda x: x['creation_date'])


def read_json_file(filepath):
    import json
    with open(filepath, 'r') as file:
        return json.load(file)


def write_json_file(filepath, data):
    import json
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)