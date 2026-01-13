import math 

cabinet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binarysearch(cabinet, looking_for):
    guess = math.floor(len(cabinet) / 2)
    upperbound = len(cabinet)
    lowerbound = 0

    while abs(cabinet[guess] - looking_for) > 0.0001:
        if cabinet[guess] > looking_for:
            upperbound = guess
            guess = math.floor((guess + lowerbound) / 2)
        if cabinet[guess] < looking_for:
            lowerbound = guess
            guess = math.floor((guess + upperbound) / 2)
    return guess

print(binarysearch(cabinet, 8))