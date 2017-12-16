#! /usr/bin/python3

import os
import requests
from getpass import getpass

import settings

def is_username_valid(username):
    if username:
        return True
    return False

def is_password_valid(password):
    if password:
        return True
    return False

def login(username, password):
    # This function is for the registration request.
    global e
    payload = dict(username=username, password=password)
    r = requests.post(settings.urls['signin'], data=payload)
    if r.ok:
        e = r.text
        return True
    elif r.status_code == 400 or r.status_code == 403:
        e = r.text
        return False
    else:
        o = open('theClientUnchained.log', mode='w')
        o.write(r.text)
        o.close()
        e = "Unknown error occured. The response has been logged in theClientUnchained.log."
        return False

def main():
    global e
    e = ""
    done = False
    while True:
        os.system("clear")
        if done:
            print(e + "\nNow press enter to return to the menu.\n")
            input()
            return
        e = "Enter your username and password. " + e
        print(e + "\n")
        username = str(input("Enter your username: "))
        if not is_username_valid(username):
            e = "Enter your username."
            continue
        password = str(getpass(prompt="Enter your password: "))
        if not is_password_valid(password):
            e = "Enter your password."
            continue
        done = login(username, password)
