import argparse
from io import StringIO
from datetime import datetime
from os.path import exists as file_exists
from time import sleep
from urllib.parse import urljoin
import socket

import requests
from lxml import etree


# requests
# lxml  Xpath => лучше для xml
#       CSS Selectors => лучше для HTML
# cssselect
# Граббинг (сбор данных) и парсинг (разбор данных)
class Page(object):
    """Веб страница"""
    def __init__(self, url, params=None, **kwargs):
        self.__url = url
        self.__params = params
        self.__kwargs = kwargs
        self.__response = None

    def __call__(self, refresh=False):
        """Вызывается, когда объект используют как функцию"""
        if refresh or self.__response is None:
            self.__response = requests.get(self.__url, self.__params, **self.__kwargs)
        return self.__response


class Finder(object):
    """Поисковик элементов в документе с помощью CSS селекторов"""

    def __init__(self, page):
        self.__page = page
        self.__tree = None
        self.__context = None

    def __call__(self, css_selector):
        found = self.all(css_selector)
        if len(found):
            return found.pop()

    def all(self, css_selector):
        """ВЫполняет поиск всех элесентов на странице с заданным CSS селектором"""
        return self.context.cssselect(css_selector)

    @property
    def context(self): # getter
        if self.__context is None:
            return self.tree.getroot() # получить коренаой элемент
        return self.__context

    @context.setter
    def context(self, css_selector):  #setter
        self.__context = self(css_selector)

    @context.deleter
    def context(self):
        self.__context = None

    @property
    def tree(self):
        """Дерево веб документа"""
        if self.__tree is None:
            parser = etree.HTMLParser()
            self.__tree = etree.parse(StringIO(self.__page().text), parser)
        return self.__tree



class WeatherGrabber(object):
    """Граббер и парсер данных с сервиса Яндекс-Погода"""


class WeatherService(object):
    """Сервис погоды"""

    def show(self, search):
        print(search)

    def listen(self, ip, port):
        founder = Finder(Page('https://yandex.ru/pogoda/saint-petersburg'))

        temperature = founder('.current-weather__thermometer.current-weather__thermometer_type_now')
        print(temperature.text)

if __name__ == '__main__':
    service = WeatherService()
    parser = argparse.ArgumentParser(description='Сервис погоды')
    # создаем подпарсеры для вложеных аргументов
    subparsers = parser.add_subparsers()

    parser_show = subparsers.add_parser('show', description='Узнать погоду', help='Узнать погоду')
    parser_show.add_argument('-s', '--search', required=True, help='Город')
    parser_show.set_defaults(callback=service.show)

    parser_listen = subparsers.add_parser('listen', description='Запустить сервер', help='Запустить сервер')
    parser_listen.add_argument('-i', '--ip', default='127.0.0.1', help='ip адрес')
    # можно указать любой тип данных, help - описание при вызове справки, default - значение по умолчанию
    parser_listen.add_argument('-p', '--port', default=6666, type=int, help='Порт')
    parser_listen.set_defaults(callback=service.listen)

    # препращаем полученые аргументы из NameSpace  в словарь
    arguments = vars(parser.parse_args())
    callback = arguments.pop('callback')

    callback(**arguments)
