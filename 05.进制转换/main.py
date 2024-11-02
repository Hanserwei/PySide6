import re
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
from 进制转化 import Ui_Form  # 确保这个模块是正确生成的


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.c1 = ''  # 输入进制
        self.c2 = ''  # 输出进制
        self.setupUi(self)  # 初始化 UI
        self.lineEdit_2.setReadOnly(True)  # 设置输出框为只读
        self.bind()
        self.input_value = ''  # 初始化输入值

    def bind(self):
        self.lineEdit.textEdited.connect(self.get_input)  # 监听输入框变化
        self.comboBox.currentTextChanged.connect(self.choice_1)  # 监听输入进制选择
        self.comboBox_2.currentTextChanged.connect(self.choice_2)  # 监听输出进制选择
        self.pushButton.clicked.connect(self.start)  # 监听开始转化按钮
        self.pushButton_2.clicked.connect(self.clearall)  # 监听清除按钮

    def get_input(self):
        self.input_value = self.lineEdit.text()  # 获取输入框的文本

    def choice_1(self):
        self.c1 = self.comboBox.currentText()  # 获取输入进制
        print(f"选择输入进制: {self.c1}")  # 调试输出

    def choice_2(self):
        self.c2 = self.comboBox_2.currentText()  # 获取输出进制
        print(f"选择输出进制: {self.c2}")  # 调试输出

    def start(self):
        if not self.c1 or not self.c2:
            QMessageBox.warning(self, "错误", "请选择输入和输出进制")  # 提示未选择进制
            return

        try:
            result = self.calculation(self.input_value, self.c1, self.c2)
            self.lineEdit_2.setText(result)  # 显示结果
        except ValueError as e:
            QMessageBox.warning(self, "错误", str(e))

    def calculation(self, value, base_from, base_to):
        # 检查输入值是否有效
        if base_from == "十六进制" and not re.match(r'^[0-9A-Fa-f]+$', value):
            raise ValueError("无效的十六进制数")
        elif base_from == "十进制" and not value.isdigit():
            raise ValueError("无效的十进制数")
        elif base_from == "八进制" and not re.match(r'^[0-7]+$', value):
            raise ValueError("无效的八进制数")
        elif base_from == "二进制" and not re.match(r'^[01]+$', value):
            raise ValueError("无效的二进制数")

        # 将输入值转换为十进制
        if base_from == "十六进制":
            decimal_value = int(value, 16)
        elif base_from == "十进制":
            decimal_value = int(value)
        elif base_from == "八进制":
            decimal_value = int(value, 8)
        elif base_from == "二进制":
            decimal_value = int(value, 2)
        else:
            raise ValueError("不支持的输入进制")

        # 将十进制值转换为目标进制
        if base_to == "十六进制":
            return hex(decimal_value).upper()[2:]  # 转换为十六进制并去掉 '0x'
        elif base_to == "十进制":
            return str(decimal_value)
        elif base_to == "八进制":
            return oct(decimal_value)[2:]  # 转换为八进制并去掉 '0o'
        elif base_to == "二进制":
            return bin(decimal_value)[2:]  # 转换为二进制并去掉 '0b'
        else:
            raise ValueError("不支持的输出进制")

    def clearall(self):
        self.lineEdit.clear()  # 清空输入框
        self.lineEdit_2.clear()  # 清空输出框
        self.comboBox.setCurrentIndex(0)  # 重置输入进制选择
        self.comboBox_2.setCurrentIndex(0)  # 重置输出进制选择
        self.c1 = ''  # 重置输入进制
        self.c2 = ''  # 重置输出进制

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("进制转化")  # 设置窗口标题
    window.show()
    sys.exit(app.exec())
