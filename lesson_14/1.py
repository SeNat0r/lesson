# utf-8
"""
__new__(cls) - настоящий конструктор
__init__(self) - конструктор (инициализация)
__del__(self) - деструктор

__int__
__float__
__bool__
__str__ (__unicode__) - (python 2)
"""

from pprint import pprint


class Product(object):
    """Атата, документация"""

    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        """Вызывается при конвертации в str"""
        return self.title

    def __repr__(self):
        """Вызывается repr() для получения строки 'формального' представления оюъекта"""
        return 'Класс: {}\nПродукт "{}" стоимостью {}'.format(self.__class__, self.title, self.price)

    def __float__(self):
        """Вызывается при конвертации в float"""
        return self.price


class Cart(object):
    __slots__ = ['products']

    def __init__(self):
        self.products = []

    def __iter__(self):
        return self

    def __next__(self):
        for product in self.products:
            return product
        raise StopIteration

    def __len__(self):
        return len(self.products)

    def __getitem__(self, item):
        if item < len(self):
            return self.products[item]

    def __setitem__(self, key, product):
        # self.products.insert(key, product)
        self.products[key] = product

    def add(self, product):
        self.products.append(product)

    def __delitem__(self, key):
        if key < len(self):
            self.products.pop(key)


# print('Имя класса: {}'.format(Product.__name__))
# print('Имя модуля: {}'.format(Product.__module__))
# print('Кортеж базовых классов: {}'.format(Product.__bases__))
#
# print('Словарь атрибутов класса')
# pprint(Product.__dict__)

book = Product('ООП', 999.13)
book2 = Product('Совершенный код', 700.13)
book3 = Product('Шаблоны?', 350.15)
cart = Cart()
cart.add(book)
cart.add(book2)
cart.add(book3)
# cart[2] = book3

# for p in cart:
#     print('В корзине: {}'.format(p))

# print('Класс, на основе которого создан объект: {}'.format(book.__class__))
#
# print('Словарь атрибутов объекта на основе класса')
# pprint(book.__dict__)
#
# print(Product.__doc__)

# print(repr(book))
# print(float(book))
print('Кол-во кник в корзине: {}'.format(len(cart)))


# Перегрузка операторов

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """ПЕрегрузка оператора +"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """ПЕрегрузка оператора -"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """ПЕрегрузка оператора *"""
        return Vector(self.x * other.x, self.y * other.y)

    def __lt__(self, other):
        """
        Перегрузка оператора <
        (переопределение)
        """
        return self.length() < other.length()

    def __eq__(self, other):
        """Перегрузка оператора =="""
        return self.length() == other.length()

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(1, 5)
v2 = Vector(1, 8)

print('Сумма векторов v1 + v2 = {}'.format(v1 + v2))
print('Разность векторов v1 - v2 = {}'.format(v1 - v2))
print('Произведение векторов v1 * v2 = {}'.format(v1 * v2))

print('{} > {}: {}'.format(v1, v2, v1 > v2))
print('{} < {}: {}'.format(v1, v2, v1 < v2))
print('{} <= {}: {}'.format(v1, v2, v1 == v2))
print('{} <= {}: {}'.format(v1, v2, v1 != v2))
