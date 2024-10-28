import sys

from PySide6.QtWidgets import QApplication,QWidget,QLineEdit,QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QVBoxLayout()

        line = QLineEdit()
        line.setPlaceholderText('请输入内容！')

        mainlayout.addWidget(line)
        self.setLayout(mainlayout)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())