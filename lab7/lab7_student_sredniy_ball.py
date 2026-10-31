# Лабораторная работа №7, вариант 2
# Класс Student: ФИО, группа, оценки; средний балл, долги

class Student:
    def __init__(self, name, group, grades):
        self._name = name
        self._group = group
        self._grades = list(grades)

    # свойства для доступа к приватным полям
    @property
    def name(self):
        return self._name

    @property
    def group(self):
        return self._group

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, value):
        self._grades = list(value)

    # средний балл по всем оценкам
    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    # долги — количество неудовлетворительных оценок
    def debts(self):
        return sum(1 for g in self.grades if g <= 2)

    # строка с полной информацией о студенте
    def info(self):
        return "{} (гр. {}) средний балл: {:.2f}, долгов: {}".format(
            self.name, self.group, self.average(), self.debts())


def main():
    students = [
        Student("Иванов Иван Иванович", "ИЭК-21", [5, 4, 5, 3, 4]),
        Student("Петрова Анна Сергеевна", "ИЭК-21", [4, 4, 5, 5, 5]),
        Student("Сидоров Пётр Алексеевич", "ИЭК-22", [2, 3, 2, 4, 3]),
        Student("Кузнецова Мария Игоревна", "ИЭК-22", [5, 5, 5, 4, 5]),
    ]

    # вывод всех студентов
    print("Список студентов:")
    for s in students:
        print(" ", s.info())

    # студенты с долгами
    print("\nСтуденты с долгами:")
    found = False
    for s in students:
        if s.debts() > 0:
            print(" ", s.name, "-", s.debts(), "долг(ов)")
            found = True
    if not found:
        print("  нет")

    # поиск лучшего среднего балла
    best = students[0]
    for s in students:
        if s.average() > best.average():
            best = s
    print("\nЛучший средний балл у:", best.name, "-", round(best.average(), 2))

    # изменение оценок через свойство grades
    students[2].grades = [3, 3, 4, 4, 3]
    print("\nПосле пересдачи у", students[2].name, ":")
    print(" ", students[2].info())


if __name__ == "__main__":
    main()
