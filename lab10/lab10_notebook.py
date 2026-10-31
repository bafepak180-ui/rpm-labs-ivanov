"""
Лабораторная работа №10, вариант 2.
Файл: lab10_notebook.py
Тема: записная книжка — контакты, категории, экспорт в CSV.

ПАСПОРТ МОДУЛЯ
Назначение: программный модуль lab10_notebook.py ведёт простую записную книжку
контактов. Каждый контакт хранится как словарь с полями name (имя), phone (телефон)
и category (категория). Модуль позволяет добавлять контакты, искать их по категории
и выгружать весь список в файл CSV для дальнейшего открытия в Excel или LibreOffice.
Функции модуля:
  add_contact(contacts, name, phone, category) — добавляет контакт в список, проверяет
    пустые имя и телефон, неизвестную категорию заменяет на "другое"; возвращает True/False;
  find_by_category(contacts, category) — возвращает список контактов нужной категории;
  export_csv(contacts, filename) — записывает контакты в CSV-файл, возвращает число строк;
  read_number(prompt) — читает целое число с клавиатуры, повторяет ввод при ошибке;
  main() — консольное меню программы.
Вход: строки имени, телефона и категории, номер пункта меню, имя CSV-файла.
Выход: сообщения в консоли, файл contacts.csv с заголовком name,phone,category.
Ограничения: категории только из набора работа/друзья/семья/другое; телефон хранится
как строка без проверки формата; данные не сохраняются между запусками, кроме экспорта.

РУКОВОДСТВО ПОЛЬЗОВАТЕЛЯ
Запуск программы: python lab10_notebook.py (или python3 lab10_notebook.py).
После запуска появляется меню из пунктов: 1 — добавить контакт, 2 — показать контакты
по категории, 3 — экспорт в CSV, 0 — выход. При выборе пункта 1 программа спросит имя,
телефон и категорию; пустые имя или телефон не принимаются, при неизвестной категории
контакт попадёт в "другое". Пункт 2 выводит все контакты выбранной категории или
сообщение "Ничего не найдено". Пункт 3 сохраняет все контакты в файл contacts.csv
в текущей папке и печатает количество выгруженных записей. Если файл записать нельзя,
выводится сообщение об ошибке без Traceback. Пример работы: добавляем контакт
"Иван", "89001234567", "работа", затем выбираем пункт 3 — в contacts.csv появятся
строки name,phone,category и Иван,89001234567,работа.
Запуск тестов: python -m unittest lab10_notebook.py — все тесты должны пройти.
"""

import csv
import os
import unittest

CSV_FILE = "contacts.csv"
CATEGORIES = ("работа", "друзья", "семья", "другое")


# добавление контакта с проверкой имени, телефона и категории
def add_contact(contacts, name, phone, category="другое"):
    name = name.strip()
    phone = phone.strip()
    if not name or not phone:
        return False
    if category not in CATEGORIES:
        category = "другое"
    contacts.append({"name": name, "phone": phone, "category": category})
    return True


# поиск контактов по категории
def find_by_category(contacts, category):
    return [c for c in contacts if c["category"] == category]


# выгрузка списка контактов в CSV-файл
def export_csv(contacts, filename=CSV_FILE):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "phone", "category"])
        for c in contacts:
            writer.writerow([c["name"], c["phone"], c["category"]])
    return len(contacts)


# чтение числа с клавиатуры с повторным вводом при ошибке
def read_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Нужно число, попробуйте снова.")


def main():
    contacts = []
    while True:
        print("\n1 - добавить, 2 - показать по категории, 3 - экспорт, 0 - выход")
        choice = read_number("Выбор: ")
        if choice == 0:
            break
        elif choice == 1:
            name = input("Имя: ")
            phone = input("Телефон: ")
            category = input("Категория (работа/друзья/семья/другое): ").strip()
            if add_contact(contacts, name, phone, category):
                print("Контакт добавлен.")
            else:
                print("Имя и телефон не могут быть пустыми.")
        elif choice == 2:
            category = input("Категория: ").strip()
            found = find_by_category(contacts, category)
            if not found:
                print("Ничего не найдено.")
            for c in found:
                print(c["name"], c["phone"], c["category"])
        elif choice == 3:
            try:
                count = export_csv(contacts)
                print("Экспортировано записей:", count)
            except OSError:
                print("Не удалось записать файл.")
        else:
            print("Нет такого пункта.")


# unit-тесты для всех функций модуля
class TestNotebook(unittest.TestCase):
    def setUp(self):
        self.contacts = []
        self.filename = "test_contacts.csv"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_add_contact(self):
        self.assertTrue(add_contact(self.contacts, "Иван", "89001234567", "работа"))
        self.assertEqual(len(self.contacts), 1)

    def test_add_empty_name(self):
        self.assertFalse(add_contact(self.contacts, "   ", "89001234567", "работа"))
        self.assertEqual(len(self.contacts), 0)

    def test_add_empty_phone(self):
        self.assertFalse(add_contact(self.contacts, "Иван", "", "работа"))
        self.assertEqual(len(self.contacts), 0)

    def test_add_bad_category(self):
        add_contact(self.contacts, "Иван", "89001234567", "знакомые")
        self.assertEqual(self.contacts[0]["category"], "другое")

    def test_add_strips_spaces(self):
        add_contact(self.contacts, "  Иван  ", " 123 ", "семья")
        self.assertEqual(self.contacts[0]["name"], "Иван")
        self.assertEqual(self.contacts[0]["phone"], "123")

    def test_find_by_category(self):
        add_contact(self.contacts, "Иван", "111", "работа")
        add_contact(self.contacts, "Пётр", "222", "друзья")
        found = find_by_category(self.contacts, "работа")
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]["name"], "Иван")

    def test_find_empty_list(self):
        self.assertEqual(find_by_category(self.contacts, "работа"), [])

    def test_find_unknown_category(self):
        add_contact(self.contacts, "Иван", "111", "работа")
        self.assertEqual(find_by_category(self.contacts, "спорт"), [])

    def test_export_creates_file(self):
        add_contact(self.contacts, "Иван", "111", "работа")
        export_csv(self.contacts, self.filename)
        self.assertTrue(os.path.exists(self.filename))

    def test_export_content(self):
        add_contact(self.contacts, "Иван", "111", "работа")
        export_csv(self.contacts, self.filename)
        with open(self.filename, encoding="utf-8") as f:
            lines = f.read().splitlines()
        self.assertEqual(lines[0], "name,phone,category")
        self.assertEqual(lines[1], "Иван,111,работа")

    def test_export_count(self):
        add_contact(self.contacts, "Иван", "111", "работа")
        add_contact(self.contacts, "Пётр", "222", "друзья")
        self.assertEqual(export_csv(self.contacts, self.filename), 2)

    def test_export_empty_list(self):
        self.assertEqual(export_csv(self.contacts, self.filename), 0)


if __name__ == "__main__":
    unittest.main()
