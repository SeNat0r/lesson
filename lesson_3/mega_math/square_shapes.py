from cmath import pi as PI  # переопределение импортированной функции


def calculate_square_area(a):
    return a ** 2


def calculate_rectangle_area(a, b):
    return a * b


def calculate_triangle_area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def calculate_circle_area(r):
    return PI * r ** 2


if __name__ == '__main__':
    print('Модуль запускаемы')
