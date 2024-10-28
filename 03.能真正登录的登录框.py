import sys


from PySide6.QtWidgets import QApplication,QWidget,QLineEdit
from 登录框 import Ui_Form

class MyWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.loginFuc)
    def loginFuc(self):
        # 拿到账号
        account = self.lineEdit.text()
        # 拿到密码
        password = self.lineEdit_2.text()
        if account=='admin' and password=='wwgb1314':
            print('登录成功！')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())