import sqlite3 as sl
from easygui import *

conn = sl.connect('telbook.db')

cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS contacts
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            mail TEXT,
            birthday TEXT,
            tNumber1 TEXT,
            tNumber2 TEXT)
            ''')

def add_values():
    name=enterbox("Введите имя контакта:")
    mail=enterbox("Введите электронную почту:")
    birthday=enterbox("Введите день рождения:")
    tNumber1=enterbox("Введите телефонный номер:")
    tNumber2=enterbox("Введите второй телефонный номер:")
    cur.execute("INSERT INTO contacts (name, mail, birthday, tNumber1, tNumber2) VALUES (?, ?, ?, ?, ?)", (name, mail, birthday, tNumber1, tNumber2))
    conn.commit()
    msgbox("Контакт успешно добавлен!")

def select_all():
    cur.execute('SELECT * FROM contacts')
    output=''
    for row in cur.fetchall():
        output+=str(row)
    msgbox(output, 'Существующие контакты')

def search_contact():
    keyword=enterbox("Введите искомое значение:")
    cur.execute('SELECT * FROM contacts WHERE name LIKE ? OR mail LIKE ? OR birthday LIKE ? OR tNumber1 LIKE ? OR tNumber2 LIKE ?' , ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%'))
    output=''
    for row in cur.fetchall():
        output+=str(row)
    msgbox(output, 'Найденные контакты')


def main():
        while True:
            choice = choicebox("Выберите действие", "Главная форма", ['Просмотр контактов', 'Добавить контакт', 'Поиск', 'Выход'])
            if choice == "Просмотр контактов":
                select_all()
            if choice == "Добавить контакт":
                add_values()
            if choice == "Поиск":
                search_contact()    
            if choice == "Выход":
                break
        conn.close()

if __name__=='__main__':
     main()
