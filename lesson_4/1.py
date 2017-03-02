#   0 stdin => input()
#   1 stdout => print()
#   2 stderr => ошибки интерпретатора
#   open()
# os.path.join
# w, a, x (- если файл существует, ошибка, если нет - создан)
# w+, a+, x+ - добавление возможности читать файл

# f = open('out.txt', 'wb') # b - бинарный режим
# f.write(b'012345 \n')
# f.write(b'56789')
# f.writelines([b'c', b'd'])
# f.close()

# f = open('out.txt', 'r')
# # print(f.read(2)) # read(a) - прочитать 2 байта
# # print(f.read(4))
# # print(f.readlines())
# # for line in f:
# # #     f.readline()
# #     print(line)
# s = f.read()
# print(f.tell()) # позиция курсора
# f.seek(0) # перемещение курсора в 0 байт
# f.close()

# менеджеры контекста

# with open('out.txt') as f:
#     # print(f.read())

data = {
    'users': [
        {
            'id': 1,
            'name': 'Linus T',
            'skills': ('c++', 'linux')
        },
        {
            'id': 2,
            'name': 'R S',
            'skills': ('c++', 'GNU', 'Fifa')
        }

    ]
}

# Pickle

# import pickle
#
# with open('users.pickle', 'wb') as f:
#     pickle.dump(data, f)
#
# with open('users.pickle', 'rb') as f:
#     print(pickle.load(f))

# JSON => JavaScript Object Notation
# import json
#
# with open('users.json', 'w') as f:
#     json.dump(data, f)
#
# with open('users.json') as f:
#     print(json.load(f))

# ini

# csv
# id;name;skills

import csv

with open('users.csv', 'w') as f:
    users = data.get('users', [])
    fieldnames = users[0].keys() # check error
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    for user in users:
        writer.writerow(user)