import sys
import os,datetime,time,fileinput
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from Program import SecondWindow


class UI_FouthTab(object):
    def setupUi(self, Form):
        self.LabelSrc=QLabel('请选择源文件',self)
        self.LineSrc =QLineEdit('')
        self.BtnSrc = QPushButton('选择文件', self)
        self.BtnSrc.clicked.connect(self.ButtonSrcShowDialog)



        self.LabelDst=QLabel('请选择目标文件',self)
        self.LineDst =QLineEdit('',self)
        self.BtnDst = QPushButton('选择文件', self)
        self.BtnDst.clicked.connect(self.ButtonDstShowDialog)


        self.BtnStart = QPushButton('文件对比', self)
        self.BtnStart.clicked.connect(self.FouthSingalFileCompareEmit)


        upgrid=QGridLayout()
        #grid.setSpacing(10)
        upgrid.addWidget(self.LabelSrc,1,0)
        upgrid.addWidget(self.LineSrc,1,1)
        upgrid.addWidget(self.BtnSrc,1,2)
        upgrid.addWidget(self.LabelDst,2,0)
        upgrid.addWidget(self.LineDst,2,1)
        upgrid.addWidget(self.BtnDst,2,2)


        upgrid.addWidget(self.BtnStart,3,2)
        upgrid.setColumnStretch(0,1)
        upgrid.setColumnStretch(1,3)





        vlayout=QVBoxLayout()


        MainGrid=QGridLayout()
        MainGrid.addLayout(upgrid,0,0)
        MainGrid.addLayout(vlayout,1,0)



        self.setLayout(MainGrid)


