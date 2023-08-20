"""Задача: 
реализуйте класс Student и класс Aspirant, аспирант отличается
 от студента наличием некой научной работы.
Класс Student содержит переменные: String firstName, lastName, 
group. А также, double averageMark, содержащую среднюю оценку.
Создать метод getScholarship() для класса Student, который 
возвращает сумму стипендии. Если средняя оценка студента равна 
5, то сумма 2000, иначе 1900. Переопределить этот метод в 
классе Aspirant.  Если средняя оценка аспиранта равна 5, то 
сумма 2500, иначе 2200.
Создать массив типа Student, содержащий объекты класса 
Student и Aspirant. Вызвать метод getScholarship() для каждого 
элемента массива.

Пишем логику решения задачи:
1. Создается класс Student с конструктором init, принимающим 
параметры firstName, lastName, group и averageMark. В 
конструкторе происходит инициализация атрибутов объекта 
(self.firstName, self.lastName, self.group, self.averageMark) 
значениями, переданными в параметры конструктора.

2. В классе Student определен метод getScholarship. 
Метод проверяет значение атрибута averageMark объекта. Если 
значение равно 5, то метод возвращает значение 2000, иначе 
возвращает значение 1900.

3. Создается класс Aspirant, наследуемый от класса Student. 
В конструкторе init класса Aspirant, кроме параметров, 
принимаемых конструктором класса Student, добавляется новый 
параметр scientificWork. С помощью вызова 
super().init(firstName, lastName, group, averageMark) 
вызывается конструктор родительского класса для инициализации 
наследованных атрибутов.

4. В классе Aspirant также определен метод getScholarship. 
Метод также проверяет значение атрибута averageMark объекта. 
Если значение равно 5, то метод возвращает значение 2500, 
иначе возвращает значение 2200.

5. Создается массив students, содержащий объекты классов 
Student и Aspirant. В массиве создаются объекты с помощью 
вызова конструкторов классов с передачей соответствующих 
значений параметров.

6. Для каждого элемента массива students вызывается 
метод getScholarship(). Выводится строка, содержащая значения 
атрибутов firstName, lastName объекта и результат вызова 
метода getScholarship(), указывающая, является ли студент 
аспирантом или студентом обычного курса."""

class Student:
    def init(self, firstName, lastName, group, averageMark):
        self.firstName = firstName
        self.lastName = lastName
        self.group = group
        self.averageMark = averageMark
        
    def getScholarship(self):
        if self.averageMark == 5:
            return 2000
        else:
            return 1900

class Aspirant(Student):
    def init(self, firstName, lastName, group, averageMark, scientificWork):
        super().init(firstName, lastName, group, averageMark)
        self.scientificWork = scientificWork
    
    def getScholarship(self):
        if self.averageMark == 5:
            return 2500
        else:
            return 2200

# Создаем массив с объектами классов Student и Aspirant
students = [
    Student("John", "Doe", "Group 1", 4.8),
    Aspirant("Jane", "Smith", "Group 2", 5.0, "Scientific Work 1"),
    Student("Mike", "Johnson", "Group 1", 4.9),
    Aspirant("Emily", "Williams", "Group 3", 4.7, "Scientific Work 2")
]

# Вызываем метод getScholarship() для каждого элемента массива и выводим результат
for student in students:
    print(f"{student.firstName} {student.lastName}, Scholarship: {student.getScholarship()}")