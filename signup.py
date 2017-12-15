import os
import requests
from getpass import getpass

import settings

def is_username_valid(username):
    if (3 <= len(username) <= 100
        and username.replace('_', '').isalnum()
        and (username[0].isalpha() or username[0] == '_')
):
        return True
    return False

def is_password_valid(password):
    if len(password) >= 8:
        return True
    return False

def is_name_valid(name):
    if 0 <= len(name) <= 100:
        return True
    return False

def register(name, username, password):
    # This function is for the registration request.
    global e
    payload = dict(name=name, username=username, password=password)
    r = requests.post(settings.urls['signup'], data=payload)
    if r.ok:
        e = r.text
        return True
    elif r.status_code == 400:
        e = r.text
        return False
    else:
        o = open('theClientUnchained.log', mode='w')
        o.write(r.text)
        o.close()
        e = "Unknown error has occured. The response has been logged in theClientUnchained.log."
        return False

def main():
    global e
    e = ""
    done = False
    while True:
        os.system("clear")
        if done:
            print(e + "\n")
            input()
            return
        e = "Fill in your data. " + e
        print(e + "\n")
        name = str(input("Enter your name: "))
        if not is_name_valid(name):
            e = "Enter your name."
            continue
        username = str(input("Enter your username: "))
        if not is_username_valid(username):
            e = "Your username must only contain letters, numbers, and underscores. It may not start with a number."
            continue
        password = str(getpass(prompt="Enter your password: "))
        if not is_password_valid(password):
            e = "Your password must be longer than 8 characters."
            continue
        done = register(name, username, password)
