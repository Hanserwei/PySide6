import sys

from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QVBoxLayout

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        mainlayout = QVBoxLayout()
        button = QPushButton('按钮',self)
        button.clicked.connect(self.hello)
        mainlayout.addWidget(button)
        self.setLayout(mainlayout)

    def hello(self):
        print("hello!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())