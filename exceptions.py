import time
import random

class NetworkError(Exception):
    pass

class Retry:
    def __init__(self, attempts=3, delay=1, backoff=2):
        self.attempts = attempts
        self.delay = delay
        self.backoff = backoff

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, self.attempts + 1):
                try:
                    return func(*args, **kwargs)
                except NetworkError as e:
                    if attempt == self.attempts:
                        raise
                    wait_time = self.delay * (self.backoff ** (attempt - 1))
                    time.sleep(wait_time)
                    print(f'Retrying... (Attempt {attempt})')
        return wrapper

@Retry(attempts=5, delay=2)
def fetch_data(url):
    if random.choice([True, False]):  # Simulate a network issue
        raise NetworkError('Network failed')
    return f'Data from {url}'

if __name__ == '__main__':
    print(fetch_data('http://example.com'))