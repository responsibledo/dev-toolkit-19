import time
import requests

class NetworkError(Exception):
    pass

class TimeoutError(NetworkError):
    pass

def retry_request(url, max_retries=3, delay=1):
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            attempts += 1
            print(f'Timeout occurred. Retrying {attempts}/{max_retries}...')
            time.sleep(delay)
        except requests.exceptions.RequestException as e:
            raise NetworkError(f'Network error occurred: {e}') from e
    raise TimeoutError('Max retries exceeded.')