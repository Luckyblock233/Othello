# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(680, 520)
        self.verticalLayoutWidget = QWidget(Widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(580, 10, 91, 71))
        self.verticalLayoutWidget.setAutoFillBackground(False)
        self.gridLayout = QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.Label_black_number = QLabel(self.verticalLayoutWidget)
        self.Label_black_number.setObjectName(u"Label_black_number")
        font = QFont()
        font.setFamilies([u"\u6c49\u4eea\u65d7\u9ed1 90S"])
        font.setPointSize(11)
        font.setBold(False)
        self.Label_black_number.setFont(font)
        self.Label_black_number.setAutoFillBackground(False)
        self.Label_black_number.setFrameShape(QFrame.Box)
        self.Label_black_number.setScaledContents(False)

        self.gridLayout.addWidget(self.Label_black_number, 0, 0, 1, 1)

        self.Label_white_number = QLabel(self.verticalLayoutWidget)
        self.Label_white_number.setObjectName(u"Label_white_number")
        self.Label_white_number.setFont(font)
        self.Label_white_number.setFrameShape(QFrame.Box)

        self.gridLayout.addWidget(self.Label_white_number, 1, 0, 1, 1)

        self.verticalLayoutWidget_2 = QWidget(Widget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(500, 10, 81, 71))
        self.gridLayout_2 = QGridLayout(self.verticalLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 0, 3, 0)
        self.Label_white_number_2 = QLabel(self.verticalLayoutWidget_2)
        self.Label_white_number_2.setObjectName(u"Label_white_number_2")
        self.Label_white_number_2.setFont(font)
        self.Label_white_number_2.setAutoFillBackground(False)
        self.Label_white_number_2.setFrameShape(QFrame.NoFrame)
        self.Label_white_number_2.setScaledContents(False)

        self.gridLayout_2.addWidget(self.Label_white_number_2, 1, 0, 1, 1)

        self.Label_black_number_2 = QLabel(self.verticalLayoutWidget_2)
        self.Label_black_number_2.setObjectName(u"Label_black_number_2")
        self.Label_black_number_2.setFont(font)
        self.Label_black_number_2.setAutoFillBackground(False)
        self.Label_black_number_2.setFrameShape(QFrame.NoFrame)
        self.Label_black_number_2.setScaledContents(False)

        self.gridLayout_2.addWidget(self.Label_black_number_2, 0, 0, 1, 1)

        self.ScrollArea_History = QScrollArea(Widget)
        self.ScrollArea_History.setObjectName(u"ScrollArea_History")
        self.ScrollArea_History.setGeometry(QRect(500, 90, 171, 361))
        self.ScrollArea_History.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 169, 359))
        self.ScrollArea_History.setWidget(self.scrollAreaWidgetContents)
        self.Button_remake = QPushButton(Widget)
        self.Button_remake.setObjectName(u"Button_remake")
        self.Button_remake.setGeometry(QRect(500, 460, 171, 31))
        font1 = QFont()
        font1.setFamilies([u"\u6c49\u4eea\u65d7\u9ed1 90S"])
        font1.setPointSize(11)
        self.Button_remake.setFont(font1)
        self.Button_remake.setFocusPolicy(Qt.ClickFocus)
        self.Button_remake.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.Label_black_number.setText("")
        self.Label_white_number.setText("")
        self.Label_white_number_2.setText(QCoreApplication.translate("Widget", u"\u767d\u68cb\u6570\u91cf\uff1a", None))
        self.Label_black_number_2.setText(QCoreApplication.translate("Widget", u"\u9ed1\u68cb\u6570\u91cf\uff1a", None))
        self.Button_remake.setText(QCoreApplication.translate("Widget", u"\u91cd\u65b0\u5f00\u59cb\u6e38\u620f", None))
    # retranslateUi

