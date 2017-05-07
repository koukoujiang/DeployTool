import sys,os,shutil,logging
import os,datetime,time,fileinput
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from UI_FirstTab import UI_FirstTab
from UI_SecondTab import UI_SecondTab
from UI_SecondWindow import  UI_SecondWindow
from UI_ThirdTab import UI_ThirdTab
from UI_FouthTab import UI_FouthTab
from UI_FifthTab import UI_FifthTab
from ConfRead import Conf

global logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)
if not os.path.exists('Log'):
    os.makedirs('Log')
fh = logging.FileHandler('Log/%s.log' % (datetime.datetime.now().strftime("%Y%m%d")))
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)



class TabDialog(QWidget):
    def __init__(self):
        super().__init__()
        global  logger
        self.FirstTab=FirstTab()
        self.SecondTab=SecondTab()
        self.ThirdTab=ThirdTab()
        self.FouthTab=FouthTab()
        self.FifthTab=FifthTab()
        self.FirstTab.FirstSingalShowMsg.connect(self.ButtonGetLastFile)
        self.SecondTab.SecondSingalDeployMsg.connect(self.BtnDeployFile)
        self.ThirdTab.ThirdSingalZipFile.connect(self.ButtonZipFile)
        self.FouthTab.FouthSingalFileCompare.connect(self.ButtonFileCompare)



        tabWidget = QTabWidget()
        tabWidget.addTab(self.FirstTab, '获取最新文件')
        tabWidget.addTab(self.SecondTab, '部署并备份')
        tabWidget.addTab(self.ThirdTab,'打包文件')
        tabWidget.addTab(self.FouthTab,'文本差分')
        tabWidget.addTab(self.FifthTab,'读取文件列表')


        self.TextInfo=QTextEdit('',self)
        self.TextInfo.setReadOnly(True)



        mainLayout = QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        mainLayout.addWidget(self.TextInfo)
        self.setLayout(mainLayout)

        self.setGeometry(300, 300, 800, 500)
        self.setWindowIcon(QIcon('image/icon.png'))
        self.setWindowTitle("DFRZ DeployTool")



        self.WebSiteDict={}
        for line in fileinput.input('WebSiteNameConvert'):
            line=line=line.strip('\n').split('#')
            self.WebSiteDict[line[0]]=line[1]





#提取最新时间内文件，并判断是否要用关键字
    def ButtonGetLastFile(self):
        Delaytime=(datetime.datetime.now()- datetime.timedelta(hours=self.FirstTab.SpinBoxTime.value())).strftime("%Y-%m-%d %H:%M:%S") #延迟时间
        KeyWordFile=self.FirstTab.LineKeyFile.text().split(',')
        for root, dirs, files in os.walk(self.FirstTab.LineSrc.text()):
            for file in files:
                SrcFile=os.path.join(root,file).replace('\\','/')
                DstFile=(self.FirstTab.LineDst.text()+'/'+(((root.split('/'))[-1]).split('\\'))[0]+SrcFile[len(self.FirstTab.LineSrc.text()):]).replace('\\','/')
                DstPath=self.FirstTab.LineDst.text()+'/'+(((root.split('/'))[-1]).split('\\'))[0]+root[len(self.FirstTab.LineSrc.text()):].replace('\\','/')
                filetime=os.path.getmtime(os.path.join(root,file))
                filetime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(filetime))
                if Delaytime<filetime:
                    if self.FirstTab.CheckBoxKeyFile.isChecked():
                        if file in KeyWordFile:
                            if not os.path.exists(DstPath):
                                os.makedirs(DstPath)
                            self.TextInfo.append(DstFile)
                            logger.info('获取最新文件：'+DstFile)
                            shutil.copy2(SrcFile,DstFile)
                    else:
                        if not os.path.exists(DstPath):
                            os.makedirs(DstPath)
                        self.TextInfo.append(DstFile)
                        logger.info('获取最新文件：'+DstFile)
                        shutil.copy2(SrcFile,DstFile)
        self.TextInfo.append('Finish........')
        logger.info('Finish........')



    def BtnDeployFile(self):
        now= datetime.datetime.now().strftime("%Y%m%d")
        BackupPath='D:/backup/'+ str(now)+'/'+self.SecondTab.LineWebSitePath.text().split('/')[-1]
        try:
            for root, dirs, files in os.walk(self.SecondTab.LineChooseFolder.text()):
                for file in files:
                    SrcFile=os.path.join(root,file).replace('\\','/')
                    DstFile=self.SecondTab.LineWebSitePath.text()+SrcFile[len(self.SecondTab.LineChooseFolder.text()):]
                    DstPath=(self.SecondTab.LineWebSitePath.text()+root[len(self.SecondTab.LineChooseFolder.text()):]).replace('\\','/')
                    DstBackFile= BackupPath + SrcFile[len(self.SecondTab.LineChooseFolder.text()):]
                    DstBackPath=(BackupPath+ root[len(self.SecondTab.LineChooseFolder.text()):]).replace('\\','/')
                    if not os.path.exists(DstFile):
                        if not os.path.exists(DstPath):
                            os.makedirs(DstPath)
                        self.TextInfo.append('文件已被更新：  '+DstFile)
                        logger.info('文件已被更新：  '+DstFile)
                        shutil.copy2(SrcFile,DstFile)
                    else:
                        if not os.path.exists(DstBackPath):
                            os.makedirs(DstBackPath)
                        shutil.copy2(DstFile,DstBackFile)
                        if not os.path.exists(DstPath):
                            os.makedirs(DstPath)
                        self.TextInfo.append('文件已被更新：  '+DstFile)
                        logger.info('文件已被更新：  '+DstFile)
                        shutil.copy2(SrcFile,DstFile)
            self.TextInfo.append('部署完成.......'+'备份文件路径：  '+BackupPath + '  (只备份被覆盖的文件)')
            logger.info('部署完成.......'+'备份文件路径：  '+BackupPath + '  (只备份被覆盖的文件)')
        except:
            reply = QMessageBox.question(self, '错误警告','请确认路径是否正确', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)



    def ButtonZipFile(self):
        shutil.rmtree('D:/website/')
        SrcPath=self.ThirdTab.LinePath.text().replace('/','\\')
        if self.ThirdTab.CheckBox_0.isChecked():
            os.system("echo D|xcopy /s /Y  %s\%s D:\\website\%s" %(SrcPath,self.ThirdTab.CheckBox_0.text(),self.ThirdTab.CheckBox_0.text()))
        if self.ThirdTab.CheckBox_1.isChecked():
            os.system("echo D|xcopy /s /Y  %s\%s D:\\website\%s" %(SrcPath,self.ThirdTab.CheckBox_1.text(),self.ThirdTab.CheckBox_1.text()))
        if self.ThirdTab.CheckBox_2.isChecked():
            os.system("echo D|xcopy /s /Y  %s\%s D:\\website\%s" %(SrcPath,self.ThirdTab.CheckBox_2.text(),self.ThirdTab.CheckBox_2.text()))
        if self.ThirdTab.CheckBox_3.isChecked():
            os.system("echo D|xcopy /s /Y  %s\%s D:\\website\%s" %(SrcPath,self.ThirdTab.CheckBox_3.text(),self.ThirdTab.CheckBox_3.text()))
        if self.ThirdTab.CheckBox_4.isChecked():
            os.system("echo D|xcopy /s /Y  %s\%s D:\\website\%s" %(SrcPath,self.ThirdTab.CheckBox_4.text(),self.ThirdTab.CheckBox_4.text()))
        if self.ThirdTab.CheckBox_5.isChecked():
            os.system("echo D|xcopy /s /Y  %s\%s D:\\website\%s" %(SrcPath,self.ThirdTab.CheckBox_5.text(),self.ThirdTab.CheckBox_5.text()))
        if self.ThirdTab.CheckBox_6.isChecked():
            os.system("echo D|xcopy /s /Y  %s\%s D:\\website\%s" %(SrcPath,self.ThirdTab.CheckBox_6.text(),self.ThirdTab.CheckBox_6.text()))
        if self.ThirdTab.CheckBox_7.isChecked():
            os.system("echo D|xcopy /s /Y  %s\%s D:\\website\%s" %(SrcPath,self.ThirdTab.CheckBox_7.text(),self.ThirdTab.CheckBox_7.text()))
        if self.ThirdTab.CheckBox_8.isChecked():
            os.system("echo D|xcopy /s /Y  %s\%s D:\\website\%s" %(SrcPath,self.ThirdTab.CheckBox_8.text(),self.ThirdTab.CheckBox_8.text()))
        if self.ThirdTab.CheckBox_9.isChecked():
            os.system("echo D|xcopy /s /Y  %s\%s D:\\website\%s" %(SrcPath,self.ThirdTab.CheckBox_9.text(),self.ThirdTab.CheckBox_9.text()))

        for Name in os.listdir('D:/website/'):
                if Name in self.WebSiteDict.keys():
                    newName=Name.replace(Name,self.WebSiteDict[Name])
                    os.rename(os.path.join('D:/website/', Name), os.path.join('D:/website/', newName))
                    self.TextInfo.append('文件夹：'+Name+'  打包时，文件名已经替换为'  + newName)
                    logger.info('文件夹：'+Name+'  打包时，文件名已经替换为'  + newName)
                else:
                    self.TextInfo.append('文件夹：'+Name +'没有在自定义文件WebSiteNameConvert中找到，请确认是否正确')
                    logger.info('文件夹：'+Name +'没有在自定义文件WebSiteNameConvert中找到，请确认是否正确')
        if os.path.exists( 'D:/%s.zip' %self.ThirdTab.LineZipFileName.text()):
                os.remove('D:/%s.zip' %self.ThirdTab.LineZipFileName.text())

        os.system("C:/Progra~1/WinRAR/WinRAR a D:\\%s.zip D:\\website" %self.ThirdTab.LineZipFileName.text())
        self.TextInfo.append('打包完成')
        logger.info('打包完成')




    def ButtonFileCompare(self):
        DataA=[];DataB=[]
        try:
            for line in fileinput.input(self.FouthTab.LineSrc.text()):
                DataA.append(line.strip('\n'))
            for line in fileinput.input(self.FouthTab.LineDst.text()):
                DataB.append(line.strip('\n'))
            self.TextInfo.append('文件： '+self.FouthTab.LineDst.text() +'  新web.conf增加了：')
            for m in list(set(DataB).difference(set(DataA))):
                if m:
                    self.TextInfo.append(m)
            self.TextInfo.append('文件： '+self.FouthTab.LineSrc.text()+'   新web.conf删除了：')
            for m in list(set(DataA).difference(set(DataB))):
                if m:
                    self.TextInfo.append(m)
        except:
            reply = QMessageBox.question(self, '错误警告','文件编码无法识别', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)



class FirstTab(QWidget,UI_FirstTab):
    FirstSingalShowMsg=pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def ButtonSrcShowDialog(self):
        fname = QFileDialog.getExistingDirectory(self, 'Open file',Conf().GetLastFile_Src)
        self.LineSrc.setText(fname)

    def ButtonDstShowDialog(self):
        fname = QFileDialog.getExistingDirectory(self, 'Open file',Conf().GetLastFile_Dst)
        self.LineDst.setText(fname)

    def FirstSinalEmit(self):
        self.FirstSingalShowMsg.emit()

class SecondTab(QWidget,UI_SecondTab):
    SecondSingalShowMsg=pyqtSignal()
    SecondSingalDeployMsg=pyqtSignal()
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.SecondWindow=SecondWindow()
        self.SecondWindow.SecondWindowSingalGetSiteName.connect(self.GetWebSitePath)

    def SecondSingalShowMsgeEmit(self):
        self.SecondSingalShowMsg.emit()

    def SecondSingalDeployMsgEmit(self):
        self.SecondSingalDeployMsg.emit()

    def ButtonChooseFolder(self):
        fname=QFileDialog.getExistingDirectory(self,'Open file',Conf().DeployAndBackup_Src)
        self.LineChooseFolder.setText(fname)

    def ShowSecondWindow(self):
        self.SecondWindow.show()
        self.SecondWindow.exec_()

    def GetWebSitePath(self):
        self.LineWebSitePath.clear()
        self.LineWebSitePath.insert(self.SecondWindow.LabelChooseWebSite.text().replace('\\','/'))


class SecondWindow(QDialog,UI_SecondWindow):
    SecondWindowSingalGetSiteName=pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.BtnOK.clicked.connect(self.SecondWindowSingalEmit)

    def SecondWindowSingalEmit(self):
        self.SecondWindowSingalGetSiteName.emit()

    def ButtonJudge(self):
        if self.ButtonGroup.checkedId() == 0:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer)
        elif self.ButtonGroup.checkedId() == 1:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_Monitor)
        elif self.ButtonGroup.checkedId()== 2:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_Admin)
        elif self.ButtonGroup.checkedId()== 3:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_Cms)
        elif self.ButtonGroup.checkedId()== 4:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_CS)
        elif self.ButtonGroup.checkedId()== 5:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_Event)
        elif self.ButtonGroup.checkedId()== 6:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_glwww)
        elif self.ButtonGroup.checkedId()== 7:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_GqAdmin)
        elif self.ButtonGroup.checkedId()== 8:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_M)
        elif self.ButtonGroup.checkedId()== 9:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_MiRGJ)
        elif self.ButtonGroup.checkedId()== 10:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_MiRZR)
        elif self.ButtonGroup.checkedId()== 11:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_Open)
        elif self.ButtonGroup.checkedId()== 12:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_Resource)
        elif self.ButtonGroup.checkedId()== 13:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_RGJ)
        elif self.ButtonGroup.checkedId()== 14:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_Stock)
        elif self.ButtonGroup.checkedId()== 15:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_StockUserCenter)
        elif self.ButtonGroup.checkedId()== 16:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_Strategy)
        elif self.ButtonGroup.checkedId()== 17:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_UserCenter)
        elif self.ButtonGroup.checkedId()== 18:
            self.LabelChooseWebSite.setText(Conf().ServerPath_WebServer+Conf().ServerPath_WWW)
        elif self.ButtonGroup.checkedId()== 50:
            self.LabelChooseWebSite.setText(Conf().ServerPath_ApiServer)
        elif self.ButtonGroup.checkedId()== 51:
            self.LabelChooseWebSite.setText(Conf().ServerPath_ApiServer+Conf().ServerPath_APIGL)
        elif self.ButtonGroup.checkedId()== 52:
            self.LabelChooseWebSite.setText(Conf().ServerPath_ApiServer+Conf().ServerPath_APIGQ)
        elif self.ButtonGroup.checkedId()== 53:
            self.LabelChooseWebSite.setText(Conf().ServerPath_ApiServer+Conf().ServerPath_APIRGJ)
        elif self.ButtonGroup.checkedId()== 54:
            self.LabelChooseWebSite.setText(Conf().ServerPath_ApiServer+Conf().ServerPath_APIRZR)


class ThirdTab(QWidget,UI_ThirdTab):
    ThirdSingalZipFile=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def ThirdSingalZipFileEmit(self):
        self.ThirdSingalZipFile.emit()

    def ButtonGetFolderName(self):
        fname = QFileDialog.getExistingDirectory(self, 'Open file','D:/')
        self.LinePath.setText(fname)
        self.FolderNameData=[]
        self.FolderNameData=['NoSite','NoSite','NoSite','NoSite','NoSite','NoSite','NoSite','NoSite','NoSite','NoSite']
        i=0
        try:
            if fname:
                for s in os.listdir(fname):
                    self.FolderNameData[i]=s
                    i+=1
                self.CheckBox_0.setText(self.FolderNameData[0])
                self.CheckBox_1.setText(self.FolderNameData[1])
                self.CheckBox_2.setText(self.FolderNameData[2])
                self.CheckBox_3.setText(self.FolderNameData[3])
                self.CheckBox_4.setText(self.FolderNameData[4])
                self.CheckBox_5.setText(self.FolderNameData[5])
                self.CheckBox_6.setText(self.FolderNameData[6])
                self.CheckBox_7.setText(self.FolderNameData[7])
                self.CheckBox_8.setText(self.FolderNameData[8])
                self.CheckBox_9.setText(self.FolderNameData[9])
            else:
                pass
        except:
            reply = QMessageBox.question(self, '错误警告','目录数目过大，请重新选择', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

class FouthTab(QWidget,UI_FouthTab):
    FouthSingalFileCompare=pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def FouthSingalFileCompareEmit(self):
        self.FouthSingalFileCompare.emit()

    def ButtonSrcShowDialog(self):
        filename,filetype = QFileDialog.getOpenFileName(self,'Open File','D:/', "All Files (*)")
        self.LineSrc.setText(filename)

    def ButtonDstShowDialog(self):
        filename,filetype = QFileDialog.getOpenFileName(self,'Open File','D:/', "All Files (*)")
        self.LineDst.setText(filename)

class FifthTab(QWidget,UI_FifthTab):
    def __init__(self):
        super().__init__()
        self.setupUi(self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    tabdialog = TabDialog()
    tabdialog.show()
    sys.exit(app.exec_())
