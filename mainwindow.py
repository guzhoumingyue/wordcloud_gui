# -*- coding:utf-8 -*-
"""
 * @file MyServer
 * @author 党智腾
 * mail 642212607@qq.com
 * WeChat dangzhiteng
 * @date 2018-05-14
 * @version V 1.0
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Mainwin(object):
    def setupUi(self, Mainwin):
        Mainwin.setObjectName("Mainwin")
        Mainwin.resize(826, 640)
        self.gridLayout = QtWidgets.QGridLayout(Mainwin)
        self.gridLayout.setObjectName("gridLayout")
        self.load_text = QtWidgets.QPushButton(Mainwin)
        self.load_text.setObjectName("load_text")
        self.gridLayout.addWidget(self.load_text, 0, 4, 1, 1)
        self.show_pic = QtWidgets.QLabel(Mainwin)
        self.show_pic.setText("")
        self.show_pic.setObjectName("show_pic")
        self.gridLayout.addWidget(self.show_pic, 2, 0, 1, 6)
        self.begin = QtWidgets.QPushButton(Mainwin)
        self.begin.setObjectName("begin")
        self.gridLayout.addWidget(self.begin, 1, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.changeset = QtWidgets.QPushButton(Mainwin)
        self.changeset.setObjectName("changeset")
        self.gridLayout.addWidget(self.changeset, 1, 0, 1, 1)
        self.save_pic = QtWidgets.QPushButton(Mainwin)
        self.save_pic.setObjectName("save_pic")
        self.gridLayout.addWidget(self.save_pic, 1, 3, 1, 1)
        self.text_path = QtWidgets.QLineEdit(Mainwin)
        self.text_path.setMinimumSize(QtCore.QSize(0, 30))
        self.text_path.setDragEnabled(True)
        self.text_path.setObjectName("text_path")
        self.gridLayout.addWidget(self.text_path, 0, 0, 1, 4)
        self.label = QtWidgets.QLabel(Mainwin)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(Mainwin)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 4, 1, 1)

        self.retranslateUi(Mainwin)
        QtCore.QMetaObject.connectSlotsByName(Mainwin)

    def retranslateUi(self, Mainwin):
        _translate = QtCore.QCoreApplication.translate
        Mainwin.setWindowTitle(_translate("Mainwin", "词云生成器"))
        self.load_text.setText(_translate("Mainwin", "加载文本"))
        self.begin.setText(_translate("Mainwin", "开始生成"))
        self.changeset.setText(_translate("Mainwin", "调整配置"))
        self.save_pic.setText(_translate("Mainwin", "保存图片"))
        self.label.setText(_translate("Mainwin", "版本号V1.0"))
        self.label_2.setText(_translate("Mainwin", "---党智腾"))

import source_rc
