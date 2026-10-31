# Лабораторная работа 3, вариант 2
# Факториал n! и сумма ряда 1 + 1/2! + ... + 1/n!

# Ввод n с проверкой (do-while: while True + break)
while True:
    text = input("Введите n (целое число, n >= 1): ")
    try:
        n = int(text)
    except ValueError:
        print("Ошибка: нужно целое число")
        continue
    if n < 1:
        print("Ошибка: n должно быть не меньше 1")
        continue
    break

# Факториал n! циклом for
fact = 1
for i in range(1, n + 1):
    fact *= i

# Сумма ряда 1 + 1/2! + ... + 1/n!
# факториал накапливаем по ходу, чтобы не считать его заново
total = 1.0
term_fact = 1
for i in range(2, n + 1):
    term_fact *= i
    total += 1 / term_fact

print(f"{n}! = {fact}")
print(f"Сумма ряда = {total:.6f}")
