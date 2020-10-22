# ***** Основы объектно-ориентированного программирования (ООП) *****

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

# *** Принцип наследования - принцип ООП *****

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

# вызов метода общего для всех (метод наследуется от родительского класса)
oliver.info()
katrin.info()
john.info()

# вызов метода, которым обладают все классы кроме Simple_Human
john.skill()
katrin.skill()

# вызов метода, которым обладает только класс Medic
katrin.therapy(john)

try:
    oliver.skill()
except AttributeError:
    print("У него нет метода skill")
    oliver.info()
