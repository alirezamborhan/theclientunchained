#! /usr/bin/python3

import os
import requests

import settings

def logout(session):
    global e
    
    try:
        r = session.get(settings.urls["signout"])
    except requests.exceptions.ConnectionError:
        e = "Connection failed!"
        return True
    if r.ok or r.status_code == 400:
        e = r.text
        return False
    else:
        o = open('theClientUnchained.log', mode='w')
        o.write(r.text)
        o.close()
        e = "Unknown error occured. The response has been logged in theClientUnchained.log."
        return True

def main(session):
    # returns whether we are still logged in.
    global e
    e = ""
    os.system("clear")
    result = True
    try:
        result = logout(session)
        print(e + "\n")
        input()
        return result
    except KeyboardInterrupt:
        return result
