#                   ***** Генератор паролей ****

import hashlib
from tkinter import Tk, StringVar, Label, Entry, Button

def hashing():
    """
    Функция шифрования
    """
    # 1. строка пароли
    origin_str = pwd.get()

    # 2. кодирование
    byte_str = origin_str.encode()

    # 3. шифрование
    hash_str = hashlib.sha256(byte_str)

    # 4. преобразование в строку hex-числа (шестнадцатиричного числа) 
    hex_str = hash_str.hexdigest()[:10]

    # 5. передаем в переменную pwd_hash
    pwd_hash.set(hex_str)

    # 6. запись в файл
    with open("pwd.txt", "w") as f:
        f.write(f"{pwd.get()} : {pwd_hash.get()}")


# объект окна
window = Tk()
# заголовок окна
window.title("Password Generator")

# переменные с объектами класса StringVar
pwd = StringVar()
pwd_hash = StringVar()

# Текстовая метка созданная компонентом (виджетом, элементом) Label
# Label позволяет выводить статический (неизменяемый) текст без возможности редактирования
label = Label(text="Пароль: ")
# Позиционирование методом grid(сетка)
label.grid(row=0, column=0, padx=5, pady=5)

# поле ввода/ввывода текста осуществляется виджетом Entry
Entry(textvariable=pwd).grid(row=0, column=1, padx=5, pady=5)

# создание кнопки
Button(text="Click me", command=hashing).grid(row=1, column=0, padx=5, pady=5)

# Вывод текста
Entry(textvariable=pwd_hash).grid(row=1, column=1, padx=5, pady=5)

# запуск основного цикла
window.mainloop()