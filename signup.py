import requests

def is_username_valid(username):
    if len(username) >= 3 and username.replace('_', '').isalnum() and (username[0].isalpha() or username[0] == '_'):
        return True
    return False

def is_password_valid(password):
    if len(password) >= 8:
        return True
    return False

def is_name_valid(name):
    if name:
        return True
    return False

def register(name, username, password):
    pass

def main():
    e = ""
    while True:
        e = "Fill in your data. " + e
        name = str(input("Enter your name: "))
        if not is_name_valid(name):
            e = "Enter your name."
            continue
        username = str(input("Enter your username: "))
        if not is_username_valid(username):
            e = "Your username must only contain letters, numbers, and underscores. It may not start with a number."
            continue
        password = str(input("Enter your password: "))
        if not is_password_valid(password):
            e = "Your password must be longer than 8 characters."
            continue
        if register(name, username, password):
            return
