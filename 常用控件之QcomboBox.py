import sys

from PyQt6.QtWidgets import QApplication,QWidget,QComboBox,QVBoxLayout
from PyQt6.QtCore import Qt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        cb = QComboBox()
        cb.addItems(['李华','张三','小王'])
        cb.currentTextChanged.connect(self.showname)
        # cb.setEditable(True)

        mainlayout = QVBoxLayout()
        mainlayout.addWidget(cb)
        self.setLayout(mainlayout)

    def showname(self,name):
        print(name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
