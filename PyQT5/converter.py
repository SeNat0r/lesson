import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QDoubleSpinBox, QPushButton, QVBoxLayout


class Converter(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUi()
        self.initSignals()
        self.initLayouts()

    def initUi(self):
        self.setWindowTitle('Конвертер валют')

        self.srcLable = QLabel('Сумма в рубля', self)
        self.srcAmount = QDoubleSpinBox(self)
        self.srcAmount.setMaximum(999999999)

        self.resultLabel = QLabel('Сумма в долларак', self)
        self.resultAmount = QDoubleSpinBox(self)
        self.resultAmount.setMaximum(999999999)

        self.convertBtn = QPushButton('Перевести', self)



    def initSignals(self):
        pass

    def initLayouts(self):
        w = QWidget(self)

        self.mainLayout = QVBoxLayout(w)
        self.mainLayout.addWidget(self.srcLable)
        self.mainLayout.addWidget(self.srcAmount)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addWidget(self.resultAmount)
        self.mainLayout.addWidget(self.convertBtn)

        self.setCentralWidget(w)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    cc = Converter()
    cc.show()

    sys.exit(app.exec_())