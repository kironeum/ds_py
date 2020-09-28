# *********    СПИСКИ (lists)  **********

# СОЗДАНИЕ ПУСТОГО СПИСКА 

myList = []
myList2 = list() 

myList2.append(100)
myList2.append(100)
myList2.append(777)

myList2.append("hello")

myList2.append([1,2,3])

# ОБРАЩЕНИЕ К ЭЛЕМЕНТАМ СПИСКА -----------------------------

el = myList2[2]   # извлечение значения по индексу


del myList2[1]  # удаление элемента по индексу

myList2[1] = 200 # замена значения по индексу

# СОЗДАНИЕ ЗАПОЛНЕННОГО СПИСКА -----------------------------

myList = [10, 20, 30, 40, "A", "B"]

s = "привет, Мир!"

myList3 = list(s)

# ФУНКЦИЯ RANGE()

# range(end), создается набор чисел от 0 дло числа end (не включительно)
# range(start, end), создается набор чисел от start дло числа end (не включительно)
# range(start, end, step), создается набор чисел от start дло числа end (не включительно) с шагом step

numbers = list(range(5))
numbers = list(range(1,5))
numbers = list(range(1, 10, 2))
numbers = list(range(10, 1, -1))


# ****** МЕТОДЫ СПИСКА ********

a = [10, 20, 30, 40, 50]

# append - метод добавления элемента

#  объект.метод()

a.append(100)

# insert - добавляет элемент в список по индексу

a.insert(0, 7)

# remove - удаляет элемент по значению

a.remove(30)

# clear - очистка списка

#a.clear() 

# sort - сортировка списка

b = [8,2,1,7,3,2,8,4,1]
b.sort(reverse=True)

# reverse - поворот списка 

c = [1,2,3]
c.reverse()

print(c)
