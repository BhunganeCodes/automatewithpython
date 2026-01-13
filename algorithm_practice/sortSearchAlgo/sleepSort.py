# To implement sleep sort algorithm below...
import threading
from time import sleep

def sleep_sort(i):
    global sorted_list
    sleep(i)
    sorted_list.append(i)
    return i

items = [2, 4, 5, 2, 1, 7]
sorted_list = []
ignore_result = [threading.Thread(target=sleep_sort, args=(i,)).start() for i in items]

print(ignore_result)