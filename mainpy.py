#!/usr/bin/env

def set_firstName(firstName):
    return firstName

def set_lastName(lastName):
    return lastName

def set_username(username):
    return username

def get_fullName():
    fullName = set_firstName(firstName) + " " + set_lastName(lastName)
    return fullName
def is_valid_userName(userName):
    if userName == "pgPasci" or userName == "pgAmazu":
        return True
    return False

def say_Hello():
    print(f"Hello Mr. {get_fullName()} Welcome to \'Tanjawa\' Organization".title().strip().center(20,' '))

def out_Of_Organization():
    print(f"{set_username(username)} your not in \'Tanjaawa\' Organization")
    
firstName = input("Enter Your firstName : ")
set_firstName(firstName)

lastName = input("Enter Your lastName : ")
set_lastName(lastName)

username = input("Enter Your Username : ")

if is_valid_userName(username):
    say_Hello()
else :
    out_Of_Organization()
    

