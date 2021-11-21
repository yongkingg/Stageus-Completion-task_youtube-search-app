from sys import _xoptions
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QBrush, QImage, QPalette, QPixmap
import Config
import MyDataBase

class ManageInforPage:
    def __init__(self,revUi,revId):
        self.ui = revUi
        self.getIdValue = revId
        self.db = MyDataBase.MyDataBase()
        self.getAccontInfor = self.db.read("userInterFace",["id"],[self.getIdValue])

        self.getSetting = Config.Setting()
        self.db = MyDataBase.MyDataBase()
      
        

        # Back 이벤트
        self.ui.button_back_manageinforpage.mousePressEvent = lambda event: self.back_event(event)
        self.ui.button_back_manageinforpage.enterEvent = lambda event: self.enter_backbtn_event(event)
        self.ui.button_back_manageinforpage.leaveEvent = lambda event: self.leave_backbtn_event(event)



    def back_event(self,event):      
        self.ui.pageset -= 5
        self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)

    def enter_backbtn_event(self,event):
        self.ui.button_back_manageinforpage.setStyleSheet("border-image : url(Pic/BackBtnEvent.png);")

    def leave_backbtn_event(self,event):
        self.ui.button_back_manageinforpage.setStyleSheet("border-image : url(Pic/Back_VideoSearchPage.png);")

    def update_event(self,event):
        pass
    def enter_updatebtn_event(self,event):
        self.ui.button_manageinforpage.setStyleSheet(
                "border-image : '';"
                "background-color : black;"    
                "border : 4px solid black;"
                "Color : white;"
            )
    def leave_updatebtn_event(self,event):
        self.ui.button_manageinforpage.setStyleSheet(
                "border-image : '';"
                "background-color : grey;"    
                "border : 4px solid black;"
            )

