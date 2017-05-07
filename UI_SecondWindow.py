from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from ConfRead import Conf
import fileinput

class UI_SecondWindow(object):
    def setupUi(self, Form):

        self.ButtonGroup=QButtonGroup()
        SecondGrid=QGridLayout()


        self.CheckBox_0=QCheckBox('WebServer',self)
        self.CheckBox_1=QCheckBox(Conf().ServerPath_Monitor,self)
        self.CheckBox_2=QCheckBox(Conf().ServerPath_Admin,self)
        self.CheckBox_3=QCheckBox(Conf().ServerPath_Cms,self)
        self.CheckBox_4=QCheckBox(Conf().ServerPath_CS,self)
        self.CheckBox_5=QCheckBox(Conf().ServerPath_Event,self)
        self.CheckBox_6=QCheckBox(Conf().ServerPath_glwww,self)
        self.CheckBox_7=QCheckBox(Conf().ServerPath_GqAdmin,self)
        self.CheckBox_8=QCheckBox(Conf().ServerPath_M,self)
        self.CheckBox_9=QCheckBox(Conf().ServerPath_MiRGJ,self)
        self.CheckBox_10=QCheckBox(Conf().ServerPath_MiRZR,self)
        self.CheckBox_11=QCheckBox(Conf().ServerPath_Open,self)
        self.CheckBox_12=QCheckBox(Conf().ServerPath_Resource,self)
        self.CheckBox_13=QCheckBox(Conf().ServerPath_RGJ,self)
        self.CheckBox_14=QCheckBox(Conf().ServerPath_Stock,self)
        self.CheckBox_15=QCheckBox(Conf().ServerPath_StockUserCenter,self)
        self.CheckBox_16=QCheckBox(Conf().ServerPath_Strategy,self)
        self.CheckBox_17=QCheckBox(Conf().ServerPath_UserCenter,self)
        a=2
        b=1
        if b<a:
            self.CheckBox_18=QCheckBox(Conf().ServerPath_WWW,self)
            self.ButtonGroup.addButton(self.CheckBox_18,18)
            SecondGrid.addWidget(self.CheckBox_18,9,1)


        self.CheckBox_50=QCheckBox('ApiServer',self)
        self.CheckBox_51=QCheckBox(Conf().ServerPath_APIGL,self)
        self.CheckBox_52=QCheckBox(Conf().ServerPath_APIGQ,self)
        self.CheckBox_53=QCheckBox(Conf().ServerPath_APIRGJ,self)
        self.CheckBox_53=QCheckBox(Conf().ServerPath_APIRZR,self)




        self.LabelChooseWebSite=QLabel('Please choose the website',self)
        self.LabelWebSiteConf=QLabel('Web站点配置文件名:'+'  '+'WebSite.conf',self)


        self.ButtonGroup.addButton(self.CheckBox_0,0)
        self.ButtonGroup.addButton(self.CheckBox_1,1)
        self.ButtonGroup.addButton(self.CheckBox_2,2)
        self.ButtonGroup.addButton(self.CheckBox_3,3)
        self.ButtonGroup.addButton(self.CheckBox_4,4)
        self.ButtonGroup.addButton(self.CheckBox_5,5)
        self.ButtonGroup.addButton(self.CheckBox_6,6)
        self.ButtonGroup.addButton(self.CheckBox_7,7)
        self.ButtonGroup.addButton(self.CheckBox_8,8)
        self.ButtonGroup.addButton(self.CheckBox_9,9)
        self.ButtonGroup.addButton(self.CheckBox_10,10)
        self.ButtonGroup.addButton(self.CheckBox_11,11)
        self.ButtonGroup.addButton(self.CheckBox_12,12)
        self.ButtonGroup.addButton(self.CheckBox_13,13)
        self.ButtonGroup.addButton(self.CheckBox_14,14)
        self.ButtonGroup.addButton(self.CheckBox_15,15)
        self.ButtonGroup.addButton(self.CheckBox_16,16)
        self.ButtonGroup.addButton(self.CheckBox_17,17)

        self.ButtonGroup.addButton(self.CheckBox_50,50)
        self.ButtonGroup.addButton(self.CheckBox_51,51)
        self.ButtonGroup.addButton(self.CheckBox_52,52)
        self.ButtonGroup.addButton(self.CheckBox_53,53)





        self.ButtonGroup.buttonClicked.connect(self.ButtonJudge)

        self.BtnOK=QPushButton('OK',self)
        self.BtnOK.clicked.connect(self.accept)


        SecondGrid.addWidget(self.CheckBox_0,0,0)
        SecondGrid.addWidget(self.CheckBox_1,1,0)
        SecondGrid.addWidget(self.CheckBox_2,1,1)
        SecondGrid.addWidget(self.CheckBox_3,2,0)
        SecondGrid.addWidget(self.CheckBox_4,2,1)
        SecondGrid.addWidget(self.CheckBox_5,3,0)
        SecondGrid.addWidget(self.CheckBox_6,3,1)
        SecondGrid.addWidget(self.CheckBox_7,4,0)
        SecondGrid.addWidget(self.CheckBox_8,4,1)
        SecondGrid.addWidget(self.CheckBox_9,5,0)
        SecondGrid.addWidget(self.CheckBox_10,5,1)
        SecondGrid.addWidget(self.CheckBox_11,6,0)
        SecondGrid.addWidget(self.CheckBox_12,6,1)
        SecondGrid.addWidget(self.CheckBox_13,7,0)
        SecondGrid.addWidget(self.CheckBox_14,7,1)
        SecondGrid.addWidget(self.CheckBox_15,8,0)
        SecondGrid.addWidget(self.CheckBox_16,8,1)
        SecondGrid.addWidget(self.CheckBox_17,9,0)

        SecondGrid.addWidget(self.CheckBox_50,10,0)
        SecondGrid.addWidget(self.CheckBox_51,11,0)
        SecondGrid.addWidget(self.CheckBox_52,11,1)
        SecondGrid.addWidget(self.CheckBox_53,12,0)

        SecondGrid.addWidget(self.LabelWebSiteConf,14,0)
        SecondGrid.addWidget(self.LabelChooseWebSite,15,0)
        SecondGrid.addWidget(self.BtnOK,16,1)

        self.setLayout(SecondGrid)
        self.setGeometry(300, 300, 800, 600)
        self.setWindowIcon(QIcon('image/icon.png'))
        self.setWindowTitle('DFRZ DeployTool')
