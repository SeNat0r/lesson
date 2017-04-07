import argparse
import socket

class WeatherClient(object):
    def __init__(self, ip, port):
        self.__address = (ip, port)

    def connect(self):
        while 1:
            search = input('Введите город: ')

            if search:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect(self.__address)
                    s.send(search.encode())
                    data = s.recv(204800)
                    print(data.decode())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Клиент для сервера погоды')

    parser.add_argument('-i', '--ip', default='127.0.0.1', help='ip адрес')
    # можно указать любой тип данных, help - описание при вызове справки, default - значение по умолчанию
    parser.add_argument('-p', '--port', default=6666, type=int, help='Порт')

    arguments = parser.parse_args()
    client = WeatherClient(arguments.ip, arguments.port)
    client.connect()