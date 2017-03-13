# class Person(object):
#     # свойства класса
#     # firstname = 'Иван'
#     # lastname = 'Иванов'
#     # Статические свойства - не привязаны к объекту, а к классу
#     foot_amount = 2
#
#     # конструктор
#     def __init__(self, firstname, lastname):
#         # инициализация свойства значением аргумента
#         self.firstname = firstname
#         self.lastname = lastname
#
#     # метод - функция, объявленная в контексте класса
#     def say_name(self):
#         print('Я {} {}, привет!'.format(self.firstname, self.lastname))
#         print('У меня {} ножек!'.format(self.foot_amount))
#
#     @staticmethod
#     # статический метод, можно вызывать несоздавая объект
#     def take_lightsabre():
#         return 'lightsabre'
#
#     @classmethod
#     def correct(cls, person):
#         if person.foot_amount > cls.foot_amount:
#             person.foot_amount = 2
#
#
# class Developer(Person):
#     def __init__(self, firstname, lastname, skills):
#         # вызов родительского метода
#         super().__init__(firstname, lastname)
#         self.skills = skills
#
#     def say_name(self):
#         super().say_name()
#         print('Я умею {}'.format(self.skills))
#
# dev1 = Developer('Linus', 'Torvalds', ['C++', 'C'])
# dev1.say_name()
# # объект:
# person1 = Person('Иван', 'Иванов')
# person2 = Person('Сидр', 'Сидоров')
# person3 = person1
#
# person3.firstname = 'Петров'
# print(person1)
# print(person2)
# print(person3)
#
# person2.foot_amount = 4
# person2.age = 1
#
# Person.correct(person2)
# print(person2.foot_amount)
#
# person1.say_name()
# person2.say_name()
# person3.say_name()
#
# Person.take_lightsabre()
#
# print(Person.foot_amount)
# print(person2.age)


class Person(object):
    def __init__(self, firstname, lastname, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone


class Product(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ProductException(BaseException):
    pass


class Order(object):
    def __init__(self, person):
        self.person = person
        self.products = []

    def add(self, product):
        if not isinstance(product, Product):
            raise ProductException('Это не товар!')
        self.products.append(product)

    def get_cost(self):
        return sum([p.price for p in self.products])


person1 = Person('Дмитрий', 'Медведев', '+79997777777')
order1 = Order(person1)

product1 = Product('Домик для уточки', 60000000)
order1.add(product1)
product2 = Product('IPhone', 50000)
order1.add(product2)

print('Стоимость', order1.get_cost())
