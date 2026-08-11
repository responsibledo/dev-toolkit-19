import re
from typing import Any, Dict

class InputValidator:
    @staticmethod
    def is_email(email: str) -> bool:
        email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        return re.match(email_regex, email) is not None

    @staticmethod
    def is_positive_integer(value: Any) -> bool:
        if isinstance(value, int) and value > 0:
            return True
        return False

    @staticmethod
    def validate_data(data: Dict[str, Any]) -> Dict[str, str]:
        errors = {}
        if 'email' in data:
            if not InputValidator.is_email(data['email']):
                errors['email'] = 'Invalid email format'
        if 'age' in data:
            if not InputValidator.is_positive_integer(data['age']):
                errors['age'] = 'Age must be a positive integer'
        return errors

