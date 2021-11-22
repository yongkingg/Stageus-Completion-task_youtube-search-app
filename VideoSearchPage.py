from sys import _xoptions
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QBrush, QImage, QPalette, QPixmap
import Config
import MyDataBase
import pafy
import vlc
import time
import urllib.request
import re
import Config
import PlayVideoThread
class VideoSearchPage:
    def __init__(self,revUi,revId,revKeyWord):
        self.ui = revUi
        self.db = MyDataBase.MyDataBase()
        self.getSetting = Config.Setting()
        self.db = MyDataBase.MyDataBase()
        self.dialog = Config.Dialog()
        self.keyWord = revKeyWord
        self.getIdValue = revId
        self.getAccontInfor = self.db.read("userInterFace",["id"],[self.getIdValue])

        # 인터페이스리스트 적용 X
        self.interFaceList = ["Name","Age","Num","TEAM","GRADE"]
        for index in range(0,5):
            print(self.interFaceList[index] + " : " + str(self.getAccontInfor[0][index+1]))
            if index == 2:
                self.ui.print_infor_videosearchpage[index].setText(self.interFaceList[index] + " : " + "0" + str(self.getAccontInfor[0][index+1]))   
            else:
                self.ui.print_infor_videosearchpage[index].setText(self.interFaceList[index] + " : " + str(self.getAccontInfor[0][index+1]))  
            self.ui.print_infor_videosearchpage[index].setAlignment(QtCore.Qt.AlignCenter)
            self.ui.print_infor_videosearchpage[index].setFont(self.getSetting.login_font_printinfor)

        self.ui.searchvideo_videosearchpage.setPlaceholderText("Search the video")
        self.ui.searchvideo_videosearchpage.setFont(self.getSetting.search_video_font)
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
        self.ui.searchvideo_playlistpage.clear()
        self.ui.searchvideo_videosearchpage.clear()
        self.ui.pageset -= 2
        self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
    def enter_backbtn_event(self,event):
            self.ui.button_videosearchpage[1].setStyleSheet("border-image : url(Pic/BackBtnEvent.png);")
    def leave_backbtn_event(self,event):
            self.ui.button_videosearchpage[1].setStyleSheet("border-image : url(Pic/Back_VideoSearchPage.png);")
    
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
    def videosearch_event(self,event):
        playVideo = PlayVideoThread.VideoThread(self.ui)
        