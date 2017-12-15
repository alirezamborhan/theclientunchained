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
    global url
    payload = dict(name=name, username=username, password=password)
    r = requests.post(url, data=payload)
    ####  Debugging the requests.
    o = open('LOG', mode='w')
    o.write(r.text)
    o.close()
    print(r.text)
    input()
    ####
    return True

def main():
    e = ""
    global url
    url = "http://127.0.0.1:8000/signup/"
    while True:
        e = "Fill in your data. " + e
        print(e)
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
