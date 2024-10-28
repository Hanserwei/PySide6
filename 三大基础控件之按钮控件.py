import sys

from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton('来点点我',self)
        btn.setGeometry(100,100,200,100)
        btn.setToolTip('点我有惊喜！')
        btn.setText('我被重新设置了！')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())