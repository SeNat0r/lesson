import sys

from url_shortener import storage

conn = storage.connect()
storage.initialize(conn)


def action_find_all():
    urls = storage.find_all(conn)

    for url in urls:
        print('{url[short_url]} - {url[original_url]} - {url[created}}'.format(url=url))


def action_show_menu():
    print('''
Сокращатель ссылок

1. Добавить url адрес
2. Найти оригинальный url адрес
3. Вывести все url адреса
m. Показать меню
q. Выйти''')


def action_exit():
    sys.exit(0)


actions = {
    'm': action_show_menu(),
    'q': action_exit()
}

if __name__ == '__main__':
    action_show_menu()

while True:
    cmd = input('\nВВедите команду: ')
    action = actions.get(cmd)

    if action:
        action()
    else:
        print('Неизвестная команда')
