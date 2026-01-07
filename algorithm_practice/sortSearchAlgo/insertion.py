# Insertion Sort Algorithm

def insert_cabinet(cabinet, to_insert):
    check_location = len(cabinet) - 1
    insert_location = 0
    
    while check_location >= 0:
        if to_insert > cabinet[check_location]:
            insert_location = check_location + 1
            check_location = -1
        check_location -= 1
    cabinet.insert(insert_location, to_insert)
    return cabinet

cabinet = [1, 2, 3, 3, 6, 8, 12]
new_cabinet = insert_cabinet(cabinet, 5)

# Using Insertion Sort Algo - Old, Unsorted Cabinet to New Sorted Cabinet
oldcabinet = [8,4,6,1,2,5,3,7]

def insertion_sort(cabinet):
    newcabinet = []
    while len(cabinet) > 0:
        to_insert = cabinet.pop(0)
        newcabinet = insert_cabinet(newcabinet, to_insert)
    return newcabinet

sorted_cabinet = insertion_sort(oldcabinet)
print(sorted_cabinet)