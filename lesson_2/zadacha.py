def cheloveg(x):
    for man in x:
        print('Имя: {}, Возраст: {}, Рост: {} '.format(man[0], man[1], man[2]))


people = [
    ['Иван', 10, 168],
    ['Мария', 20, 178],
    ['Григорий', 13, 216],
    ['Ирина', 16, 196],
    ['Кирилл', 27, 170]
]
cheloveg(people)
