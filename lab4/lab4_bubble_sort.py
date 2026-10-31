# Лабораторная работа №4, вариант 2
# Случайный массив, сортировка пузырьком, вывод до и после

import random

# ввод размера массива с проверкой
while True:
    try:
        n = int(input("Введите размер массива: "))
        if n > 0:
            break
        print("Размер должен быть больше нуля")
    except ValueError:
        print("Нужно ввести целое число")

# заполнение массива случайными числами
arr = []
for i in range(n):
    arr.append(random.randint(-50, 50))

print("Массив до сортировки:")
print(arr)

# сортировка пузырьком
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Массив после сортировки:")
print(arr)
