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
print(stepcounter)
