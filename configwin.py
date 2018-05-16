# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configwin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

"""
 * @file MyServer
 * @author 党智腾
 * mail 642212607@qq.com
 * WeChat dangzhiteng
 * @date 2018-05-14
 * @version V 1.0
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Config(object):
    def setupUi(self, Config):
        Config.setObjectName("Config")
        Config.resize(301, 352)
        self.gridLayout = QtWidgets.QGridLayout(Config)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(Config)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Config)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.mask_path_line = QtWidgets.QLineEdit(Config)
        self.mask_path_line.setMinimumSize(QtCore.QSize(0, 30))
        self.mask_path_line.setObjectName("mask_path_line")
        self.gridLayout.addWidget(self.mask_path_line, 0, 0, 1, 2)
        self.color_random = QtWidgets.QSpinBox(Config)
        self.color_random.setMinimum(1)
        self.color_random.setMaximum(300)
        self.color_random.setProperty("value", 60)
        self.color_random.setObjectName("color_random")
        self.gridLayout.addWidget(self.color_random, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(Config)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.max_word = QtWidgets.QSpinBox(Config)
        self.max_word.setMinimum(1)
        self.max_word.setMaximum(300)
        self.max_word.setProperty("value", 150)
        self.max_word.setObjectName("max_word")
        self.gridLayout.addWidget(self.max_word, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Config)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.font_path = QtWidgets.QPushButton(Config)
        self.font_path.setObjectName("font_path")
        self.gridLayout.addWidget(self.font_path, 1, 2, 1, 1)
        self.min_size = QtWidgets.QSpinBox(Config)
        self.min_size.setMinimum(1)
        self.min_size.setMaximum(300)
        self.min_size.setProperty("value", 10)
        self.min_size.setObjectName("min_size")
        self.gridLayout.addWidget(self.min_size, 6, 1, 1, 1)
        self.mask_path = QtWidgets.QPushButton(Config)
        self.mask_path.setObjectName("mask_path")
        self.gridLayout.addWidget(self.mask_path, 0, 2, 1, 1)
        self.max_size = QtWidgets.QSpinBox(Config)
        self.max_size.setMinimum(1)
        self.max_size.setMaximum(300)
        self.max_size.setProperty("value", 80)
        self.max_size.setObjectName("max_size")
        self.gridLayout.addWidget(self.max_size, 5, 1, 1, 1)
        self.font_path_line = QtWidgets.QLineEdit(Config)
        self.font_path_line.setMinimumSize(QtCore.QSize(0, 30))
        self.font_path_line.setObjectName("font_path_line")
        self.gridLayout.addWidget(self.font_path_line, 1, 0, 1, 2)
        self.color = QtWidgets.QPushButton(Config)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color.sizePolicy().hasHeightForWidth())
        self.color.setSizePolicy(sizePolicy)
        self.color.setMinimumSize(QtCore.QSize(35, 35))
        self.color.setBaseSize(QtCore.QSize(35, 35))
        self.color.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.color.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.color.setAutoFillBackground(False)
        self.color.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.color.setText("")
        self.color.setObjectName("color")
        self.gridLayout.addWidget(self.color, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(Config)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.configbtn = QtWidgets.QPushButton(Config)
        self.configbtn.setObjectName("configbtn")
        self.gridLayout.addWidget(self.configbtn, 7, 0, 1, 3)

        self.retranslateUi(Config)
        QtCore.QMetaObject.connectSlotsByName(Config)

    def retranslateUi(self, Config):
        _translate = QtCore.QCoreApplication.translate
        Config.setWindowTitle(_translate("Config", "调整参数"))
        self.label_3.setText(_translate("Config", "最小字号:"))
        self.label_4.setText(_translate("Config", "背景色:"))
        self.mask_path_line.setText(_translate("Config", "source/mask.jpg"))
        self.label_5.setText(_translate("Config", "最大字数:"))
        self.label_2.setText(_translate("Config", "最大字号:"))
        self.font_path.setText(_translate("Config", "字体路径"))
        self.mask_path.setText(_translate("Config", "mask路径"))
        self.font_path_line.setText(_translate("Config", "source/方正小标宋.TTF"))
        self.label.setText(_translate("Config", "颜色种类:"))
        self.configbtn.setText(_translate("Config", "配置完成"))
