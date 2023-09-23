import sqlite3

# Создание базы данных и установка соединения
conn = sqlite3.connect('shopIT.db')
cursor = conn.cursor()

# Создание таблицы "Компьютеры"
cursor.execute('''CREATE TABLE IF NOT EXISTS Компьютеры
                  (тип TEXT, бренд TEXT, стоимость REAL)''')

# Вставка данных в таблицу
cursor.execute("INSERT INTO Компьютеры VALUES ('ноутбук', 'HP', 35000)")
cursor.execute("INSERT INTO Компьютеры VALUES ('стационарный компьютер', 'HP', 50000)")
cursor.execute("INSERT INTO Компьютеры VALUES ('моноблок', 'Dell', 45000)")
cursor.execute("INSERT INTO Компьютеры VALUES ('ноутбук', 'Lenovo', 25000)")

# Выполнение запросов и вывод результатов
cursor.execute("SELECT * FROM Компьютеры WHERE бренд='HP'")
print("Все компьютеры бренда HP:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM Компьютеры WHERE стоимость > 40000")
print("Компьютеры стоимостью более 40000:")
for row in cursor.fetchall():
    print(row)

cursor.execute("SELECT * FROM Компьютеры WHERE тип='ноутбук' AND стоимость < 30000")
print("Компьютеры типа ноутбук и стоимостью менее 30000:")
for row in cursor.fetchall():
    print(row)

# Закрытие соединения с базой данных
conn.commit()
conn.close()