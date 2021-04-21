import getpass
from menu import menu, create_password, find, user

master_password = getpass.getpass('Please provide the master password for the password manager : ')

if master_password == 'sh<>:"123':
    choice_choosen = menu()

    while choice_choosen != 'Q':
        if choice_choosen == '1':
            create_password()
            exit()
        if choice_choosen == '2':
            user()
            exit()
        if choice_choosen == '3':
            find()
            exit()
        else:
            choice_choosen = menu()
    exit()

else:
    print("_______________________________ENTRY DECLINED__________________________")
