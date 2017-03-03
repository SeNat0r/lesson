# декораторы
# получение исходного кода страницы в байткоде
from urllib.request import urlopen

# def page(url):
#     return urlopen(url).read()
#
# python = page('http://python.org')
#
# print(python)

def page(url):
    # замкнутая область(замыкание)
    # создавать здесь свои переменные
    def get():
        return urlopen(url).read()
    return get

python = page('http://python.org')

# print(python())

# отрез символов
def trim(chars=None):
    # def fn():
    #     return s.strip(chars)
    # return fn
    # каррирование
    return lambda s: s.strip(chars)

spaces_trim = trim(' ')
slashes_trim = trim('/\\')
user = '       username           '
url = '/post/'

print(
    spaces_trim(user),
    slashes_trim(url)
)

# декораторы
# def decor(func):
#     def wrapper(*args,**kwargs):
#         result  = func(*args, **kwargs)
#         print('Результат: {}'.format(result))
#         return result
#     return wrapper
#
#
# @decor
# def do_something():
#     return 666
# do_something()
#
import  time



# started = time.time()
# result = factorial(1000)
# worked = time.time() - started
# print('выполнилась за {:f} микросекунд'.format(worked * 1e6))

# декоратор измеряющий время работы функции
def benchmark(func):
    def wrapper(*args, **kwargs):
        started = time.time()
        result = func(*args, **kwargs)
        worked = time.time() - started
        print('Функция {} выполнилась за {:f} микросекунд'.format(func.__name__, worked * 1e6))
        return result
    return wrapper

# декоратор с аргументами
def repeat(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []

            for i in range(count):
                results.append(func(*args, **kwargs))

            return results

        return wrapper

    return decorator

@benchmark
def factorial(x):
    f = 1

    for i in range(1, x + 1):
        f *= i
    return f


@repeat(5)
@benchmark
def do_something2():
    print('777')

factorial(100000)
do_something2()


