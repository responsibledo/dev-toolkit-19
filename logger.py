import logging

class CustomLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        handler = logging.FileHandler(f'{name}.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.DEBUG)

    def log_info(self, message):
        self.logger.info(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_exception(self, message):
        self.logger.exception(message)

    def log_debug(self, message):
        self.logger.debug(message)

    def check_log_file(self):
        try:
            with open(f'{self.logger.name}.log', 'r') as file:
                return True
        except FileNotFoundError:
            self.log_warning('Log file not found, creating a new one.')
            return False
        except Exception as e:
            self.log_error(f'Unexpected error: {e}')
            return False

logger = CustomLogger(__name__)
logger.log_info('Logger initialized.')