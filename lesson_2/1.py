# x = 0
# while x < 10:
#     x += 1
#     print(x)
# while True:
#     x += 1
#     if x > 20:
#         print('ok 20')
#         break  # завершает цикл принудительно
#     print('.')
#
# # перечисление элементов массива
# for a in lst:
#     pass

lst = [[1,2],[3,4],[5,6],[7,8]]
for a in lst:
    # if a == 100:
    #     continue
    # print(a)

    for b in a:
        print(b)
else: # запускается в том случае, если внутри цикла не было break
    print('!!!')