# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\update.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from distutils.dir_util import copy_tree
from shutil import which
import time


class Ui_Osdag_Update(object):
    def setupUi(self, Osdag_Update):
        Osdag_Update.setObjectName("Osdag_Update")
        Osdag_Update.resize(415, 129)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../Files/Osdag Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Osdag_Update.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Osdag_Update)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 10, 381, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.Update = QtWidgets.QPushButton(self.centralwidget)
        self.Update.setGeometry(QtCore.QRect(50, 50, 93, 28))
        self.Update.setObjectName("Update")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(270, 50, 93, 28))
        self.cancel.setObjectName("cancel")
        Osdag_Update.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Osdag_Update)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 26))
        self.menubar.setObjectName("menubar")
        Osdag_Update.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Osdag_Update)
        self.statusbar.setObjectName("statusbar")
        Osdag_Update.setStatusBar(self.statusbar)

        self.retranslateUi(Osdag_Update)
        self.cancel.clicked.connect(Osdag_Update.close)
        QtCore.QMetaObject.connectSlotsByName(Osdag_Update)
        self.Update.clicked.connect(lambda: self.update_btn())

    def retranslateUi(self, Osdag_Update):
        _translate = QtCore.QCoreApplication.translate
        Osdag_Update.setWindowTitle(_translate("Osdag_Update", "Osdag Update"))
        self.Update.setText(_translate("Osdag_Update", "Update"))
        self.cancel.setText(_translate("Osdag_Update", "Cancel"))



    def update_btn(self):
        path = which('osdag')
        if path is not None:
            path = path[:-9]
            print(path)
            src = './Files/osdag/'
            copy_tree(src, path)
            for i in range(101):
                time.sleep(0.01

                           )
                self.progressBar.setValue(i)
            Osdag_Update.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Osdag_Update = QtWidgets.QMainWindow()
    ui = Ui_Osdag_Update()
    ui.setupUi(Osdag_Update)
    Osdag_Update.show()
    sys.exit(app.exec_())
