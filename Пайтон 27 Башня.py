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