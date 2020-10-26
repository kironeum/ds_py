#                                                           ***** Основы объектно-ориентированного программирования (ООП) *****

# Объекты обладают свойствами и методами (атрибуты)
# Каждый объект должен принадлежать к определенному классу (тип)     
#  "Класс" - "чертеж" объекта
# Конкретный реализованный на базе класса объект называется экземпляром класса


# создание класса. Название принято писать с заглавной буквы.

class Cat:
    # метод-конструктор  (self - спец аргумент)
    def __init__(self):
        # свойства (атрибуты, поля)
        self.name = None

    # метод- функция, принадлежащая классу 
    def mur(self):
        return self.name
    
# создание объекта на базе класса Cat ( т.е. экземпляра (instance) класса)

cat_1 = Cat()

# чтение свойства (атрибута)
var = cat_1.name
# print("Значение var ДО изменения ", var)

# Запись в свойство 

cat_1.name = 100
# print(cat_1.name)
# print("Значение var ПОСЛЕ изменения ", var)

# var = 10
# print(cat_1.name)


# вызов метода экземпляра 
res = cat_1.mur()
#print("Результат: ", res)

# каждый объект (экземпляр класса) независим
# создание второго экземпляра класса Cat()
cat_2 = Cat()
cat_2.name = 200 

# вызов метода обеих объектов
# print(cat_1.mur())
# print(cat_2.mur())

#                                                                    *** Принцип наследования - принцип ООП *****

# создание родительского (предкового) класса 

class Animal:
    def __init__(self):
        self.num_legs = 0  # (слева атрибут справа аргумент)
    
# создание дочерних классов

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    
    def info(self):
        print(f"My name is {self.name}. Legs: {self.num_legs} ")

class Insect(Animal):
    def __init__(self, name):
        self.name = name 
    
    def info(self):
        print(f"My name is {self.name}. Legs: {self.num_legs} ")

# Создание экземпляров дочерних классов
dog_1 = Dog("Barry")
dog_1.num_legs = 4

bug = Insect("Ant")
bug.num_legs = 6

#вызов метода дочерних классов
# dog_1.info()
# bug.info()


class Human(object):
    """
    docstring
    """
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    
    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}")

class Pilot(Human):
    def skill(self):
        print("я умею летать")

class Medic(Human):
    def skill(self):        
        print("я умею лечить")
    
    def therapy(self, obj):
        print(f"Я вылечил {obj.name}")

class Simple_Human(Human):
    pass

john = Pilot("John", 45, 82.4)
katrin = Medic("Katrin", 35, 67.5)
oliver = Simple_Human("Olver", 5, 23.1)

# # вызов метода общего для всех (метод наследуется от родительского класса)
# oliver.info()
# katrin.info()
# john.info()

# # вызов метода, которым обладают все классы кроме Simple_Human
# john.skill()
# katrin.skill()

# # вызов метода, которым обладает только класс Medic
# katrin.therapy(john)

# try:
#     oliver.skill()
# except AttributeError:
#     print("У него нет метода skill")
#     oliver.info()



#                                                   ***** Полиморфизм ***** 
# поли + морф = разные формы чего-то одного

# Методы у разных классов переопределяются т.е методы имеют одинаковое название, но могут иметь различные поведения

# Родительский класс
class A:
    def func(self, arg):
        res = arg * 2
        print(f"Данные класса A: {res}")

# дочерний класс у которого метод переопределен

class A_1:
    def func(self, arg):
        res = arg ** 3
        print(f"Данные класса A_1: {res}")

class A_3:
    def func(self, arg):
        res = arg + " плюс строка"
        print(f"Данные класса A_1: {res}")
# экземпляры

# a = A()
# a_1 = A_1()
# a_3 = A_3()

# вызов методов с одинаковым названием (func), но с разным поведением
# a.func(10)
# a_1.func(10)
# a_3.func("строка")


#           Второй вид полиморфизма - применение "магических" методов (методы перегрузки операторов)
# методы, который делает из экземпляра класса функцию

class Sum(object):
    def __init__(self, param):
        self.coeff = param
    def __call__(self, a, b):
        res = (a + b) * self.coeff
        print(f"Результат: {res}")
    
    def __str__(self):
        return f"Sum {self.coeff}"

# s_1 = Sum(0.5)
# s_2 = Sum(3.14)

# объект ведет себя как функция
# s_1(10, 20)
# s_2(10, 20)

# объект при передаче в функцию print возвращает строку
# print(s_1)


#                                                               ***** Инкапсуляция ***** - скрытие атрибутов и методов (обычно применяемых только внутри класса)

#                инкапсуляция не строгая
class B:
    def __init__(self, arg):
        self._attr = arg
    
    def _method(self):
        print("hello!")

b = B(100)

# print(b._attr)
# b._method()

#                инкапсуляция строга

class C:
    def __init__(self, arg):
        self.__attr = arg
    
    def method_2(self):
        return self.__attr
    
    def __method(self):
        print("hello!")

c = C(200)
# c._C__method()
# print(c.method_2())



#                                                                ***** Композиция (агрегация)***** - использование экземпляров одного класса внутри другого 

class D:
    def __call__(self, a):
        return a ** 2

class E:
    def m(self, b):
        d = D()   # создается объект класса D
        res = b + 2
        return d(res) # используется объект класса D в качестве функции

e = E()
res = e.m(10)
# print(res)

#           статический метод, метод класса

class Person:
    # статическая переменная
    counter = 0
    def __init__(self, name, age):
        self.__n = name
        self.__a = age
        Person.counter += 1
        self.id = Person.counter

    # метод экземпляра
    def info(self):
        print(f"Идентификатор: {self.id}, Имя: {self.__n}, Возраст: {self.__a}")

    # метод класса
    @classmethod
    def count_control(cls):
        cls.counter += 1

    # статический метод
    @staticmethod
    def method(x, y):
        print(f"Res: {x + y}")

john = Person("John", 20)
john.info()
# john.count_control()


bob = Person("Bob", 30)
bob.info()
print(bob.counter)

bob.method(10, 20)
Person.method(10, 20)