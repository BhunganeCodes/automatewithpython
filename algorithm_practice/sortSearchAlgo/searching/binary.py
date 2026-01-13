import math 

cabinet = [1, 2, 3, 4, 5]
lowerbound = 0
upperbound = len(cabinet)

looking_for = 5
guess = math.floor(len(cabinet) / 2)

if cabinet[guess] > looking_for:
    print("Too High")
if cabinet[guess] < looking_for:
    print("Too Low")
else:
    print("Correct!!")