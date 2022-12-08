from Database.database import database

# A function that matches the password, analogous to back end server that performs the computation
def check_password(user, guess) -> bool:
    actual = database[user]

    for i in range(len(actual)):
        if str(guess)[i] != actual[i]:
            return False
    return True