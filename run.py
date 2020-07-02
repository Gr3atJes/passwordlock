import random
import pyperclip
import time
from termcolor import colored, cprint
from getpass import getpass
from credential import Credential
from user import User

def create_user(login_name, pin):
    """
    Function to create a new user
    """
    new_user = User(login_name,pin)
    return new_user

def save_user(user):
    """
    Function to save user details
    """
    user.save_user()

def authenticate_user(username,password):
    return User.user_auth(username,password)

def create_credential(platform,username,email,password):
    """

    Function to create a new credential

    """
    new_credential = Credential(platform,username,email,password)
    return new_credential

def delete_credential(credential):
    """
    Function to delete a credential
    """
    credential.delete_Credential()

def find_credentials(platform):
    """
    Function that finds a credential by platform name and returns the
    """
    return Credential.find_by_platform(platform)

def check_existing_credential(platform):
    """
    Function that checks if a credential exists with that number and return a Boolean
    """
    return Credential.credential_exists(platform)

def display_credentials():
    """
    Function that returns all the saved credentials
    """
    return Credential.display_credentials()

def copy_password(platform):
    """
    Function that copies the password
    """
    return Credential.copy_password(platform)

def generate_password(length):
    """
    Function which generates a random password

    Args:
        The desired password length
    """
    return Credential.generate_password(length)

def main():
    cprint("""
    Yoo welcome to the password locker.Enhanced Security
    ""","blue")
    while True:
        cprint("""
        Use the short lines to go through the system
        'lg' - login
        'xx' - Close app
        ""","blue")
    print("What would you like to do?")
    code = input().lower()
    if code == "lg":
        print("Do you have an account? Y or N")
        decision = input().lower()

        if decision.startswith("n"):
            login_name = input("Enter your username:")
            login_pin = getpass("Enter your pin: ")
            print("Loading....")
            time.sleep(1.5)
            print("\n")
            cprint("CONGRATS,YOUR ACCOUNT HAS BEEN CREATED","green",attrs=['bold'])
            print("Sign in into your account")
            sign_in_name = input("Enter your username:")
            sign_in_pin = getpass("Enter your pin:")
            save_user(create_user(login_name, login_pin))
            if authenticate_user(sign_in_name, sign_in_pin):
                print("Please wait...")
                time.sleep(1.5)
                cprint("SUCCESSFULY MADE IT TO THE SYSTEM","green",attrs=['bold'])
                print("\n")
                pass 
            else:
                sign_in_name = input("Enter your username:")
                sign_in_pin = getpass("Enter your pin:")
                if authenticate_user(sign_in_name, sign_in_pin):
                    print("Please wait..")
                    time.sleep(1.5)
                    cprint("Successfully signed in","green",attrs=['bold'])
                    print("\n")
                    pass
                ----------------------

            while True:
                if authenticate_user(sign_in_name, sign_in_pin):
                    ####
                    cprint(
                        """
                        O===[================-
                        WELCOME TO YOUR PASSWORD LOCKER:
                        Use the commands to navigate through the system :):

                         'cc' - To create a credential
                         'dc' - displays the credentials you have entered
                         'cp' - copy the password of a credential
                         'fc' - helps you find a credential by its platform name
                         'dl' - deletes a credential
                         'ex' - logs you out lol
                         'help' - helps a user around the system
                                  ""","blue")
                              print(f"At your service {sign_in_name}, what task would you like to perform?")
                              key_word = input().lower()

                              if key_word == 'cc':
                                  print