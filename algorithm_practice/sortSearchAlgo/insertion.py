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
print(new_cabinet)