# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '计算器.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(381, 368)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 371, 361))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 70))
        self.lineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.pushButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_7 = QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(30, 40))

        self.horizontalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(30, 40))

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.layoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(30, 40))

        self.horizontalLayout.addWidget(self.pushButton_9)

        self.pushButton_addition = QPushButton(self.layoutWidget)
        self.pushButton_addition.setObjectName(u"pushButton_addition")
        self.pushButton_addition.setMinimumSize(QSize(30, 40))

        self.horizontalLayout.addWidget(self.pushButton_addition)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(30, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(30, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(30, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_subtraction = QPushButton(self.layoutWidget)
        self.pushButton_subtraction.setObjectName(u"pushButton_subtraction")
        self.pushButton_subtraction.setMinimumSize(QSize(30, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_subtraction)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_1 = QPushButton(self.layoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setMinimumSize(QSize(30, 40))

        self.horizontalLayout_3.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(30, 40))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(30, 40))

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_multiplication = QPushButton(self.layoutWidget)
        self.pushButton_multiplication.setObjectName(u"pushButton_multiplication")
        self.pushButton_multiplication.setMinimumSize(QSize(30, 40))

        self.horizontalLayout_3.addWidget(self.pushButton_multiplication)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_0 = QPushButton(self.layoutWidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        self.pushButton_0.setMinimumSize(QSize(30, 40))

        self.horizontalLayout_4.addWidget(self.pushButton_0)

        self.pushButton_dot = QPushButton(self.layoutWidget)
        self.pushButton_dot.setObjectName(u"pushButton_dot")
        self.pushButton_dot.setMinimumSize(QSize(30, 40))

        self.horizontalLayout_4.addWidget(self.pushButton_dot)

        self.pushButton_reuslt = QPushButton(self.layoutWidget)
        self.pushButton_reuslt.setObjectName(u"pushButton_reuslt")
        self.pushButton_reuslt.setMinimumSize(QSize(30, 40))

        self.horizontalLayout_4.addWidget(self.pushButton_reuslt)

        self.pushButton_division = QPushButton(self.layoutWidget)
        self.pushButton_division.setObjectName(u"pushButton_division")
        self.pushButton_division.setMinimumSize(QSize(30, 40))

        self.horizontalLayout_4.addWidget(self.pushButton_division)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.pushButton_10 = QPushButton(self.layoutWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.pushButton_10)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u673a", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u56de\u9000", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_addition.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_subtraction.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_multiplication.setText(QCoreApplication.translate("Form", u"*", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_dot.setText(QCoreApplication.translate("Form", u".", None))
        self.pushButton_reuslt.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97", None))
        self.pushButton_division.setText(QCoreApplication.translate("Form", u"/", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
    # retranslateUi

