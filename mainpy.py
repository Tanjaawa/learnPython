#!/usr/bin/env
username = input("Enter Your Username : ")
def set_username():
    return username

def say_Hello():
    print(f"Hello Mr. {set_username()} Welcome to \'Tanjawa\' Organization".title().strip().center(20,' '))
say_Hello()