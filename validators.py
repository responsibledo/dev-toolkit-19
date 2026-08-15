def validate_username(username):
    if not isinstance(username, str):
        raise TypeError('Username must be a string')
    if len(username) < 3 or len(username) > 20:
        raise ValueError('Username must be between 3 and 20 characters')
    if not username.isalnum():
        raise ValueError('Username must be alphanumeric')
    return True

def validate_password(password):
    if not isinstance(password, str):
        raise TypeError('Password must be a string')
    if len(password) < 8:
        raise ValueError('Password must be at least 8 characters long')
    if not any(char.isdigit() for char in password):
        raise ValueError('Password must contain at least one digit')
    if not any(char.isupper() for char in password):
        raise ValueError('Password must contain at least one uppercase letter')
    return True

def validate_email(email):
    import re
    if not isinstance(email, str):
        raise TypeError('Email must be a string')
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        raise ValueError('Invalid email format')
    return True

