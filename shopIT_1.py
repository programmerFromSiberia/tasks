import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('sales.db')
c = conn.cursor()

# Создаем таблицу для продавцов
c.execute('''CREATE TABLE IF NOT EXISTS Salespeople
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             sname TEXT,
             city TEXT,
             comm FLOAT)''')

# Создаем таблицу для заказчиков
c.execute('''CREATE TABLE IF NOT EXISTS Customers
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             cname TEXT,
             city TEXT,
             rating INTEGER,
             id_sp INTEGER,
             FOREIGN KEY (id_sp) REFERENCES Salespeople(id))''')

# Функция для регистрации нового продавца
def register_salesperson(sname, city, comm):
    c.execute('''INSERT INTO Salespeople (sname, city, comm)
                 VALUES (?, ?, ?)''', (sname, city, comm))
    conn.commit()

# Функция для регистрации нового заказчика
def register_customer(cname, city, rating, id_sp):
    c.execute('''INSERT INTO Customers (cname, city, rating, id_sp)
                 VALUES (?, ?, ?, ?)''', (cname, city, rating, id_sp))
    conn.commit()

# Функция для редактирования записи о продавце
def edit_salesperson(id, sname, city, comm):
    c.execute('''UPDATE Salespeople
                 SET sname = ?, city = ?, comm = ?
                 WHERE id = ?''', (sname, city, comm, id))
    conn.commit()

# Функция для редактирования записи о заказчике
def edit_customer(id, cname, city, rating, id_sp):
    c.execute('''UPDATE Customers
                 SET cname = ?, city = ?, rating = ?, id_sp = ?
                 WHERE id = ?''', (cname, city, rating, id_sp, id))
    conn.commit()

# Функция для удаления записи о продавце
def delete_salesperson(id):
    c.execute('DELETE FROM Salespeople WHERE id = ?', (id,))
    conn.commit()

# Функция для удаления записи о заказчике
def delete_customer(id):
    c.execute('DELETE FROM Customers WHERE id = ?', (id,))
    conn.commit()

# Пример использования функций
register_salesperson('John Doe', 'New York', 0.05)

register_customer('Jane Smith', 'London', 4, 1)

edit_salesperson(1, 'John Smith', 'Chicago', 0.08)

edit_customer(1, 'Jane Doe', 'Paris', 5, 2)

delete_salesperson(1)

delete_customer(1)