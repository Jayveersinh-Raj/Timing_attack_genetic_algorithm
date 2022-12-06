import random, string
import timeit
import numpy as np
from Database.database import database

def check_password(user, guess):
    actual = database[user]

    if len(str(guess)) != len(str(actual)):
        return False

    for i in range(len(actual)):
        if guess[i] != actual[i]:
            return False
    return True

## Random string generator
def random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

def crack_length(user, max_length) -> int:
    trials = 100
    times = np.empty(max_length)
    for i in range(max_length):
        time_taken = timeit.repeat(stmt = 'check_password(user, str)',
                                   setup = f'user = {user!r}; str = random_string({i!r})',
                                   globals = globals(),
                                   number = trials,
                                   repeat=10)
        times[i] = min(time_taken)
    
    most_likely_n = np.argsort(times)[::-1][:5]
    return (most_likely_n, times[most_likely_n] / times[most_likely_n[0]])


