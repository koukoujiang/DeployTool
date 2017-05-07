import sys
import os,datetime,time,fileinput
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from Program import SecondWindow


class UI_ThirdTab(object):
    def setupUi(self, Form):
        self.LabelPath=QLabel('请选择需要打包的文件夹',self)
        self.LinePath=QLineEdit('',self)
        self.BtnGetFolderName=QPushButton('GetSiteName',self)
        self.BtnGetFolderName.clicked.connect(self.ButtonGetFolderName)

        h0layout=QHBoxLayout()
        h0layout.addWidget(self.LabelPath)
        h0layout.addWidget(self.LinePath)
        h0layout.addWidget(self.BtnGetFolderName)

        self.CheckBox_0=QCheckBox('NoSite',self)
        self.CheckBox_1=QCheckBox('NoSite',self)
        self.CheckBox_2=QCheckBox('NoSite',self)
        self.CheckBox_3=QCheckBox('NoSite',self)
        self.CheckBox_4=QCheckBox('NoSite',self)
        self.CheckBox_5=QCheckBox('NoSite',self)
        self.CheckBox_6=QCheckBox('NoSite',self)
        self.CheckBox_7=QCheckBox('NoSite',self)
        self.CheckBox_8=QCheckBox('NoSite',self)
        self.CheckBox_9=QCheckBox('NoSite',self)

        h1layout=QHBoxLayout()
        h1layout.addWidget(self.CheckBox_0)
        h1layout.addWidget(self.CheckBox_1)
        h1layout.addWidget(self.CheckBox_2)
        h1layout.addWidget(self.CheckBox_3)
        h1layout.addWidget(self.CheckBox_4)

        h2layout=QHBoxLayout()
        h2layout.addWidget(self.CheckBox_5)
        h2layout.addWidget(self.CheckBox_6)
        h2layout.addWidget(self.CheckBox_7)
        h2layout.addWidget(self.CheckBox_8)
        h2layout.addWidget(self.CheckBox_9)

        self.LabelZipFileName=QLabel('请输入Zip文件名',self)
        self.BtnZipFile=QPushButton('Zip File',self)
        self.LineZipFileName=QLineEdit('',self)
        self.BtnZipFile.clicked.connect(self.ThirdSingalZipFileEmit)

        h4layout=QHBoxLayout()
        h4layout.addWidget(self.LabelZipFileName)
        h4layout.addWidget(self.LineZipFileName)
        h4layout.addWidget(self.BtnZipFile)

        vlayout=QVBoxLayout()
        vlayout.addLayout(h0layout)
        vlayout.addLayout(h1layout)
        vlayout.addLayout(h2layout)
        vlayout.addLayout(h4layout)

        self.setLayout(vlayout)