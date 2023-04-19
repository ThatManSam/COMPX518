import base64
from argon2 import PasswordHasher
from getpass import getpass
import os
import re
import argon2
from better_profanity import profanity
import sqlite3

db: sqlite3.Connection | None = None

pepper = b'LV3rYF/C00W2txXdKdlgEw=='

DB_NAME = "accounts.db"

DB_ACCESS_ERROR = """
There was an error accessing the database"""

DB_INITIALISE = """
CREATE TABLE IF NOT EXISTS accounts(
    username TEXT PRIMARY KEY,
    password TEXT,
    salt TEXT
);
"""

MSG_WELCOME = """
Welcome to Assignment 1"""

OPT_LOGIN = "1"
OPT_REGISTER = "2"
OPT_EXIT = "3"

MSG_OPTIONS = f"""
You can login with your existing account
If you don't have an account you need to register an account
Options:
    {OPT_LOGIN}. Login
    {OPT_REGISTER}. Register
    {OPT_EXIT}. Exit"""

MSG_OPTIONS_ASK = f"""
Please select option ({OPT_LOGIN}, {OPT_REGISTER} or {OPT_EXIT}): """

LGN_INFO = """
Login
To login enter the username and password you used to register
"""

LGN_USER_ASK = """
Please enter your Username: """

LGN_PASS_ASK = """
Please enter your Password: """

LGN_INCORRECT = """
Login FAILED
Incorrect Username or Password"""

LGN_DENIED = """
Too many failed login attempts. Exiting..."""

LGN_SUCCESS = """
Successfully logged in as {}"""

LGN_MAX_ATTEMPTS = 3


def login():
    
    username = input("Please enter username: ")
    for _ in range(0, LGN_MAX_ATTEMPTS):
        password = getpass("Please enter password: ")
    
        if db is None:
            print(DB_ACCESS_ERROR)
            exit(1)
        
        curr = db.execute("SELECT * FROM accounts WHERE username == ?", (username,))
        user = curr.fetchone()
        if user is None:
            print(LGN_INCORRECT)
            continue
            
        _, saved_hash, saved_salt = user
        
        ph = PasswordHasher()
        try:
            ph.verify(
                bytes(saved_hash, 'utf-8'),
                bytes(password, 'utf-8') + bytes(saved_salt, 'utf-8') + pepper
            )
        except (argon2.exceptions.VerifyMismatchError, argon2.exceptions.InvalidHash):
            print(LGN_INCORRECT)
        else:
            print(LGN_SUCCESS.format(username))
            return
        
    print(LGN_DENIED)
    exit(1)
        
    
    # print("Login")


REG_USER_INFO = """
Username
The username can only contain:
 - UPPERCASE letters
 - lowercase letters
 - Numbers (0-9)
 - An underscore '_'
 
The username cannot contain profanity"""

REG_USER_ASK = """
Please enter a Username: """

REG_USER_VALID_REGEX = r'^[a-zA-Z0-9_]+$'

REG_USER_INVALID = """
!! That username does not match the requirements"""

REG_USER_PROFANE = """
!! That username contains profanity"""

REG_USER_UNIQUE = """
!! That username is already associated with another account"""


REG_PASS_INFO = """
Password
The Password can only contain:
NEED TO MAKE REQUIREMENTS"""

REG_PASS_ASK = """
Please enter a Password: """

REG_PASS_VALID_REGEX = r'^[.]+$'

REG_PASS_INVALID = """
!! That password does not match the requirements"""

REG_PASS_WEAK = """
!! That password is too weak"""

REG_PASS_BREACHED = """
!! That password is a known breached password, please use a different password"""

def register():
    username = ''
    while True:
        # Show Username information
        print(REG_USER_INFO)
        
        # Enter username
        username = input(REG_USER_ASK)
        
        # Check username is valid
        if not re.match(REG_USER_VALID_REGEX, username):
            print(REG_USER_INVALID)
            continue
        
        # Check for profanity
        if profanity.contains_profanity(username):
            print(REG_USER_PROFANE)
            continue
        
        # Check that username is unique
        if db is None:
            print(DB_ACCESS_ERROR)
            exit(1)
            
        curr = db.execute("SELECT username FROM accounts WHERE username == ?", (username,))
        if curr.fetchone is None:
            print(REG_USER_UNIQUE)
            continue
        
        # Valid and clean username
        break
    
    password = ''
    while True:
        # Show password information
        print(REG_PASS_INFO)
        
        # Enter password
        password = getpass(REG_PASS_ASK)
        
        # TODO: set password requirements
        # Check password is valid
        if re.match(REG_PASS_VALID_REGEX, password):
            print(REG_PASS_INVALID)
            continue
        
        # TODO: Implement this checking
        # Check password is not weak or breached
        # if profanity.contains_profanity(password):
        #     print(REG_PASS_WEAK)
        #     print(REG_PASS_BREACHED)
        #     continue
        
        # Valid, strong and safe password
        break    
    
    # Generate salt for password
    salt = os.urandom(16)
        
    # Combine password, salt and pepper    
    full_password = bytes(password, 'utf-8') + salt + pepper
    
    # Hash the password (with password hashing algorithm)
    ph = PasswordHasher()
    hashed = ph.hash(full_password)
        
    # Add the new user to Database (username, password and salt)
    if db is None:
        print(DB_ACCESS_ERROR)
        exit(1)
    
    curr = db.execute("INSERT INTO accounts VALUES(?, ?, ?)", (username, hashed, salt))
    
    print(f"Registered user: '{username}' with password: '{password}'")


if __name__ == "__main__":
    print(MSG_WELCOME)
    
    # Initialise database
    with sqlite3.connect(DB_NAME) as _db:
        db = _db
        db.execute(DB_INITIALISE)
        db.commit()
        
        print(MSG_OPTIONS)
        while True:
            option = input(MSG_OPTIONS_ASK)
            if option == "":
                pass
            elif option == OPT_LOGIN:
                login()
                break
            elif option == OPT_REGISTER:
                register()
                break
            elif option == OPT_EXIT:
                print("Exiting...")
                exit(0)
            else:
                print(f"Invalid option '{option}'. Exiting...")
                exit(1)        
