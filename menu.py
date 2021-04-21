from hash_maker import password
import pyperclip
from database_manager import insert_password, find_users, find_password

def menu():
    print("--"*50)
    print(("*"*50)+ "MENU" + ("*"*50))
    print('1. Create new password')
    print('**'*15)
    print('2. Get user details')
    print('**'*15)
    print('3. Get password')
    print('**'*15)
    print('Q. Exit')
    print("--"*50)
    return input(': ')

def create_password():
    print("--"*50)
    user_name = input('Please provide a username for the app or website : ')
    if user_name == None:
        user_name = ''
    print("**"*30)
    plaintext = input('Please provide a password for the app or website : ')
    passw = password(plaintext, user_name)
    pyperclip.copy(passw)
    print("**"*30)
    print("Your password has now been created and copied to your clipboard")
    print("**"*30)
    user_email = input('Please provide the email which used to login to app or website : ')
    print("**"*30)
    app_name = input('Please provide the name of the application for which you are saving password : ')
    print("**"*30)
    url = input('Please paste the url to the site that you are saving password for : ')
    print("--"*30)
    insert_password(user_name, passw, user_email, app_name, url)

def find():
    print('Please provide the name of the app or site you want to find the password to : ')
    print("  "*50)
    print("**"*50)
    app_name = input("Enter the APP NAME : ")
    find_password(app_name)

def user():
    print("Please provide the email and app name to find user details : ")
    print("  "*50)
    print("**"*50)
    user_email = input("Enter the email id : ")
    print("**"*50)
    find_users(user_email)

