# print("hello world!")    ctrl + /   =  комментир выделением

# a = input("Введите число a: ")  # конструкция: создается переменная которой присваивается значение input, который ожидает ввода от пользователя, после ввода input выходные данные присваиваются переменной message 
# b = input("Введите число b: ")

# c = int(a) + int(b)

# print("Результат: ", c)

int_num = 777 # целочисленный тип данных

float_num = 3.14 # типа данных "числа с плавающей точкой"

string = "Буквы, слова" # строковой тип данных

boolean = True # False Булевы типы данных


# print(float_num, int_num, string, boolean)




# СПОСОБ ФОРМАТИРОВАНИЯ СТРОК f-string -----------------------

name = 'Alexey'
age = 31

s = f"Name: {name} \tAge: {age}"
#print(s)


# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ ------------------------

a = 10
b = 20

res_1 = a + b
res_2 = a - b
res_3 = a * b 
res_4 = a / b  # обычое деление
res_5 = a // b # целочисленное деление (удаляет дробную часть оставляя целую)
res_6 = a % b # деление по модулю (возвращает остаток от деления)
res_7 = a ** b # возведение в степень

#print(res_7)


# ЛОГИЧЕСКИЕ ОПЕРАЦИИ --------------------------
# (см Таблица логических операторов)

x = 3
y = 3

res_8 = x != y          # "=!" лог оператор НЕ РАВНО
res_9 = x == y          # "==" лог оператор РАВЕНСТВА
res_10 = x > y 
res_11 = x >= y 

z = True
k = False

res_12 = not z      # "not" логический оператор НЕ  
res_13 = z and k    # "and" логические оператор И (true если оба значения true)
res_14 = z or k     # "or" лог оператор ИЛИ (хотя бы одно значение true)  

print(res_14)



