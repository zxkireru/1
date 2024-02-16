import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# ���������� ������
random_list = [random.randint(0, 999999) for _ in range(50000000)]

# �������� ����� ����������
start_time = time.time()
bubble_sort(random_list)
end_time = time.time()

print(f"���������� ��������� ������ {end_time - start_time} ������")



