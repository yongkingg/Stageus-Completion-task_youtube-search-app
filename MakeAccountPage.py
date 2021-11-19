from os import terminal_size
from PyQt5 import QtWidgets
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication
import Ui
import MyDataBase
import Setting
class MakeAccountPage:
    def __init__(self,revui):
        self.ui = revui
        self.db = MyDataBase.MyDataBase()
        self.getFont = Setting.Setting()
        # makeid 버튼 이벤트
        # self.ui.button_makeaccount.mousePressEvent = lambda event: self.makeaccount_event(event)
        # self.ui.button_makeaccount.enterEvent = lambda event: self.enter_makeaccountbtn_event(event)
        # self.ui.button_makeaccount.leaveEvent = lambda event: self.leave_makeaccountbtn_event(event)
        # 돋보기, 재생목록 추가 버튼 비활성화
        self.ui.button_searchbar_makeaccountpage[0].setStyleSheet("border-image:url(Pic/SearchBtnEvent.png);")
        self.ui.button_searchbar_makeaccountpage[1].setStyleSheet("border-image:url(Pic/AddPlayListEvent.png);")
        self.ui.button_searchbar_makeaccountpage[0].setDisabled(True)
        self.ui.button_searchbar_makeaccountpage[1].setDisabled(True)
        # Back 이벤트
        self.ui.button_back_makeaccountpage.mousePressEvent = lambda event: self.back_event(event)
        self.ui.button_back_makeaccountpage.enterEvent = lambda event: self.enter_button_event(event)
        self.ui.button_back_makeaccountpage.leaveEvent = lambda event: self.leave_button_event(event)
        # check 이벤트
        self.ui.button_checkid.mousePressEvent = lambda event: self.idcheck_event(event)
        self.ui.button_checkid.enterEvent = lambda event: self.enter_checkbtn_event(event)
        self.ui.button_checkid.leaveEvent = lambda event: self.leave_checkbtn_event(event)
        # 정보입력창 placeholder 이벤트
        self.guideText = ["ID :","PW :","NAME :","AGE :","Phonenumber :"]
        for index in range(0,5):
            self.ui.inputinfor_makeaccountpage[index].setPlaceholderText(self.guideText[index])
            self.ui.inputinfor_makeaccountpage[index].setFont(self.getFont.search_video_font)
        # QComboBox
        self.jobList = ["기획 1팀","기획 2팀","제작 1팀","제작 2팀","개발 1팀","개발 2팀","경영지원 1팀","경영지원 2팀"]
        self.classList = ["부장","차장","과장","대리","사원","인턴"]
        for index in range(0,len(self.jobList)):
            self.ui.combobox_makeaccountpage[0].addItem(self.jobList[index])
        self.ui.combobox_makeaccountpage[0].setFont(self.getFont.login_font_printinfor)
        for index in range(0,len(self.classList)):
            self.ui.combobox_makeaccountpage[1].addItem(self.classList[index])
        self.ui.combobox_makeaccountpage[1].setFont(self.getFont.login_font_printinfor)
        # onchange
        for index in range(0,4):
            self.ui.inputinfor_makeaccountpage[index+1].textChanged.connect(self.make_account_logic)

        self.block_btn()
    def block_btn(self):
        self.ui.button_makeaccount.setDisabled(True)
        self.ui.button_makeaccount.setStyleSheet(
            "background-color : black;"
            "border-image : '';"
            "color : black;"
            )
        self.option = []

    
    def idcheck_event(self,event):
        self.idValue = self.ui.inputinfor_makeaccountpage[0].text()
        self.readInfor = self.db.read("userInterFace",["Id"],[self.idValue])
        if self.idValue == self.readInfor[0][0]:
            self.dialog = Setting.Dialog()
            self.dialog.message.setText("이 아이디를 사용하실 수 없습니다.")
            self.dialog.result.show()
        else:
            self.dialog = Setting.Dialog()
            self.dialog.message.setText("이 아이디를 사용하실 수 있습니다.")
            self.dialog.result.show()
    
    def make_account_logic(self):
        self.pwValue = self.ui.inputinfor_makeaccountpage[1].text()
        self.nameValue = self.ui.inputinfor_makeaccountpage[1].text()
        self.ageValue = self.ui.inputinfor_makeaccountpage[1].text()
        self.numberValue = self.ui.inputinfor_makeaccountpage[1].text()

    def makeaccount_event(self,event):
        pass













































































    def enter_checkbtn_event(self,event):
        self.ui.button_checkid.setStyleSheet(
            "border-image:'';"
            "background-color : black;"
            "border : 4px solid black;"
            "color : white;"
        )
    def leave_checkbtn_event(self,event):
        self.ui.button_checkid.setStyleSheet(
            "border-image:'';"
            "background-color : grey;"
            "border : 4px solid black;"
        )
    def enter_makeaccountbtn_event(self,event):
        self.ui.button_makeaccount.setStyleSheet(
                "border-image : '';"
                "background-color : black;"    
                "border : 4px solid black;"
                "color : white;"
            )
    def leave_makeaccountbtn_event(self,event):
        self.ui.button_makeaccount.setStyleSheet(
                "border-image : '';"
                "background-color : grey;"    
                "border : 4px solid black;"
            )
    def back_event(self,event):
        self.ui.pageset -= 5
        self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
    def enter_button_event(self,event):
            self.ui.button_back_makeaccountpage.setStyleSheet("border-image : url(Pic/BackBtnEvent.png);")
    def leave_button_event(self,event):
            self.ui.button_back_makeaccountpage.setStyleSheet("border-image : url(Pic/Back_VideoSearchPage.png);")


