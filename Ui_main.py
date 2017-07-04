# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cb/ericProject/pyvideo/main.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        MainWindow.setMinimumSize(QtCore.QSize(400, 300))
        MainWindow.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/logo3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 21))
        self.label.setObjectName("label")
        self.vipvideo = QtWidgets.QRadioButton(self.centralWidget)
        self.vipvideo.setGeometry(QtCore.QRect(120, 20, 117, 21))
        #self.vipvideo.setChecked(True)
        self.vipvideo.setObjectName("vipvideo")
        self.no_name = QtWidgets.QRadioButton(self.centralWidget)
        self.no_name.setGeometry(QtCore.QRect(270, 20, 117, 21))
        self.no_name.setObjectName("no_name")
        self.no_name.setChecked(True)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 121, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 60, 161, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.play = QtWidgets.QPushButton(self.centralWidget)
        self.play.setGeometry(QtCore.QRect(300, 60, 81, 41))
        self.play.setObjectName("play")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 361, 51))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_3.setLineWidth(1)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(0, 180, 391, 91))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setLineWidth(1)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "vip视频破解器"))
        self.label.setText(_translate("MainWindow", "解析站点选择"))
        self.vipvideo.setText(_translate("MainWindow", "v&ip视频解析"))
        self.no_name.setText(_translate("MainWindow", "无名小站"))
        self.label_2.setText(_translate("MainWindow", "输入vip视频地址"))
        self.play.setText(_translate("MainWindow", "播放"))
        self.label_3.setText(_translate("MainWindow", "大部分视频都能观看，如有不能观看的视频请刷新浏览器，或者更换解析站点。"))
        self.label_4.setText(_translate("MainWindow", "作者：南寻\ngithub地址 : https://github.com/nanxung/vip_video.git\n码云地址 : https://git.oschina.net/nanxun/vip_video.git "))

import pylogo_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

