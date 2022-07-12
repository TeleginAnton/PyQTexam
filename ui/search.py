# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(691, 382)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(691, 382))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_way = QLineEdit(Form)
        self.lineEdit_way.setObjectName(u"lineEdit_way")
        self.lineEdit_way.setMinimumSize(QSize(133, 25))
        self.lineEdit_way.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.lineEdit_way)

        self.pushButton_Open = QPushButton(Form)
        self.pushButton_Open.setObjectName(u"pushButton_Open")
        self.pushButton_Open.setMinimumSize(QSize(120, 23))
        self.pushButton_Open.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_Open)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_choice = QLineEdit(Form)
        self.lineEdit_choice.setObjectName(u"lineEdit_choice")
        self.lineEdit_choice.setMinimumSize(QSize(133, 25))
        self.lineEdit_choice.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_choice)

        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(120, 20))
        self.comboBox.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton_search = QPushButton(Form)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setMinimumSize(QSize(80, 25))
        self.pushButton_search.setMaximumSize(QSize(80, 20))

        self.horizontalLayout_3.addWidget(self.pushButton_search)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)

        self.pushButtonGoOver = QPushButton(Form)
        self.pushButtonGoOver.setObjectName(u"pushButtonGoOver")

        self.verticalLayout.addWidget(self.pushButtonGoOver)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        QWidget.setTabOrder(self.comboBox, self.pushButton_Open)
        QWidget.setTabOrder(self.pushButton_Open, self.lineEdit_way)
        QWidget.setTabOrder(self.lineEdit_way, self.pushButtonGoOver)
        QWidget.setTabOrder(self.pushButtonGoOver, self.lineEdit_choice)
        QWidget.setTabOrder(self.lineEdit_choice, self.pushButton_search)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433", None))
        self.pushButton_Open.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0447\u043d\u044b\u0439 \u043f\u043e\u0438\u0441\u043a", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u0411\u0438\u043d\u0430\u0440\u043d\u044b\u0439 \u043f\u043e\u0438\u0441\u043a", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0431\u0430\u0439\u0442\u0430\u043c", None))

        self.pushButton_search.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.pushButtonGoOver.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0435\u0439\u0442\u0438", None))
    # retranslateUi

