# Исключение
# Генерация исключения
# raise RuntimeError('Сообщение об ошибке')
#
# while True:
#     try:
#         i = int(input())
#         break
#         # func()
#         # a = i + '666'
#     except ValueError as e:
#         print(e)
#     except NameError:
#         print('Несуществующая функция')
#     except:
#         print('Ошибка')
#     finally:
#         print('Этот блок выполняется всегда')

# Итераторы и генераторы
# s = 'Linus Torvalds'
# lst = [1, 2, 3, 4, 5]
person = {
    'name': 'linus torvalds',
    'age': 47,
    'is_developer': True
}


#
# for i in s:
#     print(i)
#
# def generator():
#     print('Шаг 1')
#     yield 1
#     print('Шаг 2')
#     yield 2
#     print('Шаг 3')

def countdown(n):
    print('Генератор стартовал')
    while n:
        yield n
        n -= 1


#
# for i in countdown(5):
#     print('Генератор вернул {}'.format(i))

# def generator_range(first, last):
#     for i in range(first, last):
#         yield i
#
# # Python >= 3.3
#
# def generator_range2(first, last):
#     yield from range(first, last)

# Генераторы списков/множеств/словарей
#
numbers = [1, 1, 2, 2, 3, 3]
#
# squares = [i * i for i in numbers]
# odd = [i for i in numbers if i % 2]
# points = [(x, y) for x in range(3) for y in range(2)]
# # short way => set(numbers)
# s = {i for i in numbers}
#
# keys = ['id', 'name', 'age']
values = [1, 'linus torvalds', 47]

# # short way = > dict(zip(keys, values))
#
# data = {k.upper(): v for i, k in enumerate(keys) for j, v in enumerate(values) if i == j}
#
# print(data)

data = [
    {
        'id': 1,
        'name': 'linus torvalds',
        'age': 63
    },
    {
        'id': 2,
        'name': 'Richard',
        'age': 88
    },
    {
        'id': 1,
        'name': 'linus torvalds',
        'age': 63
    }
]

# persons = {d['id']: d for d in data}
# print(persons)

# Выражения-генераторы

# gen_squares = (i * i for i in numbers)
# print(gen_squares)
#
# with open('unittest_lesson.py') as f:
#     lines = (line.strip() for line in f)
#     linuses = (l for l in lines if 'linus torvalds' in l)
#     # print(list(linuses))
#     linuses.throw(RuntimeError, 'Моя ошибка')
#     print(next(linuses))
#     linuses.close()  # GeneratorExit


# Сопрограммы
def coroutine(func):
    def wrapper(*args,**kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return wrapper

@coroutine
def echo():
    print('Генератор готв к приему сообщения')
    while True:
        msg = (yield)
        print(msg)

e = echo()
e.send('Hi!')
e.send('I like it!')