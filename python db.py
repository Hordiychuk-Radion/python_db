import sqlite3


conn = sqlite3.connect("python_users.db")  


c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    phone TEXT
);""")

print("Введіть свій вік:")
age = input()


try:
    age = int(age)
except ValueError:
    print("Вік повинен бути цілим числом.")
    exit()

if age < 18 or age > 100:
    print("Вік повинен бути від 18 до 100 років.")
    exit()


print("Введіть своє ім'я:")
name = input()


print("Введіть свій номер телефону:")
phone = input()


if len(phone) != 10:
    print("Номер телефону повинен містити рівно 10 цифр.")
    exit()


c.execute("INSERT INTO users (name, age, phone) VALUES (?, ?, ?)", (name, age, phone))


conn.commit()


conn.close()