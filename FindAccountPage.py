from PyQt5 import QtWidgets
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication
import Config
import MyDataBase
class FindAccountPage:
    def __init__(self,revui):
        self.ui = revui
        self.db = MyDataBase.MyDataBase()
        self.getType = Config.Type()
        self.getFont = Config.Setting()
        # IDFIND 버튼 이벤트
        self.ui.button_findidpw[0].mousePressEvent = lambda event: self.idfind_checkform(event)
        self.ui.button_findidpw[0].enterEvent = lambda event: self.enter_idfind_event(event)
        self.ui.button_findidpw[0].leaveEvent = lambda event: self.leave_idfind_event(event)
        # PWFIND 버튼 이벤트
        self.ui.button_findidpw[1].mousePressEvent = lambda event: self.pwfind_checkform(event)
        self.ui.button_findidpw[1].enterEvent = lambda event: self.enter_pwfind_event(event)
        self.ui.button_findidpw[1].leaveEvent = lambda event: self.leave_pwfind_event(event)
        # 돋보기, 재생목록 추가 버튼 비활성화

        # Back 이벤트
        self.ui.button_back_findaccountpage.mousePressEvent = lambda event: self.back_event(event)
        self.ui.button_back_findaccountpage.enterEvent = lambda event: self.enter_button_event(event)
        self.ui.button_back_findaccountpage.leaveEvent = lambda event: self.leave_button_event(event)

    def idfind_checkform(self,event):
        self.namevalue_id = self.ui.inputinfor_findaccountpage[0].text()
        self.numbervalue_id = self.ui.inputinfor_findaccountpage[1].text()
        self.checkname = []
        self.checknum_id = []
        self.checkname_option = True
        self.checknum_id_option = True
        for i in str(self.namevalue_id):
            self.checkname.append(i)
        for i in str(self.numbervalue_id):
            self.checknum_id.append(i) 
        for index in range(0,len(self.checknum_id)):
            if self.checknum_id[index] not in self.getType.intType:
                self.checknum_id_option = False
                break
            else:
                pass
        for index in range(0,len(self.checkname)):
            if self.checkname[index] in self.getType.intType:
                self.checkname_option = False
                break
            elif self.checkname[index] in self.getType.specialText:
                self.checkname_option = False
                break
            elif self.checkname[index] in self.getType.english:
                self.checkname_option = False
                break
            else:
                pass
        self.idfind_logic()

    def idfind_logic(self):
        if len(self.checkname) <= 1 and len(self.checknum_id) != 11:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("이름과 전화번호를 다시 입력해주세요")
            self.dialog.result.show()
        elif len(self.checknum_id) != 11:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("전화번호를 다시 입력해주세요(010-####-####)")
            self.dialog.result.show()
        elif len(self.checkname) <= 1:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("이름을 다시 입력해주세요(한글만 입력 가능합니다.)")
            self.dialog.result.show()
        elif int(self.checknum_id[0]) != 0 or int(self.checknum_id[1]) != 1 or int(self.checknum_id[2]) != 0 or self.checknum_id_option == False:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("전화번호 형식을 지켜주세요 (010~")
            self.dialog.result.show()
        elif self.checkname_option == False:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("이름을 다시 입력해주세요")
            self.dialog.result.show()
        else:
            self.read_inputdata = self.db.read("userInterFace", ["Name","Phonenumber"],[self.namevalue_id,self.numbervalue_id])
            if len(self.read_inputdata) == 0:
                self.dialog = Config.Dialog()
                self.dialog.message.setText("존재하지 않는 계정입니다.")
                self.dialog.result.show()
                self.ui.printidpw_findaccountpage[0].setText("")
            else:
                self.ui.printidpw_findaccountpage[0].setText("ID : " + self.read_inputdata[0][0])
                self.ui.printidpw_findaccountpage[0].setFont(self.getFont.login_font_printinfor)
                self.ui.printidpw_findaccountpage[0].setAlignment(QtCore.Qt.AlignCenter)

    def pwfind_checkform(self,event):
        self.idValue_pw = self.ui.inputinfor_findaccountpage[2].text()
        self.numbervalue_pw = self.ui.inputinfor_findaccountpage[3].text()
        self.checknum_pw = []
        self.checknum_pw_option = True
        for i in str(self.numbervalue_pw):
            self.checknum_pw.append(i) 
        for index in range(0,len(self.checknum_pw)):
            if self.checknum_pw[index] not in self.getType.intType:
                self.checknum_pw_option = False
                break
            else:
                pass
        self.pwfind_logic()
    def pwfind_logic(self):
        if len(self.idValue_pw) == 0 and len(self.checknum_pw) != 11:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("아이디와 전화번호를 입력해주세요")
            self.dialog.result.show()
        elif len(self.idValue_pw) == 0:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("아이디를 입력해주세요")
            self.dialog.result.show()
        elif len(self.checknum_pw) != 11:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("전화번호를 다시 입력해주세요(010-####-####)")
            self.dialog.result.show()
        elif int(self.checknum_pw[0]) != 0 or int(self.checknum_pw[1]) != 1 or int(self.checknum_pw[2]) != 0 or self.checknum_pw_option == False:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("전화번호 형식을 지켜주세요 (010~")
            self.dialog.result.show()
        else:
            self.read_inputdata = self.db.read("userInterFace", ["Id","Phonenumber"],[self.idValue_pw,self.numbervalue_pw])
            if len(self.read_inputdata) == 0:
                self.dialog = Config.Dialog()
                self.dialog.message.setText("존재하지 않는 계정입니다.")
                self.dialog.result.show()
                self.ui.printidpw_findaccountpage[1].setText("")
            else:
                self.getPw = self.db.read("saveIDPW", ["Id"],[self.idValue_pw])
                self.ui.printidpw_findaccountpage[1].setText("PW : " + self.getPw[0][1])
                self.ui.printidpw_findaccountpage[1].setFont(self.getFont.login_font_printinfor)
                self.ui.printidpw_findaccountpage[1].setAlignment(QtCore.Qt.AlignCenter)

    def enter_idfind_event(self,event):
        self.ui.button_findidpw[0].setStyleSheet(
                "border-image : '';"
                "background-color : black;"    
                "border : 4px solid black;"
                "color : white;"
            )
    def leave_idfind_event(self,event):
        self.ui.button_findidpw[0].setStyleSheet(
                "border-image : '';"
                "background-color : darkgrey;"    
                "border : 4px solid black;"
            )
    def pwfind_event(self,event):
        pass
    def enter_pwfind_event(self,event):
        self.ui.button_findidpw[1].setStyleSheet(
                "border-image : '';"
                "background-color : black;"    
                "border : 4px solid black;"
                "color : white;"
            )
    def leave_pwfind_event(self,event):
        self.ui.button_findidpw[1].setStyleSheet(
                "border-image : '';"
                "background-color : darkgrey;"    
                "border : 4px solid black;"
            )
    def enter_button_event(self,event):
        self.ui.button_back_findaccountpage.setStyleSheet("border-image : url(Pic/BackBtnEvent.png);")
    def leave_button_event(self,event):
        self.ui.button_back_findaccountpage.setStyleSheet("border-image : url(Pic/Back_VideoSearchPage.png);")
    def update_event(self,event,index):
        self.ui.pageset += 2
        self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
    def back_event(self,event):
        self.ui.pageset -= 4
        self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
        for index in range(0,2):
            self.ui.inputIDPW[index].clear()

