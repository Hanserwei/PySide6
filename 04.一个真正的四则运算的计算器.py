import sys
from urllib.response import addbase

from PySide6.QtWidgets import QApplication,QWidget
from 计算器 import Ui_Form

class MyWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.numberResult = None
        self.setupUi(self)
        self.result = ''
        self.bind()

    def bind(self):
        self.pushButton_0.clicked.connect(lambda :self.addnumber('0'))
        self.pushButton_1.clicked.connect(lambda :self.addnumber('1'))
        self.pushButton_2.clicked.connect(lambda :self.addnumber('2'))
        self.pushButton_3.clicked.connect(lambda :self.addnumber('3'))
        self.pushButton_4.clicked.connect(lambda :self.addnumber('4'))
        self.pushButton_5.clicked.connect(lambda :self.addnumber('5'))
        self.pushButton_6.clicked.connect(lambda :self.addnumber('6'))
        self.pushButton_7.clicked.connect(lambda :self.addnumber('7'))
        self.pushButton_8.clicked.connect(lambda :self.addnumber('8'))
        self.pushButton_9.clicked.connect(lambda :self.addnumber('9'))
        self.pushButton_dot.clicked.connect(lambda :self.addnumber('.'))
        self.pushButton_addition.clicked.connect(lambda :self.addnumber('+'))
        self.pushButton_subtraction.clicked.connect(lambda :self.addnumber('-'))
        self.pushButton_multiplication.clicked.connect(lambda :self.addnumber('*'))
        self.pushButton_division.clicked.connect(lambda :self.addnumber('/'))
        self.pushButton_reuslt.clicked.connect(self.equal)
        self.pushButton.clicked.connect(self.back)
        self.pushButton_10.clicked.connect(self.clear)
    def addnumber(self,number):
        self.lineEdit.clear()
        self.result += number
        self.lineEdit.setText(self.result)

    def equal(self):
        self.numberResult = eval(self.result)
        self.lineEdit.setText(str(self.numberResult))

    def back(self):
        self.result = self.result[:-1]
        self.lineEdit.setText(self.result)

    def clear(self):
        self.result = ''
        self.lineEdit.clear()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())