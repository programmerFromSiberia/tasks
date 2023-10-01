import sqlite3

# Создание и подключение к базе данных
conn = sqlite3.connect('database_players.db')
cursor = conn.cursor()

# Создание таблицы "players"
cursor.execute('''CREATE TABLE players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    best_score INTEGER
)''')

# Создание таблицы "games"
cursor.execute('''CREATE TABLE games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    score INTEGER,
    id_player INTEGER
)''')

# Запросы на вставку данных
players_data = [
    ('Миша', 200),
    ('Ваня', 154),
    ('Дима', 178),
    ('Коля', 210)
]

games_data = [
    ('Миша', 110, 1),
    ('Миша', 200, 1),
    ('Дима', 178, None),
    ('Коля', 10, None),
    ('Коля', 30, None)
]

# Вставка данных в таблицу "players"
cursor.executemany('INSERT INTO players (name, best_score) VALUES (?, ?)', players_data)

# Вставка данных в таблицу "games"
cursor.executemany('INSERT INTO games (name, score, id_player) VALUES (?, ?, ?)', games_data)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()