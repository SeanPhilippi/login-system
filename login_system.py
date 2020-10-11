# run program using sudo
from database import users
import keyboard

account = input("Would you like to create an account? Answer 'yes' or 'no'.\n")
if account == 'yes' or account == 'y':
    while True:
        username = input("Enter a username: ")
        
        # read database.txt
        with open('database.txt', 'r', encoding='utf-8-sig') as db:
            lines = db.readlines()
            taken = False
            for line in lines:
                line = line.split(', ')
                user = line[0][10:]
                if username == user:
                    print('Username has already been taken')
                    taken = True
                    break

        if taken:
            continue
        else:
            while True:
                password = input("Enter a password: ")
                # check password for length, special characters, and capitalized character
                # in future, maybe give a rating based on password strength, find a library for this?
                if len(password) < 8:
                    print("Password is too short. Must be at least 8 characters")
                else:
                    confirm_password = input("Enter your password again to confirm: ")
                    if password == confirm_password:
                        with open('database.txt', 'a') as db:
                            db.write('username: ' + username + ', password: ' + password + '\n')
                        print("Account successfully created!")
                        # print("users:", users)
                        break
                    else:
                        print("Passwords do not match.")
                        continue
            print('Account successfully created!')
            # print('Press esc to exit')
            # print('Your username and password will be sent to your email.')
            # if keyboard.is_pressed('esc'):
            #    exit()
elif account == 'no' or 'n':
    exit()
