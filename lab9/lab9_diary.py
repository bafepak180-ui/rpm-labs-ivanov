# Лабораторная работа №9, вариант 2
# Дневник (diary.txt): добавление записей, вывод всех, поиск по дате

FILE_NAME = "diary.txt"


class BadLineError(Exception):
    """Своя ошибка: строка в файле имеет неверный формат."""
    pass


def read_entries():
    """Читает записи из файла, возвращает список пар (дата, текст)."""
    entries = []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|", 1)
            if len(parts) != 2:
                raise BadLineError("битая строка в файле: " + line)
            entries.append((parts[0], parts[1]))
    return entries


def add_entry():
    """Добавляет одну запись в конец файла."""
    date = input("Дата (дд.мм.гггг): ").strip()
    text = input("Текст записи: ").strip()
    if not date or not text:
        raise ValueError("дата и текст не должны быть пустыми")
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(date + "|" + text + "\n")
    print("Запись добавлена.")


# если файла нет — создаём дневник с парой демо-записей
try:
    with open(FILE_NAME, "r", encoding="utf-8"):
        pass
except FileNotFoundError:
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        f.write("01.03.2024|Первая запись в дневнике\n")
        f.write("15.03.2024|Сдал лабораторную по файлам\n")
    print("Создан новый дневник с демо-записями.")

# главное меню
while True:
    print("\n1 — добавить запись, 2 — показать все, 3 — поиск по дате, 0 — выход")
    try:
        choice = input("Выбор: ").strip()
    except EOFError:
        break
    try:
        if choice == "1":
            add_entry()
        elif choice == "2":
            for date, text in read_entries():
                print(date, "-", text)
        elif choice == "3":
            date = input("Дата для поиска: ").strip()
            found = [t for d, t in read_entries() if d == date]
            if found:
                for t in found:
                    print(date, "-", t)
            else:
                print("Записей на эту дату нет.")
        elif choice == "0":
            print("Пока.")
            break
        else:
            print("Нет такого пункта меню.")
    except FileNotFoundError:
        print("Файл дневника не найден.")
    except BadLineError as e:
        print("Ошибка данных в файле:", e)
    except ValueError as e:
        print("Ошибка ввода:", e)
    except OSError as e:
        print("Ошибка работы с файлом:", e)
