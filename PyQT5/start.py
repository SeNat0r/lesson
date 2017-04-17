import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

"""
QtCore - база
QtGui - вещи, связаные напрямую с графическим интерфейсом
QtWidgets - элементы интерфейса (кнопки, поля свода и т.д.)
QtNetwork

QSql
QWebKit
QWebKitWidgets
"""


class Start(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.resize(400, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Start()
    w.show()

    sys.exit(app.exec_())