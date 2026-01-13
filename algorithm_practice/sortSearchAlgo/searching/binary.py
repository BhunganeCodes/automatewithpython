import math 

cabinet = [1, 2, 3, 4, 5]
lowerbound = 0
upperbound = len(cabinet)

looking_for = 5
guess = math.floor(len(cabinet) / 2)

if cabinet[guess] > looking_for:
    upperbound = guess
    guess = math.floor((guess + lowerbound) / 2)
if cabinet[guess] < looking_for:
    lowerbound = guess
    guess = math.floor((guess + upperbound) / 2)