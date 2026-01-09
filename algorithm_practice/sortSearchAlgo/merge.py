def merge(left, right):
    newcabinet = []
    while min(len(left), len(right)) > 0:

        if left[0] > right[0]:
            to_insert = right.pop(0)
            newcabinet.append(to_insert)

        elif left[0] <= right[0]:
            to_insert = left.pop(0)
            newcabinet.append(to_insert)

    if len(left) > 0:
        for item in left:
            newcabinet.append(item)

    if len(right) > 0:
        for item in right:
            newcabinet.append(item)
    return newcabinet

left = [1, 3, 4, 4, 5, 7, 8, 9]
right = [2, 4, 6, 7, 8, 8, 10, 12, 13, 14]
newcab = merge(left, right)

# Merge to Sort
import math

def mergesort_two_elements(cabinet):
    new_cabinet = []
    if len(cabinet) == 1:
        new_cabinet = cabinet
    else:
        left = cabinet[:math.floor(len(cabinet) / 2)]
        right = cabinet[math.floor(len(cabinet) / 2):]
    return new_cabinet