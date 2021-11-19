from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import QCoreApplication
import Ui
import MyDataBase

class VideoSearchPage:
    def __init__(self,revui):
        self.ui = revui
        self.db = MyDataBase.MyDataBase()
        # 돋보기 버튼 이벤트
        self.ui.button_searchbar_videosearchpage[0].mousePressEvent = lambda event: self.videosearch_event(event)
        self.ui.button_searchbar_videosearchpage[0].enterEvent = lambda event: self.enter_search_event(event)
        self.ui.button_searchbar_videosearchpage[0].leaveEvent = lambda event: self.leave_search_event(event)
        # 플러스 버튼 이벤트
        self.ui.button_searchbar_videosearchpage[1].mousePressEvent = lambda event: self.addplaylist_event(event)
        self.ui.button_searchbar_videosearchpage[1].enterEvent = lambda event: self.enter_plus_event(event)
        self.ui.button_searchbar_videosearchpage[1].leaveEvent = lambda event: self.leave_plus_event(event)
        #뒤로가기
        self.ui.button_videosearchpage[1].mousePressEvent = lambda event: self.back_event(event)
        self.ui.button_videosearchpage[1].enterEvent = lambda event: self.enter_backbtn_event(event)
        self.ui.button_videosearchpage[1].leaveEvent = lambda event: self.leave_backbtn_event(event)
       # 업데이트
        self.ui.button_videosearchpage[0].mousePressEvent = lambda event: self.update_event(event)
        self.ui.button_videosearchpage[0].enterEvent = lambda event: self.enter_updatebtn_event(event)
        self.ui.button_videosearchpage[0].leaveEvent = lambda event: self.leave_updatebtn_event(event)


    def update_event(self,event):
        self.ui.pageset += 3
        self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
        
    def enter_updatebtn_event(self,event):
        self.ui.button_videosearchpage[0].setStyleSheet(
                "border-image : '';"
                "background-color : black;"    
                "border : 4px solid black;"
                "Color : white;"
            )
    def leave_updatebtn_event(self,event):
        self.ui.button_videosearchpage[0].setStyleSheet(
                "border-image : '';"
                "background-color : grey;"    
                "border : 4px solid black;"
            )
    def back_event(self,event):
        self.ui.pageset -= 2
        self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
    def enter_backbtn_event(self,event):
            self.ui.button_videosearchpage[1].setStyleSheet("border-image : url(Pic/BackBtnEvent.png);")
    def leave_backbtn_event(self,event):
            self.ui.button_videosearchpage[1].setStyleSheet("border-image : url(Pic/Back_VideoSearchPage.png);")
    def videosearch_event(self,event):
        # self.ui.pageset -= 2
        # self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
        pass
    def enter_search_event(self,event):
        self.ui.button_searchbar_videosearchpage[0].setStyleSheet("border-image:url(Pic/SearchBtnEvent.png);")
    def leave_search_event(self,event):
        self.ui.button_searchbar_videosearchpage[0].setStyleSheet("border-image:url(Pic/SearchBtn.png);")
    def addplaylist_event(self,event):
        pass
    def enter_plus_event(self,event):
        self.ui.button_searchbar_videosearchpage[1].setStyleSheet("border-image:url(Pic/AddPlayListEvent.png);")
    def leave_plus_event(self,event):
        self.ui.button_searchbar_videosearchpage[1].setStyleSheet("border-image:url(Pic/AddPlayList.png);")
