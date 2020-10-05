#       ***** ЦИКЛЫ (ОПЕРАТОРЫ ЦИКЛОВ) *****

# Оператор цикла While

number = 0

# while number <= 10:
#     print(number)
#     #number += 1  # аналог: number = number + 1


# ПРЕРЫВАНИЕ ЦИКЛА ПО ДОПОЛНИТЕЛЬНОМУ УСЛОВИЮ (BREAK)

# while number < 10:
#     if number == 5: # если значение number станет равной 5,
#         break       # то вызываем инструкцию breakm которая прерывает цикл
#     print(number)
#     number += 1
    

# ПРИМЕР ПРЕРЫВАНИЯ БЕСКОНЕЧНОГО ЦИКЛА (TRUE) С ИСПОЛЬЗОВАНИЕМ BREAK 

# while True:
#     s = input("Введите команду: ")
#     print(f"Вы ввели команду: {s}") 
#     if s.lower() == "стоп":
#         break

# ПРОПУСК КУСКА КОДА ИЗ ТЕЛА ЦИКЛА

# while True:
#     s = input("Введите слово 'YES': ")
#     if s != "YES": 
#         print("Вы не ввели требуемое слово :P ")
#         continue # если вызывается инструкция continue, то цикл возвращается в начало

#     print(f"Вы ввели команду: {s}") 
#     break

# ОПЕРАТОР ЦИКЛА FOR 

# 1. (for) читает элемент по порядку
# 2. присваивает значение элемента в свою переменную
# 3. выполняет блок кода своего тела

# for n in [1,2,3,4,5,6]:  # для (каждой n) каждого объекта внутри переменной n из списка напечатать значение переменной n
#     print(n)


myTuple = (100, 200, 300)

# for n in myTuple[::-1]:
#     print(n)

# for n in myTuple[::-1]:
#     print(n)

# for n in myTuple:
#     if n == 200:
#         break # or continue
#     print(n)

for idx in range(5, 20, 2):
    res = idx + 1
    print(res)
