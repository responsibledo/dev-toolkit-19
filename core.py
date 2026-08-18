import json

def load_robbie_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f'Error: File not found - {file_path}')
        return {}
    except json.JSONDecodeError:
        print('Error: Failed to decode JSON')
        return {}


def save_robbie_data(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError:
        print(f'Error: Could not write to file - {file_path}')


def update_item(data, key, value):
    if key in data:
        data[key] = value
    else:
        print(f'Warning: Key {key} not found in data')


def get_item(data, key):
    return data.get(key, f'Key {key} not found')


def delete_item(data, key):
    if key in data:
        del data[key]
    else:
        print(f'Warning: Key {key} not found for deletion')


if __name__ == '__main__':
    sample_data = load_robbie_data('data.json')
    print(get_item(sample_data, 'player_stats'))
    update_item(sample_data, 'player_stats', {'score': 100})
    save_robbie_data(sample_data, 'data.json')