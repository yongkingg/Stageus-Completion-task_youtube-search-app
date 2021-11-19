from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import QCoreApplication
import Ui
import MyDataBase
import Setting

class PlayListPage:
    def __init__(self,revui,revId):
        self.ui = revui
        self.getSetting = Setting.Setting()
        self.db = MyDataBase.MyDataBase() 
        self.getIdValue = revId
        self.getAccontInfor = self.db.read("userInterFace",["id"],[self.getIdValue])
        print(self.getAccontInfor)

        for index in range(0,5):
            if index == 2:
                self.ui.print_infor_playlistpage[index].setText("0" + str(self.getAccontInfor[0][index+1]))   
            else:
                self.ui.print_infor_playlistpage[index].setText(str(self.getAccontInfor[0][index+1]))  
            self.ui.print_infor_playlistpage[index].setAlignment(QtCore.Qt.AlignCenter)
            self.ui.print_infor_playlistpage[index].setFont(self.getSetting.login_font_printinfor)


        # 돋보기 버튼 이벤트
        self.ui.button_searchbar_playlistpage[0].mousePressEvent = lambda event: self.videosearch_event(event)
        self.ui.button_searchbar_playlistpage[0].enterEvent = lambda event: self.enter_search_event(event)
        self.ui.button_searchbar_playlistpage[0].leaveEvent = lambda event: self.leave_search_event(event)
        # 플러스 버튼 이벤트
        self.ui.button_searchbar_playlistpage[1].mousePressEvent = lambda event: self.addplaylist_event(event)
        self.ui.button_searchbar_playlistpage[1].enterEvent = lambda event: self.enter_plus_event(event)
        self.ui.button_searchbar_playlistpage[1].leaveEvent = lambda event: self.leave_plus_event(event)
        # update, logout 이벤트
        for index in range(0,2):
            if index == 0:
                self.ui.button_playlistpage[index].mousePressEvent = lambda event, num = index: self.update_event(event, num)
            else:
                self.ui.button_playlistpage[index].mousePressEvent = lambda event, num = index: self.logout_event(event, num)
            self.ui.button_playlistpage[index].enterEvent = lambda event, num = index: self.enter_button_event(event,num)
            self.ui.button_playlistpage[index].leaveEvent = lambda event, num = index: self.leave_button_event(event,num)







    
    def enter_button_event(self,event,index):
        self.ui.button_playlistpage[index].setStyleSheet("border-image : '';"
                "background-color : black;"   
                "color : white;" 
                "border : 4px solid black;"
            )
    def leave_button_event(self,event,index):
        self.ui.button_playlistpage[index].setStyleSheet("border-image : '';"
                "background-color : darkgrey;"    
                "border : 4px solid black;"
            )
    def update_event(self,event,index):
        self.ui.pageset += 5
        self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
        
    def logout_event(self,event,index):
        self.ui.pageset -= 1
        self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
        for index in range(0,2):
            self.ui.inputIDPW[index].clear()
    def videosearch_event(self,event):
        self.ui.pageset += 2
        self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
    def enter_search_event(self,event):
        self.ui.button_searchbar_playlistpage[0].setStyleSheet("border-image:url(Pic/SearchBtnEvent.png);")
    def leave_search_event(self,event):
        self.ui.button_searchbar_playlistpage[0].setStyleSheet("border-image:url(Pic/SearchBtn.png);")
    def addplaylist_event(self,event):
        pass
    def enter_plus_event(self,event):
        self.ui.button_searchbar_playlistpage[1].setStyleSheet("border-image:url(Pic/AddPlayListEvent.png);")
    def leave_plus_event(self,event):
        self.ui.button_searchbar_playlistpage[1].setStyleSheet("border-image:url(Pic/AddPlayList.png);")
