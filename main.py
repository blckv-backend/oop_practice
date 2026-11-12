#Классы и обекты
#Классы- как чертеж ил инструкция дома,а объект который создается из этого чертежа
#Атрибутами считается свойства объекта,а методы это действия этого объекта
#Git это система контроля версий, или простыми словами она нужна для сохранения изменений моего кода
#Github это сайт где можно увидеть сохранеия и делится своим кодом
#__init__ я не понял
#self указывает на обьект по моим понятиям
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'My name is {self.name}, and I am {self.age} years old.')


student1 = Student("Alex", 20)
student1.introduce()

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def persons(self):
        print(f'My name is {self.name}, I am {self.age} years old.And i live in {self.city}.')

person1 = Person("Alex", 20, "London")
person2 = Person("Aidin", 17, "Bishkek")
person1.persons()
person2.persons()


class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def info(self):
        print(f"My phone is {self.brand} {self.model} He's price is {self.price}.")
    def discount(self):
        self.price = self.price * 0.90

phone1 = Phone("iphone", "17 pro max", 10000)
phone2 = Phone("iphone", "18 pro max", 100000)
phone1.discount()
phone1.info()
phone2.discount()
phone2.info()

class FootballPlayer():
    def __init__(self,name, age, position, goals):
        self.name = name
        self.age = age
        self.position = position
        self.goals = goals
    def show_info(self):
        print(f'My name is {self.name}, I am {self.age} years old.My position is {self.position}.And I score {self.goals} goals.')
    def score_goals(self):
        self.goals += 1
    def celebrate(self):
        print("SIUUUUUU")

player1 = FootballPlayer("Leonel Messi", 38, "Striker", 100)
player2 = FootballPlayer("Cristiano Ronaldo", 42, "Striker", 1000)
player1.score_goals()
player2.score_goals()
player1.show_info()
player2.show_info()
player1.celebrate()
player2.celebrate()

# I am learning Git and GitHubпш