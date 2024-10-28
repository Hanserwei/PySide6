import sys

from PySide6.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PySide6.QtCore import Qt
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        mainlayout = QVBoxLayout()

        lb = QLabel('我是一个标签！',self)
        lb.setText('我是被修改的文字！')
        lb.setAlignment(Qt.AlignmentFlag.AlignCenter) # 凡是什么flag之类的东西都在QtCore里面

        mainlayout.addWidget(lb)
        self.setLayout(mainlayout)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())