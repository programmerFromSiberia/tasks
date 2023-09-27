import sqlite3

# Создание базы данных
conn = sqlite3.connect('shopIT.db')
c = conn.cursor()

# Создание таблицы Salespeople
c.execute('''CREATE TABLE IF NOT EXISTS Salespeople
             (id INTEGER PRIMARY KEY,
              sname TEXT,
              city TEXT,
              comm REAL)''')

# Создание таблицы Customers
c.execute('''CREATE TABLE IF NOT EXISTS Customers
             (id INTEGER PRIMARY KEY,
              cname TEXT,
              city TEXT,
              rating INTEGER,
              id_sp INTEGER,
              FOREIGN KEY(id_sp) REFERENCES Salespeople(id))''')

# Вставка данных из файла Salespeople.txt
with open('F:\\Учеба\\ТОП Академия\\Домашние задания\\SQL\\ДЗ SQL\\SQL35\\Salespeople.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(',')
        c.execute('''INSERT INTO Salespeople (sname, city, comm)
                     VALUES (?, ?, ?)''', (data[0], data[1], float(data[2])))

# Вставка данных из файла Customers.txt
with open('F:\\Учеба\\ТОП Академия\\Домашние задания\\SQL\\ДЗ SQL\\SQL35\\Customers.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        data = line.strip().split(',')
        c.execute('''INSERT INTO Customers (cname, city, rating, id_sp)
                     VALUES (?, ?, ?, ?)''', (data[0], data[1], int(data[2]), int(data[3])))

conn.commit()
conn.close()
