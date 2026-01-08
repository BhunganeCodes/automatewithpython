def insert_cabinet(cabinet, to_insert):
    global stepcounter
    check_location = len(cabinet) - 1
    insert_location = 0
    
    while check_location >= 0:
        stepcounter += 1
        if to_insert > cabinet[check_location]:
            insert_location = check_location + 1
            check_location = -1
        check_location -= 1
    stepcounter += 1
    cabinet.insert(insert_location, to_insert)
    return cabinet

def insertion_sort(cabinet):
    global stepcounter
    newcabinet = []
    while len(cabinet) > 0:
        stepcounter += 1
        to_insert = cabinet.pop(0)
        newcabinet = insert_cabinet(newcabinet, to_insert)
    return newcabinet

oldcabinet = [8,4,6,1,2,5,3,7]
stepcounter = 0
sorted_cabinet = insertion_sort(oldcabinet)

# Create function to count steps and generate random, unordered list of numbers
import random

def check_steps(size_of_cabinet):
    global stepcounter
    stepcounter = 0
    cabinet = [int(1000 * random.random()) for _ in range(size_of_cabinet)]
    sorted_cabinet = insertion_sort(cabinet)
    return stepcounter

# Let's create a list of random numbers between 1 and 100
random.seed(5040)
xs = list(range(1, 100))
ys =[check_steps(x) for x in xs]

# Visualize the data
import matplotlib.pyplot as plt

plt.plot(xs, ys)
plt.title("Steps Required for Inserion Sort for Random Cabinets")
plt.xlabel("Number of Files in Random Cabinet")
plt.ylabel("Steps Required to Sort Cabinet - Insertion Sort")
plt.show()