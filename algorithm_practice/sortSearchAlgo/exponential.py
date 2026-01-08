import random, math
import matplotlib.pyplot as plt
import numpy as np

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

def check_steps(size_of_cabinet):
    global stepcounter
    stepcounter = 0
    cabinet = [int(1000 * random.random()) for _ in range(size_of_cabinet)]
    sorted_cabinet = insertion_sort(cabinet)
    return stepcounter

random.seed(5040)
xs = list(range(1, 100))
ys = [check_steps(x) for x in xs]
ys_exp = [math.exp(x) for x in xs]

plt.plot(xs, ys)
axes = plt.gca()
axes.set_ylim([np.min(ys), np.max(ys) + 140])

plt.plot(xs, ys_exp)
plt.title("Comparing Insertion Sort to the Exponential Function")
plt.xlabel("Number of Files in Random Cabinet")
plt.ylabel("Number of Steps Required to Sort Cabinet")
plt.show()