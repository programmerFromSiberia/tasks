import random


class Student:
    def __init__(self, name='', group='', gpa=0):
        self.__id = random.randint(1, 100)
        self.__name = name
        self.__group = group
        self.__gpa = gpa

    def show(self):
        print(self.__name, self.__group, self.__gpa, end=' | ')

    @property
    def getgroup(self):
        return self.__group

    @property
    def getgpa(self):
        return self.__gpa

    def setGroup(self, group):
        if isinstance(group, str):
            self.__group = group
        else:
            print("Attribute must be a string")


# Создаем список студентов
students = [
    Student("John", "Group A", 3.5),
    Student("Alice", "Group B", 3.8),
    Student("Bob", "Group A", 3.2),
    Student("Eve", "Group C", 4.0)
]

# Сортируем список по убыванию атрибута id
students.sort(key=lambda student: student._Student__id, reverse=True)

# Выводим отсортированный список студентов
for student in students:
    student.show()