import random
from user import User


def main():

    while True:
        print("Sup !This a password locker system")
        print('\n')
        print("Input a shortcut to navigate through the system:to create a new user Use 'nu': To login to the system use 'lg' or 'ex' to exit the system")
        short_code = input().lower()
        print('\n')

        if short_code == 'nu':
            print('create username')
            create_user_name = input()

            print('create password')
            create_user_password = input()

            print ('confirm password')
            confirm_password = input()


            while confirm_password != create_user_password:
                print ("invalid password did not match!")
                print("enter your password")
                create_user_password = input()
                print("confirm the password !hehe")
                confirm_password = input()
                else:
                    print(f"congrats (create_user_name): account creation successful")
                    print('\n')
                    print("proceed to login")
                    entered_username = input()
                    print("your password")
                    entered_password = input()

                while entered_username != create_user_name or entered_password != create_user_password:
                    print("invalid username or password")
                    print ("Username")
                    entered_username = input()
                    print("Your password")
                    entered_password = input()

                else:
                    print(f"welcome: (entered_username) to your account")
                    print("\n")
            elif short_code == 'lg':
                print("welcome")
                print("enter user name")
                default_user_name = input()

                print("Enter password")
                default_user_password = input()
                print('\n')
                while default_user_name != 'testuser' or default_user_password != '00000':
                    print("Wrong userName or password.Username 'testUser' and password '00000'")
                    print("Enter user name")
                    default_user_name = input()
                    print("\n")
                else:
                    print("Login success")
                    print('\n')
                    print('\n')

            elif short_code == 'ex':
                break
            else:
                print("Enter valid code to continue")

if __name__ == '__main__':
    main()

