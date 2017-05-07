import sys
import os,datetime,time,fileinput
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from Program import SecondWindow


class UI_SecondTab(object):
    def setupUi(self, Form):
        self.LabelChooseFolder=QLabel('请需要部署的站点文件夹     ')
        self.LineChooseFolder=QLineEdit('',self)
        self.BtnChooseFolder=QPushButton('ChooseFolder',self)
        self.BtnChooseFolder.clicked.connect(self.ButtonChooseFolder)

        maingrid=QGridLayout()
        maingrid.addWidget(self.LabelChooseFolder,0,0)
        maingrid.addWidget(self.LineChooseFolder,0,1)
        maingrid.addWidget(self.BtnChooseFolder,0,2)

        self.LabelWebSiteName=QLabel('请选择站点                     ',self)
        self.LineWebSitePath=QLineEdit('',self)
        self.BtnWebSiteChoose=QPushButton('WebSiteChoose',self)
        self.BtnWebSiteChoose.clicked.connect(self.ShowSecondWindow)

        maingrid.addWidget(self.LabelWebSiteName,1,0)
        maingrid.addWidget(self.LineWebSitePath,1,1)
        maingrid.addWidget(self.BtnWebSiteChoose,1,2)

        self.BtnDeploy=QPushButton('Deploy',self)
        self.BtnDeploy.clicked.connect(self.SecondSingalDeployMsgEmit)

        maingrid.addWidget(self.BtnDeploy,2,2)



        self.setLayout(maingrid)

        self.setGeometry(300, 300, 800, 500)
        #self.setWindowIcon(QIcon('image/icon.png'))
        self.setWindowTitle('DFRZ DeployTool')