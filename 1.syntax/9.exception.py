# ***** ИСКЛЮЧЕНИЯ (исключительные события, ситуации, ошибки, exception) ***** 

# Пример ошибки "деление на ноль" (zero division)

a = 100
b = 0

# без обработки потенциального исключения
#c = a/b

# обработка исключения

''' try:          < - попытка
    print(0)
except print(0):
    pass  ''' 

try: 
    c = a / b
except:
    # код который работает при обнаружении исключительного события
    #print("Что-то пошло не так :P")
    c = 0

#print("Результат: ", c)



# try:
#     val_1 = int(input("Введите число: "))

#     result = 50 / val_1

# # обработка конкретного исключения
# except ValueError as error:
#     print(f"Возникло исключение: тип - {ValueError} : {error}")
#     print("Нужно ввести число")

# except ZeroDivisionError:
#     print("Попытка деления на ноль")


# # обработка общего исключения
# except Exception as error:
#     print(error)

# конструкция "try-except-else"

#      вариант без использования else
#      потенциально аварийный участок кода
# try:
#     a = int(input("Введите число "))
#     c = 100 / a
# except ZeroDivisionError:
#     c = 0

# кусок кода который должен работать в любом случае
# print("Result: ", c)

# вариант с использованием else
# try:
#     a = int(input("Введите число "))
#     c = 100 / a
# except ZeroDivisionError:
#     c = 0
# # блок else срабатывает если НЕ отлавливаются исключения
# else:
#     print("Result: ", c)


# вариант с использованием finally
# try:
#     a = int(input("Введите число "))
#     c = 100 / a
#     print("Полет нормальный")
# except ZeroDivisionError:
#     c = 0
#     print("Деление на ноль")

# # finally срабатывает в любом случае, даже если программа завершается аварийно
# finally:
#     # внутри должны быть критически важные действия
#     # например, закрытие файла или сессии базы данных и т.д.
#     print("Сработала finally")

# конструкция "try-except-else-finally"

# try:
#     a = int(input("Введите число "))
#     c = 100 / a
#     print("Полет нормальный")
# except ZeroDivisionError:
#     c = 0
#     print("Деление на ноль")
# except Exception as err:
#     print("Исключение")
    
# # else сработает если нет исключения
# else:  
#     c += 1
#     print("Result: ", c)

# # finally срабатывает в любом случае, даже если программа завершается аварийно
# finally:
#     # внутри должны быть критически важные действия
#     # например, закрытие файла или сессии базы данных и т.д.
#     print("Сработала finally")
# print("Код после обработки исключений")


# КАСТОМИЗИРОВАННЫЕ ИСКЛЮЧЕНИЯ
# try:
#     a = int(input("Введите число: "))
#     if a == 0:
#         raise Exception("Деление на ноль")
#     c = 100 / a
#     print("Полет нормальный")
# except Exception as e:
#     print(e)
    

# ***** ПРИМЕР ПРИБЛИЖЕННЫЙ К РЕАЛЬНОСТИ *****

while True:
    # ввод данных
    try: 
        a = int(input("Введите число: "))
        c = 100 / a
    except ValueError:
        print("Нужно ввести число")
        continue
    except ZeroDivisionError:
        print("Вы попытались поделить на ноль")
        continue
    print("Result: ", c)   
    break 
    # обработка

# ДОМАШКА! ! ! ПРИМЕНИТЬ ЭКСПЕШНЫ И ФУНКЦИИ (ОБРАБОТКА ДАННЫХ - ОТДЕЛЬНАЯ Ф-Я, ВЫЧИСЛЕНИЯ - ОТДЕЛЬНАЯ Ф-Я) К КАЛЬКУЛЯТОРУ
