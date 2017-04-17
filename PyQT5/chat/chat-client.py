import sys
import socket
from time import sleep
from datetime import datetime
import json
import threading

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QStackedWidget, QLabel, QLineEdit,
    QPlainTextEdit, QSpinBox, QTextBrowser, QPushButton,
    QVBoxLayout, QSplitter, QSpacerItem, QSizePolicy
)


class LoginWidget(QWidget):
    onLogin = pyqtSignal(str, str, int)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initUi()
        self._initSignals()
        self._initLayouts()

    def _initUi(self):
        self.flashMessage = QLabel(self)
        self.flushMessage()

        self.usernameEdit = QLineEdit(self)
        self.hostEdit = QLineEdit('192.168.7.50', self)
        self.portEdit = QSpinBox(self)

        self.portEdit.setMaximum(65535)
        self.portEdit.setValue(6666)

        self.loginBtn = QPushButton('Войти', self)

    def showMessage(self, message):
        self.flashMessage.setText(message)
        self.flashMessage.show()

    def flushMessage(self):
        self.flashMessage.clear()
        self.flashMessage.hide()

    def _initSignals(self):
        self.loginBtn.clicked.connect(self.onClickLoginBtn)

    def onClickLoginBtn(self):
        username = self.usernameEdit.text()

        if username:
            self.onLogin.emit(username, self.hostEdit.text(), self.portEdit.text())
        else:
            self.showMessage('Введите логин')

    def _initLayouts(self):
        self.spacer_1 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.spacer_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.addItem(self.spacer_1)
        self.mainLayout.addWidget(self.flashMessage)
        self.mainLayout.addWidget(self.usernameEdit)
        self.mainLayout.addWidget(self.hostEdit)
        self.mainLayout.addWidget(self.portEdit)
        self.mainLayout.addWidget(self.loginBtn)
        self.mainLayout.addItem(self.spacer_2)



class ChatWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._initUi()
        self._initSignals()
        self._initLayouts()

    def _initUi(self):
        pass

    def _initSignals(self):
        pass

    def _initLayouts(self):
        pass


class ChatClient(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__clientSocket = None

        self._initUi()
        self._initSignals()
        self._initLayouts()

    def _initUi(self):
        self.loginWidget = LoginWidget(self)
        self.chatWidget = ChatWidget(self)

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.addWidget(self.loginWidget)
        self.stackedWidget.addWidget(self.chatWidget)
        self.stackedWidget.setCurrentWidget(self.loginWidget)

        self.setCentralWidget(self.stackedWidget)

        self.resize(600, 400)

    def _initSignals(self):
        self.loginWidget.onLogin.connect(self.connect)

    def _initLayouts(self):
        pass

    def connect(self, username, host, port):
        self.__clientSocket = sock = socket.socket()

        try:
            sock.connect((host, port))

            thread = threading.Thread(target=self.wait, daemon=True)
            thread.start()

            self.stackedWidget.setCurrentWidget(self.chatWidget)
        except:
            self.loginWidget.showMessage('Сервер не доступен')
            return False

    def disconnect(self):
        if self.__clientSocket:
            self.__clientSocket.close()
            self.__clientSocket = None

    def wait(self):
        if self.__clientSocket is None:
            return
        while 1:
            message = self.__clientSocket.recv(4096)

            if not message:
                self.disconnect()
                break

#
            sleep(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = ChatClient()
    w.show()

    sys.exit(app.exec_())
