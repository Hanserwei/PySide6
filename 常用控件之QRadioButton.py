from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QRadioButton, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPlainTextEdit
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRadioButton")
        self.resize(300, 200)
        self.initUI()

    def initUI(self):
        self.radio1 = QRadioButton("Option 1")
        self.radio2 = QRadioButton("Option 2")
        self.radio3 = QRadioButton("Option 3")
        self.plainTextEdit = QPlainTextEdit()

        self.radio1.clicked.connect(self.radio_clicked)
        self.radio2.clicked.connect(self.radio_clicked)
        self.radio3.clicked.connect(self.radio_clicked)
        self.plainTextEdit.setPlainText("This is a plain text edit.")


        vbox = QVBoxLayout()
        vbox.addWidget(self.radio1)
        vbox.addWidget(self.radio2)
        vbox.addWidget(self.radio3)

        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("Choose an option:"))
        hbox.addLayout(vbox)

        self.setLayout(hbox)

    def radio_clicked(self):
        if self.radio1.isChecked():
            print("Option 1 is selected")
        elif self.radio2.isChecked():
            print("Option 2 is selected")
        elif self.radio3.isChecked():
            print("Option 3 is selected")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
