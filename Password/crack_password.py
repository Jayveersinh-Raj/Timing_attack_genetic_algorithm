import timeit
import numpy as np
from Database.database import database
from Match_password.check_password import check_password

# function that calls check password to measure time, analog of login attempt
def crack_password(user, str) -> int:
  trials = 1000
  time_taken = timeit.repeat(stmt = 'check_password(user, str)',
                                 setup = f'user = {user!r}; input_str = {str!r}',
                                 globals = globals(),
                                 number = trials,
                                 repeat=10)
  return min(time_taken)