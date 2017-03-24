# Singleton - одиночка
import sqlite3


class DB(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)


class SingletonMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)

        return cls.__instances[cls]


class DB2(metaclass=SingletonMeta):
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Config(object):
    pass


db1 = DB2(':memory:')
db2 = DB2(':memory:')

# print(db1, db2)
config1 = Config()
config2 = Config()

# print(config1 == config2)

# Command - Команда, действие
from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class ShowVersionCommand(Command):
    def execute(self):
        print('1.0')


class HelpCommand(Command):
    def execute(self):
        print('I need help!')


commands = {
    'version': ShowVersionCommand,
    'help': HelpCommand
}

from random import randrange


# Observer - Наблюдатель

class Subject(object):
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        if isinstance(observer, Observer):
            self._observers.append(observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.handle_event()


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def handle_event(self):
        pass


class LoginHandler(Subject):
    def authorize(self):
        """
        Результаты работы:
            1. Успешный вход
            2. Ошибка при входе

        Требования:
            1. Логировать все успешные входы
            2. Логировать все попытки входа
            3. Ошибка провайдера, отсыаем cookie
        :return:
        """
        result = randrange(3)

        if result == 0:
            print('Успешный вход')
        elif result == 1:
            print('Неверный логин/пароль')
        self.notify()

class LoggerObserver(Observer):
    pass


class ErrorObserver(Observer):
    pass


class CookieObserver(Observer):
    pass

login_handler = LoginHandler()

login_handler.add_observer(LoggerObserver())
login_handler.add_observer(ErrorObserver())
login_handler.add_observer(CookieObserver())

login_handler.authorize()