import time

class NetworkError(Exception):
    pass

class MaxRetryExceeded(Exception):
    pass

class Retry:
    def __init__(self, max_retries=3, delay=1):
        self.max_retries = max_retries
        self.delay = delay

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < self.max_retries:
                try:
                    return function(*args, **kwargs)
                except NetworkError:
                    attempts += 1
                    if attempts == self.max_retries:
                        raise MaxRetryExceeded("Max retries exceeded")
                    time.sleep(self.delay)
                    self.delay *= 2  # Exponential backoff
        return wrapper

# Example usage of the retry logic
def unreliable_network_operation():
    import random
    if random.choice([True, False]):
        raise NetworkError("Network Failure")
    return "Success!"

reliable_operation = Retry(max_retries=5, delay=2)(unreliable_network_operation)

if __name__ == "__main__":
    try:
        print(reliable_operation())
    except MaxRetryExceeded as e:
        print(e)
