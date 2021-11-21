    
from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import QCoreApplication
import Ui
import MyDataBase
import Config

class VideoPage:
    def __init__(self,revui):
        self.ui = revui


    # 재생 버튼
        self.ui.button_video[0].mousePressEvent = lambda event: self.play_event(event)
        self.ui.button_video[0].enterEvent = lambda event: self.enter_playbtn_event(event)
        self.ui.button_video[0].leaveEvent = lambda event: self.leave_playbtn_event(event)
    # 일시정지 버튼
        self.ui.button_video[1].mousePressEvent = lambda event: self.pause_event(event)
        self.ui.button_video[1].enterEvent = lambda event: self.enter_pausebtn_event(event)
        self.ui.button_video[1].leaveEvent = lambda event: self.leave_pausebtn_event(event)
    # 다음영상 버튼
        self.ui.button_video[2].mousePressEvent = lambda event: self.nextvideo_event(event)
        self.ui.button_video[2].enterEvent = lambda event: self.enter_nextvideobtn_event(event)
        self.ui.button_video[2].leaveEvent = lambda event: self.leave_nextvideobtn_event(event)
    # 이전영상 버튼
        self.ui.button_video[3].mousePressEvent = lambda event: self.previousvideo_event(event)
        self.ui.button_video[3].enterEvent = lambda event: self.enter_previousvideo_event(event)
        self.ui.button_video[3].leaveEvent = lambda event: self.leave_previousvideo_event(event)
    # 음량 버튼
        self.ui.button_video[4].mousePressEvent = lambda event: self.volume_event(event)
        self.ui.button_video[4].enterEvent = lambda event: self.enter_volume_event(event)
        self.ui.button_video[4].leaveEvent = lambda event: self.leave_volume_event(event)
    # 반복재생 버튼 
        self.ui.button_selectplaylist[0].mousePressEvent = lambda event: self.replay_event(event)
        self.ui.button_selectplaylist[0].enterEvent = lambda event: self.enter_replay_event(event)
        self.ui.button_selectplaylist[0].leaveEvent = lambda event: self.leave_replay_event(event)
    # 셔플 재생
        self.ui.button_selectplaylist[1].mousePressEvent = lambda event: self.shuffleplay_event(event)
        self.ui.button_selectplaylist[1].enterEvent = lambda event: self.enter_shuffleplay_event(event)
        self.ui.button_selectplaylist[1].leaveEvent = lambda event: self.leave_shuffleplay_event(event)
    # 뒤로가기
        self.ui.button_selectplaylist[2].mousePressEvent = lambda event: self.back_event(event)
        self.ui.button_selectplaylist[2].enterEvent = lambda event: self.enter_back_event(event)
        self.ui.button_selectplaylist[2].leaveEvent = lambda event: self.leave_back_event(event)
    # 재생목록선택
        self.ui.button_selectplaylist[3].mousePressEvent = lambda event: self.selectplaylist_event(event)
        self.ui.button_selectplaylist[3].enterEvent = lambda event: self.enter_selectplaylist_event(event)
        self.ui.button_selectplaylist[3].leaveEvent = lambda event: self.leave_selectplaylist_event(event)

    def play_event(self,event):
        print("플레이버튼눌렀을때동작")
    def enter_playbtn_event(self,event):
        self.ui.button_video[0].setStyleSheet("border-image:url(Pic/PlayEvent.png);")
    def leave_playbtn_event(self,event):
        self.ui.button_video[0].setStyleSheet("border-image:url(Pic/Play.png);")
    def pause_event(self,event):
        print("일시중지버튼눌렀을때동작")
    def enter_pausebtn_event(self,event):
        self.ui.button_video[1].setStyleSheet("border-image:url(Pic/PauseEvent.png);")
    def leave_pausebtn_event(self,event):
        self.ui.button_video[1].setStyleSheet("border-image:url(Pic/Pause.png);")
    def nextvideo_event(self,event):
        print("다음영상버튼눌렀을때동작")
    def enter_nextvideobtn_event(self,event):
        self.ui.button_video[2].setStyleSheet("border-image:url(Pic/NextVideoEvent.png);")
    def leave_nextvideobtn_event(self,event):
        self.ui.button_video[2].setStyleSheet("border-image:url(Pic/NextVideo.png);")
    def previousvideo_event(self,event):
        print("이전영상눌렀을때동작")
    def enter_previousvideo_event(self,event):
        self.ui.button_video[3].setStyleSheet("border-image:url(Pic/PreviousVideoEvent.png);")
    def leave_previousvideo_event(self,event):
        self.ui.button_video[3].setStyleSheet("border-image:url(Pic/PreviousVideo.png);")
    def volume_event(self,event):
        print("음량눌렀을때동작")
    def enter_volume_event(self,event):
        self.ui.button_video[4].setStyleSheet("border-image:url(Pic/VolumeEvent.png);")
    def leave_volume_event(self,event):
        self.ui.button_video[4].setStyleSheet("border-image:url(Pic/Volume.png);")






# 재생목록 파트
    def replay_event(self,event):
        print("반복재생버튼 눌렀을때 동작")
    def enter_replay_event(self,event):
        self.ui.button_selectplaylist[0].setStyleSheet("border-image:url(Pic/ReplayEvent.png);")
    def leave_replay_event(self,event):
        self.ui.button_selectplaylist[0].setStyleSheet("border-image:url(Pic/Replay.png);")
    def shuffleplay_event(self,event):
        print("셔플재생 눌렀을때 동작")
    def enter_shuffleplay_event(self,event):
        self.ui.button_selectplaylist[1].setStyleSheet("border-image:url(Pic/ShufflePlayEvent.png);")
    def leave_shuffleplay_event(self,event):
        self.ui.button_selectplaylist[1].setStyleSheet("border-image:url(Pic/ShufflePlay.png);")
    def back_event(self,event):
        print("뒤로가기 누를때 동작")
    def enter_back_event(self,event):
        self.ui.button_selectplaylist[2].setStyleSheet("border-image:url(Pic/BackEvent.png);")
    def leave_back_event(self,event):
        self.ui.button_selectplaylist[2].setStyleSheet("border-image:url(Pic/Back.png);")
    def selectplaylist_event(self,event):
        print("재생목록선택 눌렀을때 동작")
    def enter_selectplaylist_event(self,event):
        self.ui.button_selectplaylist[3].setStyleSheet("border-image:url(Pic/SelectPlayListEvent.png);")
    def leave_selectplaylist_event(self,event):
        self.ui.button_selectplaylist[3].setStyleSheet("border-image:url(Pic/SelectPlayList.png);")
