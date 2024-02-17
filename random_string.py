import random

random_string = ''.join([chr(random.randint(33, 126)) for _ in range(1000)])

file_name = "random_string.txt"
with open(file_name, 'w') as file:
    file.write(random_string)

print("Строка из случайных символов успешно записана в файл", file_name)
