# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kdpad.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_kdPad(object):
    def setupUi(self, kdPad):
        kdPad.setObjectName("kdPad")
        kdPad.resize(707, 538)
        self.centralwidget = QtWidgets.QWidget(kdPad)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 691, 461))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBar = QtWidgets.QHBoxLayout()
        self.toolBar.setObjectName("toolBar")
        self.newFile = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.newFile.setObjectName("newFile")
        self.toolBar.addWidget(self.newFile)
        self.openFile = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.openFile.setObjectName("openFile")
        self.toolBar.addWidget(self.openFile)
        self.saveFile = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.saveFile.setObjectName("saveFile")
        self.toolBar.addWidget(self.saveFile)
        self.verticalLayout.addLayout(self.toolBar)
        self.tabBar = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabBar.setEnabled(True)
        self.tabBar.setElideMode(QtCore.Qt.ElideLeft)
        self.tabBar.setUsesScrollButtons(True)
        self.tabBar.setDocumentMode(False)
        self.tabBar.setTabsClosable(True)
        self.tabBar.setMovable(True)
        self.tabBar.setObjectName("tabBar")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setAccessibleName("")
        self.tab1.setObjectName("tab1")
        self.te1 = QtWidgets.QTextEdit(self.tab1)
        self.te1.setGeometry(QtCore.QRect(5, 0, 691, 391))
        self.te1.setObjectName("te1")
        self.tabBar.addTab(self.tab1, "")
    
        self.verticalLayout.addWidget(self.tabBar)
        kdPad.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(kdPad)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 33))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        kdPad.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(kdPad)
        self.statusbar.setObjectName("statusbar")
        kdPad.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(kdPad)
        self.tabBar.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(kdPad)

    def retranslateUi(self, kdPad):
        _translate = QtCore.QCoreApplication.translate
        kdPad.setWindowTitle(_translate("kdPad", "kdPad"))
        self.newFile.setText(_translate("kdPad", "新建"))
        self.openFile.setText(_translate("kdPad", "打开"))
        self.saveFile.setText(_translate("kdPad", "保存"))
        self.tabBar.setTabText(self.tabBar.indexOf(self.tab1), _translate("kdPad", "tab1"))
  
        self.menuFile.setTitle(_translate("kdPad", "文件"))
        self.menuEdit.setTitle(_translate("kdPad", "编辑"))
        self.statusbar.setToolTip(_translate("kdPad", "状态栏"))
        self.statusbar.setStatusTip(_translate("kdPad", "状态栏"))
        self.statusbar.setWhatsThis(_translate("kdPad", "状态栏"))

