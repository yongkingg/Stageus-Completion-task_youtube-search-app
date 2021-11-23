from sys import _xoptions
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QBrush, QImage, QPalette, QPixmap
import Config
from VideoSearchPage import VideoSearchPage

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
        self.getSetting = Config.Setting()
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
        self.stackedWidget.setStyleSheet("background-color : white;")

    # 시작 페이지 0 
        self.StartPage = QtWidgets.QWidget()
        self.StartPage.setMinimumSize(QtCore.QSize(1600, 900))
        self.StartPage.setMaximumSize(QtCore.QSize(1600, 900))
        self.stackedWidget.addWidget(self.StartPage)
    # 재생목록 페이지 1
        self.PlayListPage = QtWidgets.QWidget()
        self.PlayListPage.setMinimumSize(QtCore.QSize(1600, 900))
        self.PlayListPage.setMaximumSize(QtCore.QSize(1600, 900))
        self.stackedWidget.addWidget(self.PlayListPage)
    # 영상 재생 페이지 2
        self.VideoPage = QtWidgets.QWidget()
        self.VideoPage.setMinimumSize(QtCore.QSize(1600, 900))
        self.VideoPage.setMaximumSize(QtCore.QSize(1600, 900))
        self.stackedWidget.addWidget(self.VideoPage)
    # 영상 검색 페이지 3
        self.VideoSearchPage = QtWidgets.QWidget()
        self.VideoSearchPage.setMinimumSize(QtCore.QSize(1600, 900))
        self.VideoSearchPage.setMaximumSize(QtCore.QSize(1600, 900))
        self.stackedWidget.addWidget(self.VideoSearchPage)
    # 아이디/비밀번호 찾기 페이지 4
        self.FindAccountPage = QtWidgets.QWidget()
        self.FindAccountPage.setMinimumSize(QtCore.QSize(1600, 900))
        self.FindAccountPage.setMaximumSize(QtCore.QSize(1600, 900))
        self.stackedWidget.addWidget(self.FindAccountPage)
    # 회원가입페이지 5
        self.MakeAccountPage = QtWidgets.QWidget()
        self.MakeAccountPage.setMinimumSize(QtCore.QSize(1600, 900))
        self.MakeAccountPage.setMaximumSize(QtCore.QSize(1600, 900))
        self.stackedWidget.addWidget(self.MakeAccountPage)
    # 계정 관리 창 6
        self.ManageInforPage = QtWidgets.QWidget()
        self.ManageInforPage.setMinimumSize(QtCore.QSize(1600, 900))
        self.ManageInforPage.setMaximumSize(QtCore.QSize(1600, 900))
        self.stackedWidget.addWidget(self.ManageInforPage)



        #배경 정사각형
        self.backgroundRec_playlistpage = QtWidgets.QLabel(self.PlayListPage)
        self.backgroundRec_playlistpage.setGeometry(5,0,1595,900)
        self.backgroundRec_playlistpage.setStyleSheet("border : 2px solid black;")
        self.backgroundRec_startpage = QtWidgets.QLabel(self.StartPage)
        self.backgroundRec_startpage.setGeometry(5,0,1595,900)
        self.backgroundRec_startpage.setStyleSheet("border : 2px solid black;")
        self.backgroundRec_videopage = QtWidgets.QLabel(self.VideoPage)
        self.backgroundRec_videopage.setGeometry(5,0,1595,900)
        self.backgroundRec_videopage.setStyleSheet("border : 2px solid black;")
        self.backgroundRec_videosearchpage = QtWidgets.QLabel(self.VideoSearchPage)
        self.backgroundRec_videosearchpage.setGeometry(5,0,1595,900)
        self.backgroundRec_videosearchpage.setStyleSheet("border : 2px solid black;")
        self.backgroundRec_manageinforpage = QtWidgets.QLabel(self.ManageInforPage)
        self.backgroundRec_manageinforpage.setGeometry(5,0,1595,900)
        self.backgroundRec_manageinforpage.setStyleSheet(
            "border : 2px solid black;"
            "background-color : #D9D9D9;"
            )


        self.backgroundRec_makeaccountpage = QtWidgets.QLabel(self.MakeAccountPage)
        self.backgroundRec_makeaccountpage.setGeometry(5,0,1595,900)
        self.backgroundRec_makeaccountpage.setStyleSheet(
            "border : 2px solid black;"
            "background-color : #D9D9D9;"
            )
        self.backgroundRec_findaccountpage = QtWidgets.QLabel(self.FindAccountPage)
        self.backgroundRec_findaccountpage.setGeometry(5,0,1595,900)
        self.backgroundRec_findaccountpage.setStyleSheet(
            "border : 2px solid black;"
            "background-color : #BFBFBF;"
            )


            
#로그인 사진
        self.loginPic = QtWidgets.QLabel(self.StartPage)
        self.loginPic.setGeometry(400,100,800,400)
        self.loginPic.setStyleSheet(
            "border-image : url(Pic/LoginPic.png);"
            "border : white;"
        )   
        # 계정만들기
        self.makeAccountPic = QtWidgets.QLabel(self.StartPage)
        self.makeAccountPic.setGeometry(470,717,250,50)
        self.makeAccountPic.setText("Join membership?")
        self.makeAccountPic.setFont(self.getSetting.login_font_guide)
        # 아이디비번찾기 안내
        self.findAccountPic = QtWidgets.QLabel(self.StartPage)
        self.findAccountPic.setGeometry(935,717,200,50)
        self.findAccountPic.setText("Find ID/PW")
        self.findAccountPic.setFont(self.getSetting.login_font_guide)
        self.findAccountPic = QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

        
        # 상단 라벨 
        self.upside_bar_startpage = QtWidgets.QLabel(self.StartPage)
        self.upside_bar_startpage.setGeometry(5,0,1595,50)
        self.upside_bar_startpage.setStyleSheet(
            "border : 2px solid black;"
            "background-color : #BFBFBF;"
        )
        self.upside_bar_playlistpage = QtWidgets.QLabel(self.PlayListPage)
        self.upside_bar_playlistpage.setGeometry(5,0,1595,50)
        self.upside_bar_playlistpage.setStyleSheet(
            "border : 2px solid black;"
            "background-color : #BFBFBF;"
        )
        self.upside_bar_findaccountpage = QtWidgets.QLabel(self.FindAccountPage)
        self.upside_bar_findaccountpage.setGeometry(5,0,1595,50)
        self.upside_bar_findaccountpage.setStyleSheet(
            "border : 2px solid black;"
            "background-color : #BFBFBF;"
        )
        self.upside_bar_makeaccountpage = QtWidgets.QLabel(self.MakeAccountPage)
        self.upside_bar_makeaccountpage.setGeometry(5,0,1595,50)
        self.upside_bar_makeaccountpage.setStyleSheet(
            "border : 2px solid black;"
            "background-color : #BFBFBF;"
        )
        self.upside_bar_videosearchpage = QtWidgets.QLabel(self.VideoSearchPage)
        self.upside_bar_videosearchpage.setGeometry(5,0,1595,50)
        self.upside_bar_videosearchpage.setStyleSheet(
            "border : 2px solid black;"
            "background-color : #BFBFBF;"
        )
        self.upside_bar_manageinforpage = QtWidgets.QLabel(self.ManageInforPage)
        self.upside_bar_manageinforpage.setGeometry(5,0,1595,50)
        self.upside_bar_manageinforpage.setStyleSheet(
            "border : 2px solid black;"
            "background-color : #BFBFBF;"
        )
        self.upside_bar_videopage = QtWidgets.QLabel(self.VideoPage)
        self.upside_bar_videopage.setGeometry(5,0,1595,50)
        self.upside_bar_videopage.setStyleSheet(
            "border : 2px solid black;"
            "background-color : #BFBFBF;"
        )
        #상단 라벨 위 유튜브 이미지
        self.upside_bar_image_startpage = QtWidgets.QLabel(self.StartPage)
        self.upside_bar_image_startpage.setGeometry(10,10,200,30)
        self.upside_bar_image_startpage.setStyleSheet(
            "background-image: url(Pic/youtubelogo.png);"
        )
        self.upside_bar_image_playlistpage = QtWidgets.QLabel(self.PlayListPage)
        self.upside_bar_image_playlistpage.setGeometry(10,10,200,30)
        self.upside_bar_image_playlistpage.setStyleSheet(
            "background-image: url(Pic/youtubelogo.png);"
        )
        self.upside_bar_image_findaccountpage = QtWidgets.QLabel(self.FindAccountPage)
        self.upside_bar_image_findaccountpage.setGeometry(10,10,200,30)
        self.upside_bar_image_findaccountpage.setStyleSheet(
            "background-image: url(Pic/youtubelogo.png);"
        )
        self.upside_bar_image_makeaccountpage = QtWidgets.QLabel(self.MakeAccountPage)
        self.upside_bar_image_makeaccountpage.setGeometry(10,10,200,30)
        self.upside_bar_image_makeaccountpage.setStyleSheet(
            "background-image: url(Pic/youtubelogo.png);"
        )
        self.upside_bar_image_videosearchpage = QtWidgets.QLabel(self.VideoSearchPage)
        self.upside_bar_image_videosearchpage.setGeometry(10,10,200,30)
        self.upside_bar_image_videosearchpage.setStyleSheet(
            "background-image: url(Pic/youtubelogo.png);"
        )
        self.upside_bar_image_manageinforpage = QtWidgets.QLabel(self.ManageInforPage)
        self.upside_bar_image_manageinforpage.setGeometry(10,10,200,30)
        self.upside_bar_image_manageinforpage.setStyleSheet(
            "background-image: url(Pic/youtubelogo.png);"
        )
        self.upside_bar_image_videopage = QtWidgets.QLabel(self.VideoPage)
        self.upside_bar_image_videopage.setGeometry(10,10,200,30)
        self.upside_bar_image_videopage.setStyleSheet(
            "background-image: url(Pic/youtubelogo.png);"
        )
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






        # 정보출력쪽 정사각형 플레이리스트창
        self.printspace_playlistpage = QtWidgets.QLabel(self.PlayListPage)
        self.printspace_playlistpage.setGeometry(50,73,300,800)
        self.printspace_playlistpage.setStyleSheet(
            "border : 4px solid black;"
            "background-color : #D9D9D9;"
            )
        # 정보출력쪽 사람 플레이리스트창
        self.personimage_playlistpage = QtWidgets.QLabel(self.PlayListPage)
        self.personimage_playlistpage.setGeometry(60,80,280,310)
        self.personimage_playlistpage.setStyleSheet(
            "border-image : url(Pic/person.png);"
            )

        # 정보출력쪽 정사각형 영상검색창
        self.printspace_videosearchpage = QtWidgets.QLabel(self.VideoSearchPage)
        self.printspace_videosearchpage.setGeometry(50,73,300,800)
        self.printspace_videosearchpage.setStyleSheet(
            "border : 4px solid black;"
            "background-color : #D9D9D9;"
            )
        # 정보출력쪽 사람 영상검색창
        self.personimage_videosearchpage = QtWidgets.QLabel(self.VideoSearchPage)
        self.personimage_videosearchpage.setGeometry(60,80,280,310)
        self.personimage_videosearchpage.setStyleSheet(
            "border-image : url(Pic/person.png);"
            )
            
        # 정보출력 - 플레이리스트 페이지 ( 0. 이름 1.나이 2.전화번호3.팀4.직급)
        self.print_infor_playlistpage = []
        for index in range(0,5):
            tmpSpace = QtWidgets.QLabel(self.PlayListPage)
            yPos = 425 + (index * 65)
            tmpSpace.setGeometry(60,yPos,280,50)
            tmpSpace.setStyleSheet("border-image : '';"
                "Color : Black;"
                "background-color : #D9D9D9;"
            )
            self.print_infor_playlistpage.append(tmpSpace)
        # 정보출력 - 영상 검색 페이지
        self.print_infor_videosearchpage = []
        for index in range(0,5):
            tmpSpace = QtWidgets.QLabel(self.VideoSearchPage)
            yPos = 425 + (index * 65)
            tmpSpace.setGeometry(60,yPos,280,50)
            tmpSpace.setStyleSheet("border-image : '';"
                "Color : Black;"
                "background-color : #D9D9D9;"  # #D9D9D9;
            )
            self.print_infor_videosearchpage.append(tmpSpace)
        
        
        # 플레이리스트창 배경
        self.back_videosearchpage = QtWidgets.QLabel(self.VideoSearchPage)
        self.back_videosearchpage.setGeometry(395,100,1170,690)
        self.back_videosearchpage.setStyleSheet(
            "border: 4px solid black;"
            "background-color : #D9D9D9"
            )
        self.logoutbar_videosearchpage = QtWidgets.QLabel(self.VideoSearchPage)
        self.logoutbar_videosearchpage.setGeometry(395,786,1080,85)
        self.logoutbar_videosearchpage.setStyleSheet(
            "border: 4px solid black;"
            "background-color : #D9D9D9"
            )
        # 플레이리스트창
        self.back_playlistpage = QtWidgets.QScrollArea(self.PlayListPage)
        self.back_playlistpage.setGeometry(395,143,1170,690)
        self.back_playlistpage.setStyleSheet(
            #"border: 4px solid black;"
            "background-color : #D9D9D9;"
            )
        # self.back_playlistpage.setWidgetResizable(True)

        # self.logoutbar_playlistpage = QtWidgets.QLabel(self.PlayListPage)
        # self.logoutbar_playlistpage.setGeometry(395,800,999,85)
        # self.logoutbar_playlistpage.setStyleSheet(
        #     "border: 4px solid black;"
        #     "background-color : #D9D9D9"
        #     )

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
            xPos = 100 + (index*1284)
            if index == 0:
                yPos = 780
                xLength = 200
                yLength = 70
            else:
                yPos =850
                xLength = 181
                yLength = 30
            tmpBtn.setGeometry(xPos,yPos,xLength,yLength)
            self.button_playlistpage.append(tmpBtn)
            self.button_playlistpage[index].setText(self.button_playlistpage_text[index])
            self.button_playlistpage[index].setStyleSheet("border-image : '';"
                "background-color : darkgrey;"    
                "border : 4px solid black;"
            )
            self.button_playlistpage[index].setFont(self.getSetting.search_video_font)
            # (1080 100 45 690 4px)
            # 스크롤
            # self.scrollbar_playlistpage = QtWidgets.QScrollArea(self.PlayListPage)
            # self.scrollbar_playlistpage.setWidget(self.)
        # 돋보기, 플러스 버튼
        self.button_searchbar_playlistpage = []
        for index in range(0,2):
            tmpBtn = QtWidgets.QPushButton(self.PlayListPage)
            xPos = 1407 + (index*79)
            tmpBtn.setGeometry(xPos,73,80,60)
            self.button_searchbar_playlistpage.append(tmpBtn)
        self.button_searchbar_playlistpage[0].setStyleSheet("border-image:url(Pic/SearchBtn.png);")
        self.button_searchbar_playlistpage[1].setStyleSheet("border-image:url(Pic/AddPlayList.png);")




        self.videospace_videopage = QtWidgets.QLabel(self.VideoPage)
        self.videospace_videopage.setGeometry(56,145,1100,610)
        self.videospace_videopage.setStyleSheet(
            "background-color : #D9D9D9;"
            "border : 2px solid black;"
            )
        self.videobtnspace_videopage = QtWidgets.QLabel(self.VideoPage)
        self.videobtnspace_videopage.setGeometry(56,754,1100,87)
        self.videobtnspace_videopage.setStyleSheet(
            "background-color : grey;"
            "border : 2px solid black;"
            )
        self.playbtnspace_videopage = QtWidgets.QLabel(self.VideoPage)
        self.playbtnspace_videopage.setGeometry(1193,145,350,700)
        self.playbtnspace_videopage.setStyleSheet(
            "border : 2px solid black;"
            "background-color : grey;"
            )
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


    
        self.guide_findaccountpage = []
        self.guide_findaccountpage_text = ["FIND ID","FIND PW"]
        for index in range(0,2):
            tmpSpace = QtWidgets.QLabel(self.FindAccountPage)
            yPos = 180 + (index * 340)
            tmpSpace.setGeometry(650,yPos,300,70)
            self.guide_findaccountpage.append(tmpSpace)
            self.guide_findaccountpage[index].setStyleSheet(
                "border : 4px solid black;"
                "background-color : grey;"
                )
            self.guide_findaccountpage[index].setText(self.guide_findaccountpage_text[index])
            self.guide_findaccountpage[index].setFont(self.getSetting.findidpw_font)
            self.guide_findaccountpage[index].setAlignment(QtCore.Qt.AlignCenter)
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
            tmpSpace.setGeometry(600,yPos,xlength,67)
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
            tmpSpace.setGeometry(600,yPos,400,67)
            self.printidpw_findaccountpage.append(tmpSpace)
            self.printidpw_findaccountpage[index].setStyleSheet(
                "border-image : '';"
                "background-color : lightgrey;"    
                "border : 4px solid black;"
            )

        # 아이디/비번찾기
        self.button_findidpw = []
        self.button_findidpw_text = ["ID FIND","PW FIND"]
        for index in range(0,2):
            tmpBtn = QtWidgets.QPushButton(self.FindAccountPage)
            yPos = 340 + (index*340)
            tmpBtn.setGeometry(880,yPos,120,67)
            self.button_findidpw.append(tmpBtn)
            self.button_findidpw[index].setText(self.button_findidpw_text[index])
            self.button_findidpw[index].setFont(self.getSetting.search_video_font)
            self.button_findidpw[index].setStyleSheet(
                "border-image : '';"
                "background-color : darkgrey;"    
                "border : 4px solid black;"
            )


    
        # back
        self.button_back_makeaccountpage = QtWidgets.QPushButton(self.MakeAccountPage)
        self.button_back_makeaccountpage.setGeometry(1472,710,93,160)
        self.button_back_makeaccountpage.setStyleSheet("border-image:url(Pic/Back_VideoSearchPage.png);")

        
        #아이디 중복확인버튼
        self.button_checkid = QtWidgets.QPushButton(self.MakeAccountPage)
        self.button_checkid.setGeometry(950,250,150,60)
        self.button_checkid.setText("CHECK")
        self.button_checkid.setFont(self.getSetting.search_video_font)
        self.button_checkid.setStyleSheet(
            "border-image:'';"
            "background-color : grey;"
            "border : 4px solid black;"
        )

        self.personimage_makeaccountpage = QtWidgets.QLabel(self.MakeAccountPage)
        self.personimage_makeaccountpage.setGeometry(650,60,300,300)
        self.personimage_makeaccountpage.setStyleSheet("border-image : url(Pic/person.png);")
        
        
        self.print_signup = QtWidgets.QLabel(self.MakeAccountPage)
        self.print_signup.setGeometry(700,180,200,50)
        self.print_signup.setStyleSheet(
            "border : '';"
            "background-color : #D9D9D9;"
            )
        self.print_signup.setText("SIGN UP")
        self.print_signup.setAlignment(QtCore.Qt.AlignCenter)
        self.print_signup.setFont(self.getSetting.findidpw_font)
        # 정보 입력
        self.inputinfor_makeaccountpage = []
        for index in range(0,5):
            tmpSpace = QtWidgets.QLineEdit(self.MakeAccountPage)
            if index == 0:
                xlength = 420
            else:
                xlength = 600
            yPos = 250 + (index * 100)
            tmpSpace.setGeometry(500,yPos,xlength,60)
            self.inputinfor_makeaccountpage.append(tmpSpace)
            self.inputinfor_makeaccountpage[index].setStyleSheet(
                "border-image : '';"
                "background-color : lightgrey;"    
                "border : 4px solid black;"
            )
        self.warning_bar = []
        for index in range(0,5):
            tmpSpace = QtWidgets.QLabel(self.MakeAccountPage)
            yPos = 310 + (index * 100)
            tmpSpace.setGeometry(520,yPos,600,40)
            self.warning_bar.append(tmpSpace)
            self.warning_bar[index].setStyleSheet(
            "color : red;"
            "background-color : #D9D9D9 ;"
            )
            
        self.combobox_makeaccountpage = []
        for index in range(0,2):
            tmpBox = QtWidgets.QComboBox(self.MakeAccountPage)
            xPos = 500 + (index*350)
            tmpBox.setGeometry(xPos,750,250,60)
            self.combobox_makeaccountpage.append(tmpBox)
            self.combobox_makeaccountpage[index].setStyleSheet(
                "border : 4px solid black;"
                "border-image : '';"
                "background-color : lightgrey;"
            )
            
        # 회원가입 버튼
        self.button_makeaccount = QtWidgets.QPushButton(self.MakeAccountPage) #회원가입 버튼
        self.button_makeaccount.setGeometry(650,820,300,50)
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
        

        self.personimage_manageinforpage = QtWidgets.QLabel(self.ManageInforPage)
        self.personimage_manageinforpage.setGeometry(650,60,300,300)
        self.personimage_manageinforpage.setStyleSheet("border-image : url(Pic/person.png);")

        # 정보 입력 (1. 패스워드 2. 이름 3. 나이 4.전화번호)
        self.inputinfor_manageinforpage = []
        for index in range(0,5):
            tmpSpace = QtWidgets.QLineEdit(self.ManageInforPage)
            yPos = 380 + (index * 70)
            tmpSpace.setGeometry(500,yPos,600,60)
            self.inputinfor_manageinforpage.append(tmpSpace)
            self.inputinfor_manageinforpage[index].setStyleSheet(
                "border-image : '';"
                "background-color : lightgrey;"    
                "border : 4px solid black;"
            )
            
        # 업데이트 버튼 
        self.button_manageinforpage = QtWidgets.QPushButton(self.ManageInforPage) #회원가입 버튼
        self.button_manageinforpage.setGeometry(650,740,300,50)
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
            tmpBtn.setGeometry(1540,5,40,40)
            self.button_exit.append(tmpBtn)
            self.button_exit[index].setStyleSheet("border-image:url(Pic/Exit.png);")
        self.playListCount = 0
        self.playList = []
        self.scrollAreaWidgetContents = QtWidgets.QWidget(self.back_playlistpage)
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        self.stackedWidget.setCurrentIndex(0)  
        self.mainWindow.show()

    def makePlayList(self):
        # PlayList 추가 다이얼로그
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
        print(self.playListCount)
        self.result.close()
        name = self.playListName.text()
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(0,0,1125,100)
        self.label.setStyleSheet("border:2px solid black;")
        self.label.setMaximumHeight(100)
        self.label.setMinimumHeight(100)
        self.playList.append(self.label)
        self.verticalLayout.addWidget(self.playList[self.playListCount])
        self.playListCount += 1
        self.back_playlistpage.setWidget(self.scrollAreaWidgetContents)


# 플레이리스트를 db에 연결 . 꺼도 유지되게 만들기 
# ---- db 만들어놓긴 했음.
# 스크롤바 공부할것. 
# 플레이리스트 이름, 재생 , 삭제 버튼 만들기
