# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
from Ui_main import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.urllist=['http://www.vipjiexi.com/tong.PHP?url=',
    'http://www.wmxz.wang/video.php?url=']
        self.url=self.urllist[1]
        self.center()
        self.flag=1


    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    @pyqtSlot()
    def on_vipvideo_pressed(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.url = self.urllist[0]
        self.flag = 0
    
    @pyqtSlot()
    def on_no_name_pressed(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.url = self.urllist[1]
        self.flag = 1
    
    @pyqtSlot()
    def on_play_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.lineEdit.text():
            self.url+=self.lineEdit.text()
            webbrowser.open(self.url)
        else:
            reply=QMessageBox.information(self, "警告","未输入有效url,继续输入点击yes,否则退出程序.",QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.No:
                sys.exit(1)



if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
