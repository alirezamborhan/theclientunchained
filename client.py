#! /usr/bin/python3

import os
import requests

import signup
import signin
import dummy
import signout

def main():
    e = ""
    session = requests.Session()
    loggedin = False
    try:
        while True:
            os.system("clear")
            print(e)
            e = ""
            if not loggedin:
                print("What do you wish to do?\n")
                print("1. Sign up")
                print("2. Sign in")
                print("3. Exit\n")
                inp = str(input())
                if inp == '1':
                    signup.main(session)
                elif inp == '2':
                    loggedin = signin.main(session)
                elif inp == '3':
                    print("Fairwell!")
                    break
                else:
                    e = "Enter 1, 2, or 3."
            else:
                print("What do you wish to do?\n")
                print("1. Dummy page")
                print("2. Log out")
                print("3. Exit\n")
                inp = str(input())
                if inp == '1':
                    loggedin = dummy.main(session)
                elif inp == '2':
                    loggedin = signout.main(session)
                elif inp == '3':
                    print("Fairwell!")
                    break
                else:
                    e = "Enter 1, 2, or 3."
    except KeyboardInterrupt:
        print("Fairwell!")

main()
