import sys
import os,datetime,time,fileinput
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ConfRead import Conf
from PyQt5.QtGui import *
#from Program import SecondWindow

class UI_FifthTab(object):
    def setupUi(self, Form):
        self.LabelSrc=QLabel('请选择源路径',self)
        self.LineSrc =QLineEdit(Conf().GetLastFile_LabelSrc)
        self.BtnSrc = QPushButton('Src', self)
        #self.BtnSrc.clicked.connect(self.ButtonSrcShowDialog)


        self.LabelDst=QLabel('请选择目标路径',self)
        self.LineDst =QLineEdit(Conf().GetLastFile_LabelDst,self)
        self.BtnDst = QPushButton('Dst', self)
        #self.BtnDst.clicked.connect(self.ButtonDstShowDialog)

        self.CheckBoxKeyFile=QCheckBox('仅提取指定文件(文件名请用逗号隔开)',self)
        self.LineKeyFile=QLineEdit('',self)

        upgrid=QGridLayout()
        #grid.setSpacing(10)
        upgrid.addWidget(self.LabelSrc,1,0)
        upgrid.addWidget(self.LineSrc,1,1)
        upgrid.addWidget(self.BtnSrc,1,2)
        upgrid.addWidget(self.LabelDst,2,0)
        upgrid.addWidget(self.LineDst,2,1)
        upgrid.addWidget(self.BtnDst,2,2)
        upgrid.addWidget(self.CheckBoxKeyFile,3,0,Qt.AlignRight)
        upgrid.addWidget(self.LineKeyFile,3,1,)
        upgrid.setColumnStretch(0,1)
        upgrid.setColumnStretch(1,3)

        self.LabelTime=QLabel('请输入时间差，单位：小时',self)
        self.SpinBoxTime=QDoubleSpinBox()
        self.SpinBoxTime.setValue(1.00)
        self.SpinBoxTime.setMaximum(720.00)
        self.BtnGetLastFile=QPushButton('GetLastFile',self)
        #self.BtnGetLastFile.clicked.connect(self.FirstSinalEmit)

        h0layout=QHBoxLayout()
        h0layout.addWidget(self.LabelTime)
        h0layout.addWidget(self.SpinBoxTime)
        h0layout.addWidget(self.BtnGetLastFile)






        vlayout=QVBoxLayout()
        vlayout.addLayout(h0layout)

        MainGrid=QGridLayout()
        MainGrid.addLayout(upgrid,0,0)
        MainGrid.addLayout(vlayout,1,0)
        self.setLayout(MainGrid)


        #self.setWindowIcon(QIcon('image/icon.png'))
        self.setWindowTitle('DFRZ DeployTool')