# Write a small function that returns the values of an array that are not odd.
# All values in the array will be integers. Return the good values in the order they are given.

def no_odds(values):
    no_odds = []
    for i in values:
        if i % 2 == 0:
            no_odds.append(i) 
    return no_odds

# Short version
def no_odds(values):
    return [i for i in values if i % 2 == 0] 
