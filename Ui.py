from sys import _xoptions
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QBrush, QImage, QPalette, QPixmap
import Setting

# 이미지 경로 하는 방법 - 절대경로
# self.a = QtWidgets.QLabel(self.StartPage)
# self.a.setGeometry(QtCore.QRect(560, 390, 500, 500))
# pm = QtGui.QPixmap("C:\\Users\\dydwn\\OneDrive\\바탕 화면\\PYTHON\\8주차\\과제\\Pic\\SET.PNG")
# self.a.setPixmap(pm)

# 이미지 경로 하는 방법 - 상대경로
# self.a = QtWidgets.QLabel(self.StartPage)
# self.a.setGeometry(QtCore.QRect(560, 390, 500, 500))
# pm = QtGui.QPixmap("Pic\StartPage.PNG")
# self.a.setPixmap(pm)

class Ui:
    def __init__(self):
        self.pageset = 0
        # 세팅 가져옴
        self.getSetting = Setting.Setting()
        # 메인윈도우 형성
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindow.resize(1600,900)
        self.mainWindow.setMinimumSize(QtCore.QSize(1600,900))
        self.mainWindow.setMaximumSize(QtCore.QSize(1600,900))
        self.mainWindow.setWindowTitle("YONGTUBE")
        # 센트럴 위젯 형성
        self.centralWidget = QtWidgets.QWidget(self.mainWindow)
        self.centralWidget.setGeometry(0,0,1000,620)
        self.centralWidget.setMinimumSize(QtCore.QSize(1600, 900))
        self.centralWidget.setMaximumSize(QtCore.QSize(1600, 900)) 
        # 스택위젯 형성
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.stackedWidget.setMinimumSize(QtCore.QSize(1600, 900))
        self.stackedWidget.setMaximumSize(QtCore.QSize(1600, 900))
    # 시작 페이지 0 
        self.StartPage = QtWidgets.QWidget()
        self.StartPage.setMinimumSize(QtCore.QSize(1600, 900))
        self.StartPage.setMaximumSize(QtCore.QSize(1600, 900))
        self.StartPage.setStyleSheet("border-image:url(Pic/StartPage.png);")
        self.stackedWidget.addWidget(self.StartPage)
    # 재생목록 페이지 1
        self.PlayListPage = QtWidgets.QWidget()
        self.PlayListPage.setMinimumSize(QtCore.QSize(1600, 900))
        self.PlayListPage.setMaximumSize(QtCore.QSize(1600, 900))
        self.PlayListPage.setStyleSheet("border-image:url(Pic/PlayListPage.png);")
        self.stackedWidget.addWidget(self.PlayListPage)
    # 영상 재생 페이지 2
        self.VideoPage = QtWidgets.QWidget()
        self.VideoPage.setMinimumSize(QtCore.QSize(1600, 900))
        self.VideoPage.setMaximumSize(QtCore.QSize(1600, 900))
        self.VideoPage.setStyleSheet("border-image:url(Pic/VideoPage.png);")
        self.stackedWidget.addWidget(self.VideoPage)
    # 영상 검색 페이지 3
        self.VideoSearchPage = QtWidgets.QWidget()
        self.VideoSearchPage.setMinimumSize(QtCore.QSize(1600, 900))
        self.VideoSearchPage.setMaximumSize(QtCore.QSize(1600, 900))
        self.VideoSearchPage.setStyleSheet("border-image:url(Pic/VideoSearchPage.png);")
        self.stackedWidget.addWidget(self.VideoSearchPage)
    # 아이디/비밀번호 찾기 페이지 4
        self.FindAccountPage = QtWidgets.QWidget()
        self.FindAccountPage.setMinimumSize(QtCore.QSize(1600, 900))
        self.FindAccountPage.setMaximumSize(QtCore.QSize(1600, 900))
        self.FindAccountPage.setStyleSheet("border-image:url(Pic/FindAccountPage.png);")
        self.stackedWidget.addWidget(self.FindAccountPage)
    # 회원가입페이지 5
        self.MakeAccountPage = QtWidgets.QWidget()
        self.MakeAccountPage.setMinimumSize(QtCore.QSize(1600, 900))
        self.MakeAccountPage.setMaximumSize(QtCore.QSize(1600, 900))
        self.MakeAccountPage.setStyleSheet("border-image:url(Pic/MakeManageID.png);")
        self.stackedWidget.addWidget(self.MakeAccountPage)
    # 계정 관리 창 6
        self.ManageInforPage = QtWidgets.QWidget()
        self.ManageInforPage.setMinimumSize(QtCore.QSize(1600, 900))
        self.ManageInforPage.setMaximumSize(QtCore.QSize(1600, 900))
        self.ManageInforPage.setStyleSheet("border-image:url(Pic/MakeManageID.png);")
        self.stackedWidget.addWidget(self.ManageInforPage)

        # 아이디 비밀번호 입력
        self.inputIDPW = []  # (0.아이디 입력 1.비밀번호 입력)
        for index in range(0,2):
            tmpSpace = QtWidgets.QLineEdit(self.StartPage)
            yPos = 500 + (120*index)
            tmpSpace.setGeometry(400,yPos,600,100)
            tmpSpace.setFont(self.getSetting.login_font)
            self.inputIDPW.append(tmpSpace)
            self.inputIDPW[index].setStyleSheet(
                "border-image : '';"
                "background-color : lightgrey;"    
                "border : 2px solid black;"
            )
        self.inputIDPW[1].setEchoMode(2)

        # 0. 로그인 버튼 1.회원가입 2.아이디/비밀번호 찾기
        self.button_startpage = []
        for index in range(0,3):
            tmpBtn = QtWidgets.QPushButton(self.StartPage)
            if index == 0:
                xPos = 1020
                yPos = 500
                xLength = 220
                yLength = 220
            else:
                xPos = 430 + (465*(index-1))
                yPos = 727
                xLength = 30
                yLength = 30
            tmpBtn.setGeometry(xPos,yPos,xLength,yLength)
            tmpBtn.setFont(self.getSetting.login_font)
            self.button_startpage.append(tmpBtn)
            if index == 0:
                self.button_startpage[index].setText("LOGIN")
            self.button_startpage[index].setStyleSheet(
                "border-image : '';"
                "background-color : lightgrey;"    
                "border : 2px solid black;"
            )

        # 정보출력 - 플레이리스트 페이지 ( 0. 이름 1.나이 2.전화번호3.팀4.직급)
        self.print_infor_playlistpage = []
        for index in range(0,5):
            tmpSpace = QtWidgets.QLabel(self.PlayListPage)
            if index == 0 :
                xPos = 160
                yPos = 425
                xlength = 200
            elif index == 1:
                xPos = 135
                yPos = 490
                xlength = 225
            elif index == 2:
                xPos = 140
                yPos = 565
                xlength = 220
            elif index == 3:
                xPos = 155
                yPos = 645
                xlength = 205
            elif index == 4:
                xPos = 170
                yPos = 720
                xlength = 190
            tmpSpace.setGeometry(xPos,yPos,xlength,50)
            tmpSpace.setStyleSheet("border-image : '';"
                "Color : Black;"
            )
            self.print_infor_playlistpage.append(tmpSpace)

            # 정보출력 - 영상검색페이지
        self.print_infor_searchvideopage = []
        for index in range(0,5):
            tmpSpace = QtWidgets.QLabel(self.VideoSearchPage)
            if index == 0 :
                xPos = 160
                yPos = 425
                xlength = 200
            elif index == 1:
                xPos = 135
                yPos = 490
                xlength = 225
            elif index == 2:
                xPos = 140
                yPos = 565
                xlength = 220
            elif index == 3:
                xPos = 155
                yPos = 645
                xlength = 205
            elif index == 4:
                xPos = 170
                yPos = 720
                xlength = 190
            tmpSpace.setGeometry(xPos,yPos,xlength,50)
            tmpSpace.setStyleSheet("border-image : '';"
                    "Color : Black;"
            )
            self.print_infor_searchvideopage.append(tmpBtn)

            # 정보출력 - 아이디/비밀번호 찾기 페이지
        self.print_infor_findaccountpage = []
        for index in range(0,5):
            tmpSpace = QtWidgets.QLabel(self.FindAccountPage)
            if index == 0 :
                xPos = 160
                yPos = 425
                xlength = 200
            elif index == 1:
                xPos = 135
                yPos = 490
                xlength = 225
            elif index == 2:
                xPos = 140
                yPos = 565
                xlength = 220
            elif index == 3:
                xPos = 155
                yPos = 645
                xlength = 205
            elif index == 4:
                xPos = 170
                yPos = 720
                xlength = 190
            tmpSpace.setGeometry(xPos,yPos,xlength,50)
            tmpSpace.setStyleSheet("border-image : '';"
                "Color : Black;"
            )
            self.print_infor_findaccountpage.append(tmpBtn)

            # 정보출력 - 회원가입 페이지
        self.print_infor_makeaccountpage = []
        for index in range(0,5):
            tmpSpace = QtWidgets.QLabel(self.MakeAccountPage)
            if index == 0 :
                xPos = 160
                yPos = 425
                xlength = 200
            elif index == 1:
                xPos = 135
                yPos = 490
                xlength = 225
            elif index == 2:
                xPos = 140
                yPos = 565
                xlength = 220
            elif index == 3:
                xPos = 155
                yPos = 645
                xlength = 205
            elif index == 4:
                xPos = 170
                yPos = 720
                xlength = 190
            tmpSpace.setGeometry(xPos,yPos,xlength,50)
            tmpSpace.setStyleSheet("border-image : '';"
                "Color : Black;"
            )
            self.print_infor_makeaccountpage.append(tmpBtn)

            # 정보출력 - 회원정보수정 페이지
        self.print_infor_manageinforpage = []
        for index in range(0,5):
            tmpSpace = QtWidgets.QLabel(self.ManageInforPage)
            if index == 0 :
                xPos = 160
                yPos = 425
                xlength = 200
            elif index == 1:
                xPos = 135
                yPos = 490
                xlength = 225
            elif index == 2:
                xPos = 140
                yPos = 565
                xlength = 220
            elif index == 3:
                xPos = 155
                yPos = 645
                xlength = 205
            elif index == 4:
                xPos = 170
                yPos = 720
                xlength = 190
            tmpSpace.setGeometry(xPos,yPos,xlength,50)
            tmpSpace.setStyleSheet("border-image : '';"
                "Color : Black;"
            )
            self.print_infor_manageinforpage.append(tmpBtn)





        # 영상 검색 창
        self.searchvideo_playlistpage = QtWidgets.QLineEdit(self.PlayListPage)
        self.searchvideo_playlistpage.setGeometry(395,73,1011,60)
        self.searchvideo_playlistpage.setStyleSheet(
                "border-image : '';"
                "background-color : lightgrey;"    
                "border : 4px solid black;"
            )
        self.searchvideo_playlistpage.setFont(self.getSetting.search_video_font)

        # 회원 정보 업데이트, 로그아웃 버튼
        self.button_playlistpage = []
        self.button_playlistpage_text = ["UPDATE","LOGOUT"]
        for index in range(0,2):
            tmpBtn = QtWidgets.QPushButton(self.PlayListPage)
            xPos = 100 + (index*1286)
            if index == 0:
                yPos = 780
                xLength = 200
                yLength = 70
            else:
                yPos =789
                xLength = 181
                yLength = 85
            tmpBtn.setGeometry(xPos,yPos,xLength,yLength)
            self.button_playlistpage.append(tmpBtn)
            self.button_playlistpage[index].setText(self.button_playlistpage_text[index])
            self.button_playlistpage[index].setStyleSheet("border-image : '';"
                "background-color : darkgrey;"    
                "border : 4px solid black;"
            )
            self.button_playlistpage[index].setFont(self.getSetting.search_video_font)
        # 돋보기, 플러스 버튼
        self.button_searchbar_playlistpage = []
        for index in range(0,2):
            tmpBtn = QtWidgets.QPushButton(self.PlayListPage)
            xPos = 1407 + (index*79)
            tmpBtn.setGeometry(xPos,73,80,60)
            self.button_searchbar_playlistpage.append(tmpBtn)
        self.button_searchbar_playlistpage[0].setStyleSheet("border-image:url(Pic/SearchBtn.png);")
        self.button_searchbar_playlistpage[1].setStyleSheet("border-image:url(Pic/AddPlayList.png);")


        # 영상 재생 관련 (0.재생1.일시중지2.다음영상3.이전영상4.볼륨조절)
        self.button_video = []
        for index in range(0,5):
            tmpBtn = QtWidgets.QPushButton(self.VideoPage)
            xPos = 56 + (index*90)
            xlength = 90
            yLength = 87
            tmpBtn.setGeometry(xPos,754,xlength,yLength)
            self.button_video.append(tmpBtn)
        self.button_video[0].setStyleSheet("border-image:url(Pic/Play.png);")
        self.button_video[1].setStyleSheet("border-image:url(Pic/Pause.png);")
        self.button_video[2].setStyleSheet("border-image:url(Pic/NextVideo.png);")
        self.button_video[3].setStyleSheet("border-image:url(Pic/PreviousVideo.png);")
        self.button_video[4].setStyleSheet("border-image:url(Pic/Volume.png);")

        # 플레이리스트 관련 (0.반복재생 1.셔플재생 2.뒤로가기 3.재생목록선택)
        self.button_selectplaylist = []
        for index in range(0,4):
            tmpBtn = QtWidgets.QPushButton(self.VideoPage)
            xPos = 1193 + (index*100)
            if index < 2:
                xLength = 100
                yPos = 145
            elif index == 2:
                xLength = 150
                yPos = 145
            else:
                xPos = 1193
                yPos = 793
                xLength = 350
            tmpBtn.setGeometry(xPos,yPos,xLength,50)
            self.button_selectplaylist.append(tmpBtn)
        self.button_selectplaylist[0].setStyleSheet("border-image:url(Pic/Replay.png);")
        self.button_selectplaylist[1].setStyleSheet("border-image:url(Pic/ShufflePlay.png);")
        self.button_selectplaylist[2].setStyleSheet("border-image:url(Pic/Back.png);")
        self.button_selectplaylist[3].setStyleSheet("border-image:url(Pic/SelectPlayList.png);")



        #(0.업데이트 1.뒤로가기)
        self.button_videosearchpage = []
        for index in range(0,2):
            tmpBtn = QtWidgets.QPushButton(self.VideoSearchPage)
            xPos = 100 + (index*1372)
            if index == 0:
                yPos = 780
                xLength = 200
                yLength = 70
            else:
                yPos =710
                xLength = 93
                yLength = 160
            tmpBtn.setGeometry(xPos,yPos,xLength,yLength)
            self.button_videosearchpage.append(tmpBtn)
        self.button_videosearchpage[0].setStyleSheet("border-image : '';"
                "background-color : darkgrey;"    
                "border : 4px solid black;"
            )
        self.button_videosearchpage[0].setText("UPDATE")
        self.button_videosearchpage[0].setFont(self.getSetting.search_video_font)
        self.button_videosearchpage[1].setStyleSheet("border-image:url(Pic/Back_VideoSearchPage.png);")

    # 영상 검색 입력창
        self.searchvideo_videosearchpage = QtWidgets.QLineEdit(self.VideoSearchPage)
        self.searchvideo_videosearchpage.setGeometry(395,73,1011,60)
        self.searchvideo_videosearchpage.setStyleSheet(
                "border-image : '';"
                "background-color : lightgrey;"    
                "border : 4px solid black;"
            )
        self.searchvideo_videosearchpage.setFont(self.getSetting.search_video_font)

    # 영상 검색창 옆 버튼
        self.button_searchbar_videosearchpage = []
        for index in range(0,2):
            tmpBtn = QtWidgets.QPushButton(self.VideoSearchPage)
            xPos = 1407 + (index*79)
            tmpBtn.setGeometry(xPos,73,80,60)
            self.button_searchbar_videosearchpage.append(tmpBtn)
        self.button_searchbar_videosearchpage[0].setStyleSheet("border-image:url(Pic/SearchBtn.png);")
        self.button_searchbar_videosearchpage[1].setStyleSheet("border-image:url(Pic/AddPlayList.png);")





        # back
        self.button_back_findaccountpage = QtWidgets.QPushButton(self.FindAccountPage)
        self.button_back_findaccountpage.setGeometry(1472,710,93,160)
        self.button_back_findaccountpage.setStyleSheet("border-image:url(Pic/Back_VideoSearchPage.png);")


        # 영상 검색
        self.searchvideo_findaccountpage = QtWidgets.QLineEdit(self.FindAccountPage)
        self.searchvideo_findaccountpage.setGeometry(395,73,1011,60)
        self.searchvideo_findaccountpage.setStyleSheet(
                "border-image : '';"
                "background-color : lightgrey;"    
                "border : 4px solid black;"
            )
        self.searchvideo_findaccountpage.setFont(self.getSetting.search_video_font)


        # 영상 검색창 옆 버튼 (0.돋보기 1.재생목록추가)
        self.button_searchbar_findaccountpage = []
        for index in range(0,2):
            tmpBtn = QtWidgets.QPushButton(self.FindAccountPage)
            xPos = 1407 + (index*79)
            tmpBtn.setGeometry(xPos,73,80,60)
            self.button_searchbar_findaccountpage.append(tmpBtn)
        self.button_searchbar_findaccountpage[0].setStyleSheet("border-image:url(Pic/SearchBtn.png);")
        self.button_searchbar_findaccountpage[1].setStyleSheet("border-image:url(Pic/AddPlayList.png);")

        # 정보 입력창 (0.이름 1.전화번호 3.아이디 입력 4.전화번호 입력)
        self.inputinfor_findaccountpage = []
        for index in range(0,4):
            tmpSpace = QtWidgets.QLineEdit(self.FindAccountPage)
            xlength = 400
            if index == 1 or index == 3:
                xlength = 265
            yPos = 260 + (index * 80)
            if index >= 2:
                yPos = 440 + ((index)*80)
            tmpSpace.setGeometry(820,yPos,xlength,67)
            self.inputinfor_findaccountpage.append(tmpSpace)
            self.inputinfor_findaccountpage[index].setStyleSheet(
                "border-image : '';"
                "background-color : lightgrey;"    
                "border : 4px solid black;"
            )
            self.inputinfor_findaccountpage[index].setFont(self.getSetting.login_font_printinfor)
        # 정보 출력창(0.아이디 1.비밀번호)
        self.printidpw_findaccountpage = []
        for index in range(0,2):
            tmpSpace = QtWidgets.QLabel(self.FindAccountPage)
            yPos = 420 + (index* 340)
            tmpSpace.setGeometry(820,yPos,400,67)
            self.printidpw_findaccountpage.append(tmpSpace)
            self.printidpw_findaccountpage[index].setStyleSheet(
                "border-image : '';"
                "background-color : lightgrey;"    
                "border : 4px solid black;"
            )

        # 아이디/비번찾기
        self.button_findidpw = []
        self.button_findidpw_text = ["IDFIND","PWFIND"]
        for index in range(0,2):
            tmpBtn = QtWidgets.QPushButton(self.FindAccountPage)
            yPos = 340 + (index*340)
            tmpBtn.setGeometry(1100,yPos,120,67)
            self.button_findidpw.append(tmpBtn)
            self.button_findidpw[index].setText(self.button_findidpw_text[index])
            self.button_findidpw[index].setFont(self.getSetting.search_video_font)
            self.button_findidpw[index].setStyleSheet(
                "border-image : '';"
                "background-color : darkgrey;"    
                "border : 4px solid black;"
            )


    
    # update, back
        self.button_back_makeaccountpage = QtWidgets.QPushButton(self.MakeAccountPage)
        self.button_back_makeaccountpage.setGeometry(1472,710,93,160)
        self.button_back_makeaccountpage.setStyleSheet("border-image:url(Pic/Back_VideoSearchPage.png);")

        # 영상 검색
        self.searchvideo_makeaccountpage = QtWidgets.QLineEdit(self.MakeAccountPage)
        self.searchvideo_makeaccountpage.setGeometry(395,73,1011,60)
        self.searchvideo_makeaccountpage.setStyleSheet(
                "border-image : '';"
                "background-color : lightgrey;"    
                "border : 4px solid black;"
            )
        self.searchvideo_makeaccountpage.setFont(self.getSetting.search_video_font)

        # 영상 검색창 옆 버튼
        self.button_searchbar_makeaccountpage = []
        for index in range(0,2):
            tmpBtn = QtWidgets.QPushButton(self.MakeAccountPage)
            xPos = 1407 + (index*79)
            tmpBtn.setGeometry(xPos,73,80,60)
            self.button_searchbar_makeaccountpage.append(tmpBtn)
        self.button_searchbar_makeaccountpage[0].setStyleSheet("border-image:url(Pic/SearchBtn.png);")
        self.button_searchbar_makeaccountpage[1].setStyleSheet("border-image:url(Pic/AddPlayList.png);")

        #아이디 중복확인버튼
        self.button_checkid = QtWidgets.QPushButton(self.MakeAccountPage)
        self.button_checkid.setGeometry(1150,380,150,60)
        self.button_checkid.setText("CHECK")
        self.button_checkid.setFont(self.getSetting.search_video_font)
        self.button_checkid.setStyleSheet(
            "border-image:'';"
            "background-color : grey;"
            "border : 4px solid black;"
        )

        # 정보 입력
        self.inputinfor_makeaccountpage = []
        for index in range(0,5):
            tmpSpace = QtWidgets.QLineEdit(self.MakeAccountPage)
            if index == 0:
                xlength = 420
            else:
                xlength = 600
            yPos = 380 + (index * 70)
            tmpSpace.setGeometry(700,yPos,xlength,60)
            self.inputinfor_makeaccountpage.append(tmpSpace)
            self.inputinfor_makeaccountpage[index].setStyleSheet(
                "border-image : '';"
                "background-color : lightgrey;"    
                "border : 4px solid black;"
            )
            
        self.combobox_makeaccountpage = []
        for index in range(0,2):
            tmpBox = QtWidgets.QComboBox(self.MakeAccountPage)
            xPos = 700 + (index*350)
            tmpBox.setGeometry(xPos,730,250,60)
            self.combobox_makeaccountpage.append(tmpBox)
            self.combobox_makeaccountpage[index].setStyleSheet(
                "border : 4px solid black;"
                "border-image : '';"
                "background-color : lightgrey;"
            )
            
        # 회원가입 버튼
        self.button_makeaccount = QtWidgets.QPushButton(self.MakeAccountPage) #회원가입 버튼
        self.button_makeaccount.setGeometry(850,800,300,50)
        self.button_makeaccount.setText("MAKEID")
        self.button_makeaccount.setFont(self.getSetting.search_video_font)
        self.button_makeaccount.setStyleSheet(
                "border-image : '';"
                "background-color : grey;"    
                "border : 4px solid black;"
            )

    

        # back
        self.button_back_manageinforpage = QtWidgets.QPushButton(self.ManageInforPage)
        self.button_back_manageinforpage.setGeometry(1472,710,93,160)
        self.button_back_manageinforpage.setStyleSheet("border-image:url(Pic/Back_VideoSearchPage.png);")
        # 영상 검색
        self.searchvideo_manageinforpage = QtWidgets.QLineEdit(self.ManageInforPage)
        self.searchvideo_manageinforpage.setGeometry(395,73,1011,60)
        self.searchvideo_manageinforpage.setStyleSheet(
                "border-image : '';"
                "background-color : lightgrey;"    
                "border : 4px solid black;"
            )
        self.searchvideo_manageinforpage.setFont(self.getSetting.search_video_font)

        # 영상 검색창 옆 버튼
        self.button_searchbar_manageinforpage = []
        for index in range(0,2):
            tmpBtn = QtWidgets.QPushButton(self.ManageInforPage)
            xPos = 1407 + (index*79)
            tmpBtn.setGeometry(xPos,73,80,60)
            self.button_searchbar_manageinforpage.append(tmpBtn)
        self.button_searchbar_manageinforpage[0].setStyleSheet("border-image:url(Pic/SearchBtn.png);")
        self.button_searchbar_manageinforpage[1].setStyleSheet("border-image:url(Pic/AddPlayList.png);")

        # 정보 입력
        self.inputinfor_manageinforpage = []
        for index in range(0,5):
            tmpSpace = QtWidgets.QLineEdit(self.ManageInforPage)
            yPos = 380 + (index * 70)
            tmpSpace.setGeometry(700,yPos,600,60)
            self.inputinfor_manageinforpage.append(tmpSpace)
            self.inputinfor_manageinforpage[index].setStyleSheet(
                "border-image : '';"
                "background-color : lightgrey;"    
                "border : 4px solid black;"
            )
            
        # 업데이트 버튼 
        self.button_manageinforpage = QtWidgets.QPushButton(self.ManageInforPage) #회원가입 버튼
        self.button_manageinforpage.setGeometry(850,740,300,50)
        self.button_manageinforpage.setText("UPDATE")
        self.button_manageinforpage.setFont(self.getSetting.search_video_font)
        self.button_manageinforpage.setStyleSheet(
                "border-image : '';"
                "background-color : grey;"    
                "border : 4px solid black;"
            )

        # 종료버튼
        self.button_exit = []
        self.pageList = [self.StartPage,self.PlayListPage,self.VideoPage,self.VideoSearchPage,self.FindAccountPage,self.MakeAccountPage,self.ManageInforPage]
        for index in range(0,len(self.pageList)):
            tmpBtn = QtWidgets.QPushButton(self.pageList[index])
            tmpBtn.setGeometry(1540,10,50,50)
            self.button_exit.append(tmpBtn)
            self.button_exit[index].setStyleSheet("border-image:url(Pic/Exit.png);")

        # self.stackedWidget.setCurrentIndex(5)  
        self.mainWindow.show()