import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Клиент для сервера погоды')

    parser.add_argument('-i', '--ip', default='127.0.0.1', help='ip адрес')
    # можно указать любой тип данных, help - описание при вызове справки, default - значение по умолчанию
    parser.add_argument('-p', '--port', default=6666, type=int, help='Порт')

    arguments = parser.parse_args()
    print(arguments.ip)