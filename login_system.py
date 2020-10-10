from database import users

def usernames(users):
    usernames = []
    for user in users:
        [username, password] = user
        usernames.append(username)
    return usernames


account = input("Would you like to create an account? Answer 'yes' or 'no'.\n")
if account == 'yes' or account == 'y':
    while True:
        username = input("Enter a username: ")
        
        if username in usernames(users):
            print('Username has already been taken')
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
                        print("users:", users)
                        break
                    else:
                        print("Passwords do not match.")
        break
elif account == 'no' or 'n':
    exit()
