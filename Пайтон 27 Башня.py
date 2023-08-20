"""
представим себе игру стратегию. Напишите в комментариях логику,
которую вы видете по взаимодействию с этими башнями
Создать класс башня (есть броня и здоровье, а также регуляторы 
увеличения и уменьшения здоровья и брони). 
Создать класс стрелковая башня (умеет стрелять и все то, 
что и родитель)

"""
class Tower:
    def __init__(self, health, armor):
        self.health = health
        self.armor = armor
    
    def increase_health(self, amount):
        self.health += amount
    
    def decrease_health(self, amount):
        self.health -= amount
    
    def increase_armor(self, amount):
        self.armor += amount
    
    def decrease_armor(self, amount):
        self.armor -= amount


class ArcherTower(Tower):
    def __init__(self, health, armor):
        super().__init__(health, armor)
    
    def shoot(self):
        # Логика стрельбы стрелковой башни
        pass

#************************************************#

# можно решить эту задачу более подробно, пишем логику игры:
"""
1. Создать класс "Башня" со следующими атрибутами:
   - Здоровье (health)
   - Броня (armor)

2. Добавить методы класса "Башня":
   - Метод для увеличения здоровья (increase_health), принимающий значение на которое нужно увеличить здоровье башни
   - Метод для уменьшения здоровья (decrease_health), принимающий значение на которое нужно уменьшить здоровье башни
   - Метод для увеличения брони (increase_armor), принимающий значение на которое нужно увеличить броню башни
   - Метод для уменьшения брони (decrease_armor), принимающий значение на которое нужно уменьшить броню башни

3. Создать класс "Стрелковая башня", который наследуется от класса "Башня" и добавляет следующие методы:
   - Метод для стрельбы (shoot), который будет выполнять определенные действия при стрельбе

4. Создать экземпляры классов "Башня" и "Стрелковая башня" с заданными значениями здоровья и брони.

5. Вызвать методы увеличения/уменьшения здоровья и брони для каждой из башен, передавая им соответствующие значения.

6. Вызвать метод "стрельба" для стрелковой башни, чтобы выполнить нужные действия при стрельбе.

7. Необходимо также предусмотреть обработку возможных исключительных ситуаций при увеличении/уменьшении здоровья и брони.
"""
class Tower:
    def __init__(self, health, armor):
        self.health = health
        self.armor = armor

    def increase_health(self, value):
        try:
            if value >= 0:
                self.health += value
            else:
                raise ValueError("Value must be positive")
        except ValueError as e:
            print(e)

    def decrease_health(self, value):
        try:
            if value >= 0:
                self.health -= value
            else:
                raise ValueError("Value must be positive")
        except ValueError as e:
            print(e)

    def increase_armor(self, value):
        try:
            if value >= 0:
                self.armor += value
            else:
                raise ValueError("Value must be positive")
        except ValueError as e:
            print(e)

    def decrease_armor(self, value):
        try:
            if value >= 0:
                self.armor -= value
            else:
                raise ValueError("Value must be positive")
        except ValueError as e:
            print(e)


class ArcherTower(Tower):
    def shoot(self):
        print("Performing shooting action")


# Создание экземпляров классов
tower = Tower(100, 10)
archer_tower = ArcherTower(150, 20)

# Изменение здоровья и брони башни
tower.increase_health(50)
tower.decrease_health(20)
tower.increase_armor(5)
tower.decrease_armor(2)

archer_tower.increase_health(30)
archer_tower.decrease_health(10)
archer_tower.increase_armor(3)
archer_tower.decrease_armor(1)

# Выполнение стрельбы стрелковой башни
archer_tower.shoot()








