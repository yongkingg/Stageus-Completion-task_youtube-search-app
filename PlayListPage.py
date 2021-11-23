from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import QCoreApplication
import Ui
import MyDataBase
import Config
import VideoSearchPage
class PlayListPage:
    def __init__(self,revui,revId):
        self.ui = revui
        self.getIdValue = revId
        self.ui = revui
        self.getSetting = Config.Setting()
        self.db = MyDataBase.MyDataBase() 
        self.getIdValue = revId
        self.getAccontInfor = self.db.read("userInterFace",["id"],[self.getIdValue])

        self.playListCount = 0
        self.playList = []
        self.playlistbtn_play = []
        self.playlistbtn_delete = []
        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.ui.back_playlistpage)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        self.ui.searchvideo_playlistpage.setPlaceholderText("Search the video")
        self.ui.searchvideo_playlistpage.setFont(self.getSetting.search_video_font)

        self.interFaceList = ["Name","Age","Num","TEAM","GRADE"]
        for index in range(0,5):
            if index == 2:
                self.ui.print_infor_playlistpage[index].setText(self.interFaceList[index] + " : " + "0" + str(self.getAccontInfor[0][index+1]))   
            else:
                self.ui.print_infor_playlistpage[index].setText(self.interFaceList[index] + " : " + str(self.getAccontInfor[0][index+1]))  
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
        save_keyword = self.ui.searchvideo_playlistpage.text()
        self.videoSearchPage = VideoSearchPage.VideoSearchPage(self.ui,self.getIdValue,save_keyword)
        self.ui.pageset += 2
        self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
    def enter_search_event(self,event):
        self.ui.button_searchbar_playlistpage[0].setStyleSheet("border-image:url(Pic/SearchBtnEvent.png);")
    def leave_search_event(self,event):
        self.ui.button_searchbar_playlistpage[0].setStyleSheet("border-image:url(Pic/SearchBtn.png);")
    
    def addplaylist_event(self,event):
        self.result = QtWidgets.QDialog()
        self.result.resize(500,200)
        self.message = QtWidgets.QLabel(self.result) 
        self.message.setGeometry(50,20,400,50)
        self.message.setStyleSheet("border : 2px solid black;")
        self.message.setText("Add PlayList?")
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setFont(self.getSetting.findidpw_font)
        # 플레이리스트 이름 
        self.playListName = QtWidgets.QLineEdit(self.result)
        self.playListName.setGeometry(50,100,400,50)
        self.playListName.setStyleSheet("border : 2px solid black;")
        self.playListName.setPlaceholderText("Playlist name : ")
        # 플레이리스트 제작 버튼 
        self.makeBtn = QtWidgets.QPushButton(self.result)
        self.makeBtn.setGeometry(200,160,100,40)
        self.makeBtn.setStyleSheet(
            "border : 2px solid black;"
            "background-color : lightgrey;"
        )
        self.makeBtn.setText("Make")
        self.makeBtn.setFont(self.getSetting.findidpw_font)
        self.makeBtn.clicked.connect(self.makeplaylist_btn)
        self.result.show()

    def makeplaylist_btn(self):
        self.scrollAreaWidgetContents.setGeometry(0,0,1125,120+(self.playListCount*120))
        self.name = self.playListName.text()
        getPlayList = self.db.read("playList",["PlayListName"],[self.name])
        if len(self.name) == 0:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("Please Make Playlist name")
            self.dialog.result.show()  
        elif len(getPlayList) == 1:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("Please change Playlist name")
            self.dialog.result.show() 
        else:
            putPlayList = self.db.create("playList",["PlayListName"],[self.name])
            label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            label.setGeometry(0,0,1125,100)
            label.setStyleSheet("border:2px solid black;")
            label.setMaximumHeight(100)
            label.setMinimumHeight(100)

            self.playList.append(label)
            self.playList[self.playListCount].setText(self.name)
            self.playList[self.playListCount].setAlignment(QtCore.Qt.AlignCenter)
            self.playList[self.playListCount].setFont(self.getSetting.findidpw_font)

            self.makeBtnPlayList(label)

            self.verticalLayout.addWidget(self.playList[self.playListCount])
            self.playListCount += 1
            self.ui.back_playlistpage.setWidget(self.scrollAreaWidgetContents)
        self.result.close()



    def makeBtnPlayList(self, label):
        print(self.playList[self.playListCount])
        print(self.playListCount)

        self.button_play_playlist = QtWidgets.QPushButton(label)
        self.button_play_playlist.setStyleSheet("border-image : url(Pic/Play.png);")
        self.button_play_playlist.setGeometry(950,25,50,50)
        self.playlistbtn_play.append(self.button_play_playlist)
        self.playlistbtn_play[self.playListCount-1].clicked.connect(self.play)

        self.button_delete_playlist = QtWidgets.QPushButton(label)
        self.button_delete_playlist.setStyleSheet("border-image : url(Pic/ErasePlaylist.png);")
        self.button_delete_playlist.setGeometry(1025,25,50,50)
        self.playlistbtn_delete.append(self.button_delete_playlist)
        self.playlistbtn_delete[self.playListCount].clicked.connect(self.delete)

    def play(self):
        self.ui.pageset += 1
        self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
    def delete(self):
        pass












    def enter_plus_event(self,event):
        self.ui.button_searchbar_playlistpage[1].setStyleSheet("border-image:url(Pic/AddPlayListEvent.png);")
    def leave_plus_event(self,event):
        self.ui.button_searchbar_playlistpage[1].setStyleSheet("border-image:url(Pic/AddPlayList.png);")


