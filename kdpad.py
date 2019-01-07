# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot,Qt,QFile,QTextCodec
from PyQt5.QtWidgets import  QMainWindow,QFileDialog
from ui_kdpad import Ui_kdPad 
import os

class Kdpad(QMainWindow ):
    def __init__(self, parent=None):
        super(Kdpad,self).__init__(parent)
        self.ui = Ui_kdPad()
        self.ui.setupUi(self)
        self.tabDict = {}        
        self.tabCount = 1
        self.ui.tabBar.tabCloseRequested.connect(self.closeTab)

    @pyqtSlot()
    def on_newFile_clicked(self):
        tabIndex = self.tabCount + 1
        print(tabIndex)
        newTab = "tab" + str(tabIndex)
        newTe = "te"+ str(tabIndex)
        print("new tab name:" + newTab)
        setattr(self.ui,newTab,QtWidgets.QWidget())
        newTabObj = getattr(self.ui,newTab)
        newTabObj.setObjectName(newTab)
        setattr(self.ui, newTe , QtWidgets.QTextEdit(newTabObj))
        newTeObj = getattr(self.ui, newTe)
        newTeObj.setGeometry(QtCore.QRect(5, 0, 691, 391))
        newTeObj.setObjectName(newTab)
        self.ui.tabBar.addTab(newTabObj, "标签" + str(self.tabCount+1))
        self.ui.statusbar.showMessage("新建标签页" + newTab)
        self.ui.tabBar.setCurrentIndex(self.tabCount)
        
        self.tabCount = self.tabCount + 1

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        fh = ''
        if QFile.exists(filename):
            fh = QFile(filename)
 
        if not fh.open(QFile.ReadOnly):
            QtGui.qApp.quit()

        with open(filename,'r') as f:
            fContent =  f.read()
            self.getCurTe().setPlainText(fContent)
            self.tabDict[self.ui.tabBar.currentIndex()] = filename
            print(filename)
        self.setWindowTitle(filename)   
        
    def saveFile(self):
        filename = self.tabDict.get(self.ui.tabBar.currentIndex())
        print(filename)
        if filename == None :
            fs=QFileDialog.getSaveFileName(self,'save file',os.getenv('HOME'))
            filename = fs[0]
        with open(filename,'w') as f:
            my_text=self.getCurTe().toPlainText()
            f.write(my_text)
    @pyqtSlot()
    def on_saveFile_clicked(self):
        self.saveFile()
        
    @pyqtSlot()
    def on_openFile_clicked(self):
        self.openFile()
    
    def closeTab(self,index):
        #print(dir(e))
        print(index)
        self.ui.tabBar.removeTab(index)
    
    def getCurTe(self):
        curTabIndex = self.ui.tabBar.currentIndex()
        curTe = "te" + str(curTabIndex + 1)
        return getattr(self.ui,curTe)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = Kdpad()
    win.show();
    sys.exit(app.exec_())
