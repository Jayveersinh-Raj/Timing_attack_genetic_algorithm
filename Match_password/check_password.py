from Database.database import database

def check_password(user, guess):
    actual = database[user]

    for i in range(len(actual)):
        if str(guess)[i] != actual[i]:
            return False
    return True