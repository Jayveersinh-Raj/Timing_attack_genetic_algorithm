from Length.crack_length import crack_length

## Function to return the findings
def find_length(user, max_length) -> int:
    
    ## Empty list to store output from 10 tries
    tries = []

    ## Trying 10 times
    for i in range(10):
      tries.append(crack_length(user, max_length)[0][0])

    ## Getting the most frequent 
    return max(set(tries), key = tries.count)
