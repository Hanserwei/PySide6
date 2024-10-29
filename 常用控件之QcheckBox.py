import sys

from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout,QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        cb = QCheckBox('是否被选中！')
        cb.stateChanged.connect(self.showstate)

        btn = QPushButton('获取状态！')
        btn.clicked.connect(lambda :print(cb.isChecked()))


        mainlayout = QVBoxLayout()
        mainlayout.addWidget(cb)
        mainlayout.addWidget(btn)
        self.setLayout(mainlayout)

    def showstate(self, state):
        if state == 0:
            print("未选中")
        elif state == 2:
            print("已选中")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())