from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import QCoreApplication
import Ui
import MyDataBase
import Setting


class ManageInforPage:
    def __init__(self,revui):
        self.ui = revui
        self.db = MyDataBase.MyDataBase()
        # 돋보기, 재생목록 추가 버튼 비활성화
        self.ui.button_searchbar_manageinforpage[0].setStyleSheet("border-image:url(Pic/SearchBtnEvent.png);")
        self.ui.button_searchbar_manageinforpage[1].setStyleSheet("border-image:url(Pic/AddPlayListEvent.png);")
        self.ui.button_searchbar_manageinforpage[0].setDisabled(True)
        self.ui.button_searchbar_manageinforpage[1].setDisabled(True)
        # Back 이벤트
        self.ui.button_back_manageinforpage.mousePressEvent = lambda event: self.back_event(event)
        self.ui.button_back_manageinforpage.enterEvent = lambda event: self.enter_backbtn_event(event)
        self.ui.button_back_manageinforpage.leaveEvent = lambda event: self.leave_backbtn_event(event)
        # update 버튼 이벤트
        self.ui.button_manageinforpage.mousePressEvent = lambda event: self.update_event(event)
        self.ui.button_manageinforpage.enterEvent = lambda event: self.enter_updatebtn_event(event)
        self.ui.button_manageinforpage.leaveEvent = lambda event: self.leave_updatebtn_event(event)



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

