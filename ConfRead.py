# http://www.open-open.com/lib/view/open1398169869203.html

import configparser,string, os, sys
from datetime import datetime
from datetime import timedelta



class Conf():
    def __init__(self):
        config= configparser.ConfigParser()
        config.read('web.conf')
        self.GetLastFile_LabelSrc=config.get("GetLastFile","LabelSrc")
        self.GetLastFile_LabelDst=config.get("GetLastFile","LabelDst")
        self.GetLastFile_Src=config.get("GetLastFile","Src")
        self.GetLastFile_Dst=config.get("GetLastFile","Dst")

        self.DeployAndBackup_Src=config.get("DeployAndBackup","Src")

        self.ServerPath_WebServer=config.get("ServerPath","WebServer")
        self.ServerPath_ApiServer=config.get("ServerPath","ApiServer")

        self.ServerPath_Monitor=config.get("ServerPath","Monitor")
        self.ServerPath_Admin=config.get("ServerPath","Admin")
        self.ServerPath_Cms=config.get("ServerPath","Cms")
        self.ServerPath_CS=config.get("ServerPath","CS")
        self.ServerPath_Event=config.get("ServerPath","Event")
        self.ServerPath_glwww=config.get("ServerPath","glwww")
        self.ServerPath_GqAdmin=config.get("ServerPath","Gq.Admin")
        self.ServerPath_M=config.get("ServerPath","M")
        self.ServerPath_MiRGJ=config.get("ServerPath","Mi.RGJ")
        self.ServerPath_MiRZR=config.get("ServerPath","Mi.RZR")
        self.ServerPath_Open=config.get("ServerPath","Open")
        self.ServerPath_Resource=config.get("ServerPath","Resource")
        self.ServerPath_RGJ=config.get("ServerPath","RGJ")
        self.ServerPath_Stock=config.get("ServerPath","Stock")
        self.ServerPath_StockUserCenter=config.get("ServerPath","Stock.UserCenter")
        self.ServerPath_Strategy=config.get("ServerPath","Strategy")
        self.ServerPath_UserCenter=config.get("ServerPath","UserCenter")
        self.ServerPath_WWW=config.get("ServerPath","WWW")

        self.ServerPath_APIGL=config.get("ServerPath","API.GL")
        self.ServerPath_APIGQ=config.get("ServerPath","API.GQ")
        self.ServerPath_APIRGJ=config.get("ServerPath","API.RGJ")
        self.ServerPath_APIRZR=config.get("ServerPath","API.RZR")



#print (Conf().ServerPath_APIRZR)

if __name__ == '__main__':
    config=Conf()
    print (config.ServerPath_APIRZR)









