# Лабораторная работа №5, вариант 2
# Тема: строки. Проверка строки на палиндром
# Регистр, пробелы и спецсимволы не учитываются

def clean_text(text):
    # оставляем только буквы и цифры, приводим к нижнему регистру
    result = ''
    for ch in text:
        if ch.isalnum():
            result += ch.lower()
    return result


def is_palindrome(text):
    # палиндром читается одинаково в обе стороны
    return text == text[::-1]


print("Проверка строки на палиндром")
print("Регистр, пробелы и спецсимволы не учитываются.")

line = input("Введите строку: ")

if line.strip() == '':
    print("Ошибка: строка пустая.")
else:
    cleaned = clean_text(line)
    if cleaned == '':
        print("Ошибка: в строке нет букв и цифр.")
    else:
        print("Строка без лишних символов:", cleaned)
        if is_palindrome(cleaned):
            print("Результат: это палиндром.")
        else:
            print("Результат: это не палиндром.")
