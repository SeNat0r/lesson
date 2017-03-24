# t1 = 3
# t2 = 3
# t3 = 100000
# t4 = 100000
#
# print(t3 is t4)

# перелокация памяти - копирование массива в другую ячейку памяти, когда закончились зарезервированные ячейки массива

# Set множества
# не сохраняет последовательность. только уникальные значения
# l1 = ['q','w','e']
# l2 = [1,2,3]
# print(dict(zip(l1,l2)))

# def fib(n):
#     if n < 2:
#         return n
#     return fib(n - 2) + fib(n - 1)
# print(fib(40))
# def fib(n):
#     if n < 2:
#         return n
#     a, b = 0, 1
#     for i in range(n):
#         a,b = b, a + b
#     return a
#
# print(fib(100000))


def fib(n):
    if n < 2:
        return n
