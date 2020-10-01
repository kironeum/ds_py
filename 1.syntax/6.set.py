#   ***** МНОЖЕСТВО (SET) *****  
#   ОСОБЕННОСТИ:
#      - неупорядоченный тип коллекции, объекты не индексируются (неупорядоченная структура данных, неупорядоченный контейнер)
#      - при создании автоматически удаляет дублирующие объекты

# СОЗДАНИЕ НАПОЛНЕННОГО МНОЖЕСТВА

# 1 способ
mySet = {"a", "c", "b"}

# 2 способ

s = "hello"
l = [10,20,30,30]

mySet2 = set(l)

#       ***** ДОБАВЛЕНИЕ ЭЛЕМЕНТА

mySet.add(100)

#       ***** УДАЛЕНИЕ ЭЛЕМЕНТА 

# mySet.remove("d")

#       ***** РЕШЕНИЕ ПРОБЛЕМЫ

# 1 способ

# if "d" in mySet:
#     mySet.remove("d")
# else:
#     print("такого значения нет")

# 2 способ  -  метод, удаляющий элемент без ошибок

# mySet.discard("a")


#       ***** ОБЪЕДИНЕНИЕ МНОЖЕСТВ *****

users = {"John", "Tom", "Andrey"}

newUsers = {"John", "Kate", "Bob"}

# users2 = users.union(newUsers)   #  - метод update нужен в случае если необходимо сохранить целевое множество
# короткий аналог union()
unionUsers = users + newUsers
# users.update(newUsers)   #  - метод update изменяет целевое множество 


#       ***** ПЕРЕСЕЧЕНИЕ ***** 

intersectUsers = users.intersection(newUsers)    # - метод intersection отображает повторяющиеся элементы у разных множеств (пример: анализ текста). 

# короткий аналог метода intersection()
intersectUsers = users & newUsers

#       ***** РАЗНОСТЬ *****

# differentUsers = users.difference(newUsers)

# sdUsers = users.symmetric_difference(newUsers)

# короткий аналог метода difference()
diffUsers = users - newUsers

print(diffUsers)
