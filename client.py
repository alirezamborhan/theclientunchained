#! /usr/bin/python3

import os

import signup
import signin

def main():
    e = ""
    while True:
        os.system("clear")
        print(e)
        e = ""
        print("What do you wish to do?\n")
        print("1. Sign up")
        print("2. Sign in")
        print("3. Exit\n")
        inp = str(input())
        if inp == '1':
            signup.main()
        elif inp == '2':
            signin.main()
        elif inp == '3':
            print("Fairwell!")
            break
        else:
            e = "Enter 1, 2, or 3."

main()
