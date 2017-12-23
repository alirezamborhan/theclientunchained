#! /usr/bin/python3

import os
import requests
from getpass import getpass

import settings

def is_username_valid(username):
    """Check to see if username is valid."""
    if username:
        return True
    return False

def is_password_valid(password):
    """Check to see if password is valid."""
    if password:
        return True
    return False

def login(username, password, session):
    """Send registeration request."""
    global e
    payload = dict(username=username, password=password)
    try:
        r = session.post(settings.urls['signin'], data=payload)
    except requests.exceptions.ConnectionError:
        e = "Connection failed! Try again."
        return False
    if r.ok:
        e = r.text
        return True
    elif r.status_code == 400 or r.status_code == 403:
        # Check for errors.
        e = r.text
        return False
    else:
        # Log.
        o = open('theClientUnchained.log', mode='w')
        o.write(r.text)
        o.close()
        e = "Unknown error occured. The response has been logged in theClientUnchained.log."
        return False

def main(session):
    """Try to sign in with your session."""
    global e
    e = ""
    done = False
    try:
        while True:
            os.system("clear")
            if done:
                print(e + "\nNow press enter to return to the menu.\n")
                input()
                return True
            e = e + (' ' if e else '') + "Enter your username and password. Use Ctrl+C to return to menu."
            print(e + "\n")
            username = str(input("Enter your username: "))
            if not is_username_valid(username):
                e = "Don't leave the field empty."
                continue
            password = str(getpass(prompt="Enter your password: "))
            if not is_password_valid(password):
                e = "Don't leave the field empty."
                continue
            done = login(username, password, session)
    except KeyboardInterrupt:
        return False
