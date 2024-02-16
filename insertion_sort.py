import time
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

random_list = [random.randint(0, 999999) for _ in range(50000000)]

start_time = time.time()
insertion_sort(random_list)
end_time = time.time()

print(f"Sorting by inserts took {end_time - start_time} sec")

