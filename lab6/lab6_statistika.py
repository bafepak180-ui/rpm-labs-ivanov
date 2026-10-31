"""Лабораторная работа №6, вариант 2.
Статистика: Sum, Average, Min, Max, Count.
"""

import unittest
from unittest.mock import patch


# ---------- Ввод ----------

def read_numbers():
    """Запрашивает числа через пробел и возвращает список float."""
    while True:
        text = input("Введите числа через пробел: ").strip()
        if text == "":
            print("Пустой ввод, повторите.")
            continue
        try:
            return [float(item) for item in text.split()]
        except ValueError:
            print("Это не числа, повторите.")


# ---------- Обработка ----------

def calc_sum(numbers):
    """Возвращает сумму чисел списка."""
    return sum(numbers)


def calc_average(numbers):
    """Возвращает среднее арифметическое или None, если список пуст."""
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)


def calc_min(numbers):
    """Возвращает минимальное число или None, если список пуст."""
    if len(numbers) == 0:
        return None
    return min(numbers)


def calc_max(numbers):
    """Возвращает максимальное число или None, если список пуст."""
    if len(numbers) == 0:
        return None
    return max(numbers)


def calc_count(numbers):
    """Возвращает количество чисел в списке."""
    return len(numbers)


# ---------- Вывод ----------

def print_stats(numbers):
    """Печатает статистику по списку чисел."""
    print("Количество:", calc_count(numbers))
    print("Сумма:", calc_sum(numbers))

    average = calc_average(numbers)
    if average is None:
        print("Среднее: нет данных")
    else:
        print("Среднее: {:.3f}".format(average))

    low = calc_min(numbers)
    high = calc_max(numbers)
    if low is None:
        print("Минимум: нет данных")
        print("Максимум: нет данных")
    else:
        print("Минимум:", low)
        print("Максимум:", high)


# ---------- Главное меню ----------

def main():
    """Меню: считает статистику, пока пользователь не выберет выход."""
    while True:
        print("\n1 - ввести числа")
        print("0 - выход")
        choice = input("Выбор: ").strip()

        if choice == "0":
            print("Выход.")
            break
        elif choice == "1":
            numbers = read_numbers()
            print_stats(numbers)
        else:
            print("Нет такого пункта.")


# ---------- Тесты ----------

class TestStats(unittest.TestCase):
    """Тесты функций ввода и обработки."""

    def test_sum(self):
        self.assertEqual(calc_sum([1, 2, 3]), 6)

    def test_average(self):
        self.assertEqual(calc_average([2, 4]), 3)

    def test_average_empty(self):
        self.assertIsNone(calc_average([]))

    def test_min_max(self):
        self.assertEqual(calc_min([5, 1, 3]), 1)
        self.assertEqual(calc_max([5, 1, 3]), 5)

    def test_min_max_empty(self):
        self.assertIsNone(calc_min([]))
        self.assertIsNone(calc_max([]))

    def test_count(self):
        self.assertEqual(calc_count([1, 2, 3, 4]), 4)

    def test_read_numbers(self):
        with patch("builtins.input", side_effect=["abc", "1 2 3"]):
            self.assertEqual(read_numbers(), [1.0, 2.0, 3.0])


if __name__ == "__main__":
    main()
