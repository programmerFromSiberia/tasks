import sqlite3

# Подключаемся к базе данных
connection = sqlite3.connect('coffee_shop.db')

# Создаем курсор для выполнения SQL-запросов
cursor = connection.cursor()

# Создаем таблицу "КОФЕ"
cursor.execute('''CREATE TABLE IF NOT EXISTS coffee
                  (id INTEGER PRIMARY KEY,
                   name TEXT,
                   ml INTEGER)''')

# Создаем таблицу "БАРИСТА"
cursor.execute('''CREATE TABLE IF NOT EXISTS barista
                  (id INTEGER PRIMARY KEY,
                   name TEXT)''')

# Создаем таблицу "СМЕНА"
cursor.execute('''CREATE TABLE IF NOT EXISTS shift
                  (id INTEGER PRIMARY KEY,
                   date TEXT,
                   barista_id INTEGER)''')

# Вставляем данные в таблицу "КОФЕ"
coffee_data = [
    (1, 'Эспрессо', 50),
    (2, 'Капучино', 200),
    (3, 'Латте', 250),
]
cursor.executemany('INSERT INTO coffee VALUES (?,?,?)', coffee_data)

# Вставляем данные в таблицу "БАРИСТА"
barista_data = [
    (1, 'Иванов'),
    (2, 'Петров'),
    (3, 'Сидоров'),
]
cursor.executemany('INSERT INTO barista VALUES (?,?)', barista_data)

# Вставляем данные в таблицу "СМЕНА"
shift_data = [
    (1, '10.09.2022', 1),
    (2, '10.09.2022', 2),
]
cursor.executemany('INSERT INTO shift VALUES (?,?,?)', shift_data)

# Какой бариста на смене
shift_date = '10.09.2022'
cursor.execute('''SELECT barista.name FROM barista
                  INNER JOIN shift ON barista.id = shift.barista_id
                  WHERE shift.date = ?''', (shift_date,))
barista_on_shift = cursor.fetchone()

# Какие кофе продали на смене
cursor.execute('''SELECT coffee.name FROM coffee
                  INNER JOIN shift ON coffee.id = shift.coffee_id
                  WHERE shift.date = ?''', (shift_date,))
sold_coffees = cursor.fetchall()

# Какой бариста продал кофе "Капучино 200 мл" на смене "10.09.2022"
coffee_name = 'Капучино'
coffee_ml = 200

cursor.execute('''SELECT barista.name FROM barista
                  INNER JOIN shift ON barista.id = shift.barista_id
                  INNER JOIN coffee ON coffee.id = shift.coffee_id
                  WHERE shift.date = ? AND coffee.name = ? AND coffee.ml = ?''',
               (shift_date, coffee_name, coffee_ml))
barista_selling_coffee = cursor.fetchone()

# Закрываем соединение с базой данных
connection.close()