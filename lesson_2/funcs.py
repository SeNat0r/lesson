# функции
def some_other_func():
    print('123')
def func():
    f = open('file.log', 'a')   # а - добавление, w запись, r чтение
    # открыть файл в ржиме записи
    f.write('log\n')
    f.close()
    # some_other_func()

a = 0
while a < 10:
    a += 1
    func()  # запуск функции

