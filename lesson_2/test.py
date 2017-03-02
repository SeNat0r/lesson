def func(text, time):
    # локальная зона видимости
    print(locals())
    f = open('file.log', 'a')  # а - добавление, w запись, r чтение
    # открыть файл в ржиме записи
    f.write(time + ' ' + text + '\n')
    f.close()


func('hello', '11:13')  # Порядковы (не именнованые)
func(time='named', text='123213')  # именнованые


def func2(a, b, c=100, d=200):
    print('a: {} b: {} c: {} d: {}'.format(a, b, c, d))


# на места фигурных скобок вставляются имена переменных
func2(1, 2, 35, 20)
func2(1, 2)


# *args, **kwargs
def func3(*args):  # сколько угодно аргументов
    print(args)
    print(len(args))
    if 4 in args:
        print('yahoo')


func3(1, 2, 3, 4, 5, 6)


def func4(**kwargs):
    print(kwargs)


func4(name='alex', age='12)')


def func5(x, *args, **kwargs):
    print('x: ', x)
    print('args: ', args)
    print('kwargs: ', kwargs)


func5(123, 4123, 123, 233, 543, 324, name='Alex', age=29)


def add(x, y):
    return x + y


x = add(10, 5)
print(x)

def get_some():
    x = 10
    y = 20
    return x, y

print(get_some())

x, y = get_some()
print(x,y)

# x, y = y, x ??? что будет?
