from os import terminal_size
from PyQt5 import QtWidgets
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication
import Ui
import MyDataBase
import Config
class MakeAccountPage:
    def __init__(self,revui):
        self.ui = revui
        self.db = MyDataBase.MyDataBase()
        self.getFont = Config.Setting()
        self.getType = Config.Type()

       
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
        self.jobList = ["선택","기획 1팀","기획 2팀","제작 1팀","제작 2팀","개발 1팀","개발 2팀","경영지원 1팀","경영지원 2팀"]
        self.classList = ["선택","부장","차장","과장","대리","사원","인턴"]
        for index in range(0,len(self.jobList)):
            self.ui.combobox_makeaccountpage[0].addItem(self.jobList[index])
        self.ui.combobox_makeaccountpage[0].setFont(self.getFont.login_font_printinfor)
        self.ui.combobox_makeaccountpage[0].activated.connect(self.make_account_logic)
        for index in range(0,len(self.classList)):
            self.ui.combobox_makeaccountpage[1].addItem(self.classList[index])
        self.ui.combobox_makeaccountpage[1].setFont(self.getFont.login_font_printinfor)
        self.ui.combobox_makeaccountpage[1].activated.connect(self.make_account_logic)

        # onchange
        for index in range(0,4):
            self.ui.inputinfor_makeaccountpage[index+1].textChanged.connect(self.make_account_logic)
        # 입력 안내
        editLineList = ["ID","PW","Name","Age","Phonenumber"]
        for index in range(0,len(editLineList)):
            self.ui.warning_bar[index].setText("Please type " + editLineList[index])
            self.ui.warning_bar[index].setFont(self.getFont.warning_font)
            self.ui.warning_bar[index].setStyleSheet(
            "color : red;"
            "background-color : #D9D9D9;"
        )
        # 버튼 활성화 조건
        self.ableBtn = [False,False,False,False,False]
        self.block_btn()
    def block_btn(self):
        self.ui.button_makeaccount.setDisabled(True)
        self.ui.button_makeaccount.setStyleSheet(
            "background-color : black;"
            "border-image : '';"
            "color : black;"
        )
        # 콤보박스 데이터 가져옴
    # def get_comboboxdata(self):
    #     self.part = str(self.ui.combobox_makeaccountpage[0].currentText())
    #     self.level = str(self.ui.combobox_makeaccountpage[1].currentText())
    
    def idcheck_event(self,event):
        self.idValue = self.ui.inputinfor_makeaccountpage[0].text()
        self.readInfor = self.db.read("userInterFace",["Id"],[self.idValue])
        checkId = []
        checkid_korean = True
        checkid_specialchar = True
        checkid_length = True
        for i in str(self.idValue):
            checkId.append(i)
        for index in range(0,len(checkId)):
            if checkId[index] in self.getType.korean:
                checkid_korean = False
                break
            elif checkId[index] in self.getType.specialText:
                checkid_specialchar = False
                break
            elif len(checkId) <= 4:
                checkid_length = False
                break
        if len(self.readInfor) == 0 and checkid_korean == True and checkid_specialchar == True and checkid_length == True:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("이 아이디를 사용하실 수 있습니다.")
            self.dialog.result.show()
            self.ui.warning_bar[0].setText("ID Checked")
            self.ui.warning_bar[0].setStyleSheet(
                "color : green;"
                "background-color : #D9D9D9;"
                )
            self.ableBtn[0] = True
            self.ui.inputinfor_makeaccountpage[0].setDisabled(True)

        elif checkid_korean == False:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("이 아이디를 사용하실 수 없습니다.")
            self.dialog.result.show()
            self.ui.warning_bar[0].setText("Cant use Korean in ID")
            self.ui.warning_bar[0].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ableBtn[0] = False

        elif checkid_length == False:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("이 아이디를 사용하실 수 없습니다.")
            self.dialog.result.show()
            self.ui.warning_bar[0].setText("ID length must more than 4 words")
            self.ui.warning_bar[0].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ableBtn[0] = False
        elif checkid_specialchar == False:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("이 아이디를 사용하실 수 없습니다.")
            self.dialog.result.show()
            self.ui.warning_bar[0].setText("Cant use special Char in ID")
            self.ui.warning_bar[0].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ableBtn[0] = False
        elif len(self.readInfor) != 0:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("이 아이디를 사용하실 수 없습니다.")
            self.dialog.result.show()
            self.ui.warning_bar[0].setText("This ID already exists")
            self.ui.warning_bar[0].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ableBtn[0] = False
    def make_account_logic(self):
        self.part = str(self.ui.combobox_makeaccountpage[0].currentText())
        self.level = str(self.ui.combobox_makeaccountpage[1].currentText())
        self.pwValue = self.ui.inputinfor_makeaccountpage[1].text()
        self.nameValue = self.ui.inputinfor_makeaccountpage[2].text()
        self.ageValue = self.ui.inputinfor_makeaccountpage[3].text()
        self.numberValue = self.ui.inputinfor_makeaccountpage[4].text()
        readNumberInfor = self.db.read("userInterFace",["Phonenumber"],[self.numberValue])
        checkPw = []
        checkName = []
        checkAge = []
        checkNumber = []
        checkpw_length = True
        checkpw_korean = True
        # checkpw_form = True
        checkname_length = True
        checkname_specialchar = True
        checkname_english = True
        checkname_int = True
        checkname_korean = True

        checkage_age = True
        checkage_type = True
        checkage_zero = True

        checknumber_type = True #(숫자에 한글,영어입력 제한)
        checknumber_length = True
        checknumber_form = True #(010형식 제어)
        checknumber_list = True
        # 패스워드
        for i in str(self.pwValue):
            checkPw.append(i)
        for index in range(0,len(checkPw)):
            if len(checkPw) < 4:
                checkpw_length = False
                break
            elif checkPw[index] in self.getType.korean:
                checkpw_korean = False
                break
            # elif self.pwValue.isalnum() == False:
            #     checkpw_form = False
            #     break

        # 이름
        for i in str(self.nameValue):
            checkName.append(i)
        for index in range(0,len(checkName)):
            if checkName[index] in self.getType.specialText:
                checkname_specialchar = False
                break
            elif len(checkName) < 2:
                checkname_length = False
                break
            elif checkName[index] in self.getType.english:
                checkname_english = False
                break
            elif checkName[index] in self.getType.intType:
                checkname_int = False
                break
            elif checkName[index] in self.getType.korean:
                checkname_korean = False
                break
        # 나이
        for i in str(self.ageValue):
            checkAge.append(i)
        for index in range(0,len(checkAge)):
            for index in range(0,len(checkAge)):
                if checkAge[index] not in self.getType.intType:
                    checkage_type = False
                    break
                else: 
                    checkage_type = True
            if checkAge[0] == "0":
                checkage_zero = False
                break
            if checkage_type == True:
                if int(self.ageValue) < 20 or int(self.ageValue) > 100:
                    checkage_age = False
                    break

        # if isinstance(self.ageValue, int) == False:
        #     if int(self.ageValue) < 20 or int(self.ageValue) > 100:
        #         checkage_age = False
        # else:
        #     pass
        # 전화번호
        for i in str(self.numberValue):
            checkNumber.append(i)
        for index in range(0,len(checkNumber)):
            if checkNumber[index] not in self.getType.intType:
                checknumber_type = False
                break
            elif len(checkNumber) != 11:
                checknumber_length = False
                break
            elif checkNumber[0] != "0" or checkNumber[1] != "1" or checkNumber[2] != "0":
                checknumber_form = False
                break
            elif len(readNumberInfor) !=0 :
                checknumber_list = False
                break
        ## pw 
        if len(self.pwValue) == 0:
            self.ui.warning_bar[1].setText("Please type PW")
            self.ui.warning_bar[1].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ui.warning_bar[1].setFont(self.getFont.warning_font)
            self.ableBtn[1] = False
        elif checkpw_korean == False:
            self.ui.warning_bar[1].setText("Cant use Korean in PW")
            self.ui.warning_bar[1].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ui.warning_bar[1].setFont(self.getFont.warning_font)
            self.ableBtn[1] = False
        elif checkpw_length == False:
            self.ui.warning_bar[1].setText("Pw must more than 4 words")
            self.ui.warning_bar[1].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ui.warning_bar[1].setFont(self.getFont.warning_font)
            self.ableBtn[1] = False
        # elif checkpw_form == False:
        #     self.ui.warning_bar[1].setText("Make PW combination of English words and numbers.")
        #     self.ui.warning_bar[1].setStyleSheet(
        #         "color : red;"
        #         "background-color : #D9D9D9;"
        #     )
        #     self.ui.warning_bar[1].setFont(self.getFont.warning_font)
        else:
            self.ui.warning_bar[1].setText("Pw checked")
            self.ui.warning_bar[1].setStyleSheet(
                "color : green;"
                "background-color : #D9D9D9;"
            )
            self.ableBtn[1] = True
        ## NAME
        if len(self.nameValue) == 0:
            self.ui.warning_bar[2].setText("Please type Name")
            self.ui.warning_bar[2].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ui.warning_bar[2].setFont(self.getFont.warning_font)
            self.ableBtn[2] = False
        elif checkname_english == False:
            self.ui.warning_bar[2].setText("Cant use English in Name")
            self.ui.warning_bar[2].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ui.warning_bar[2].setFont(self.getFont.warning_font)
            self.ableBtn[2] = False
        elif checkname_specialchar == False:
            self.ui.warning_bar[2].setText("Cant use special Char in Name")
            self.ui.warning_bar[2].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ui.warning_bar[2].setFont(self.getFont.warning_font)
            self.ableBtn[2] = False
        elif checkname_length == False:
            self.ui.warning_bar[2].setText("Name must more than 2 words")
            self.ui.warning_bar[2].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ui.warning_bar[2].setFont(self.getFont.warning_font)
            self.ableBtn[2] = False
        elif checkname_korean == False:
            self.ui.warning_bar[2].setText("You cant use this name")
            self.ui.warning_bar[2].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ui.warning_bar[2].setFont(self.getFont.warning_font)
            self.ableBtn[2] = False
        elif checkname_int == False:
            self.ui.warning_bar[2].setText("Cant use number in Name")
            self.ui.warning_bar[2].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ui.warning_bar[2].setFont(self.getFont.warning_font)
            self.ableBtn[2] = False
        else:
            self.ui.warning_bar[2].setText("Name checked")
            self.ui.warning_bar[2].setStyleSheet(
                "color : green;"
                "background-color : #D9D9D9;"
            )
            self.ableBtn[2] = True
        ## AGE
        if len(self.ageValue) == 0:
            self.ui.warning_bar[3].setText("Please type Age")
            self.ui.warning_bar[3].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ui.warning_bar[3].setFont(self.getFont.warning_font)
            self.ableBtn[3] = False
        elif checkage_age == False:
            self.ui.warning_bar[3].setText("Age must bigger than 20, smaller than 100")
            self.ui.warning_bar[3].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ui.warning_bar[3].setFont(self.getFont.warning_font)
            self.ableBtn[3] = False
        elif checkage_type == False:
            self.ui.warning_bar[3].setText("Only can int type in age")
            self.ui.warning_bar[3].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ui.warning_bar[3].setFont(self.getFont.warning_font)
            self.ableBtn[3] = False
        elif checkage_zero == False:
            self.ui.warning_bar[3].setText("Cant write zero infront")
            self.ui.warning_bar[3].setStyleSheet(
                "color : red;"
                "background-color : #D9D9D9;"
            )
            self.ui.warning_bar[3].setFont(self.getFont.warning_font)
            self.ableBtn[3] = False
        else:
            self.ui.warning_bar[3].setText("Age checked")
            self.ui.warning_bar[3].setStyleSheet(
                "color : green;"
                "background-color : #D9D9D9;"
            )
            self.ableBtn[3] = True 
        ## NUMBER
        if len(self.numberValue) == 0:
            self.ui.warning_bar[4].setText("Please type Number")
            self.ui.warning_bar[4].setStyleSheet(
            "color : red;"
            "background-color : #D9D9D9;"
            )
            self.ableBtn[4] = False 
        elif checknumber_form == False:
            self.ui.warning_bar[4].setText("Please type number 010~")
            self.ui.warning_bar[4].setStyleSheet(
            "color : red;"
            "background-color : #D9D9D9;"
            )
            self.ableBtn[4] = False 
        elif checknumber_length == False:
            self.ui.warning_bar[4].setText("Please type 11 number ex) 01012345678")
            self.ui.warning_bar[4].setStyleSheet(
            "color : red;"
            "background-color : #D9D9D9;"
            )
            self.ableBtn[4] = False 
        elif checknumber_type == False:
            self.ui.warning_bar[4].setText("Type only int. not english,korean,special char")
            self.ui.warning_bar[4].setStyleSheet(
            "color : red;"
            "background-color : #D9D9D9;"
            )
            self.ableBtn[4] = False 
        elif checknumber_list == False:
            self.ui.warning_bar[4].setText("Already used number")
            self.ui.warning_bar[4].setStyleSheet(
            "color : red;"
            "background-color : #D9D9D9;"
            )
            self.ableBtn[4] = False 
        else:
            self.ui.warning_bar[4].setText("Number checked")
            self.ui.warning_bar[4].setStyleSheet(
            "color : green;"
            "background-color : #D9D9D9;"
            )
            self.ableBtn[4] = True 

        if self.ableBtn[0] == True and self.ableBtn[1] == True and self.ableBtn[2] == True and self.ableBtn[3] == True and self.ableBtn[4] == True and self.part != "선택" and self.level != "선택":
            ## 버튼 활성화 ## 
            self.ui.button_makeaccount.setEnabled(True)
            self.ui.button_makeaccount.setStyleSheet(
                "border-image : '';"
                "background-color : grey;"    
                "border : 4px solid black;"
            )
            self.ui.button_makeaccount.mousePressEvent = lambda event: self.makeaccount_event(event)
            self.ui.button_makeaccount.enterEvent = lambda event: self.enter_makeaccountbtn_event(event)
            self.ui.button_makeaccount.leaveEvent = lambda event: self.leave_makeaccountbtn_event(event)


        else:
            self.ui.button_makeaccount.setDisabled(True)
            self.ui.button_makeaccount.setStyleSheet(
            "background-color : black;"
            "border-image : '';"
            "color : black;"
            )

        
    def makeaccount_event(self,event):
        signup_infor = self.db.create("userInterFace",["Id","Name","Age","Phonenumber","TEAM","GRADE"],[self.idValue,self.nameValue,self.ageValue,self.numberValue,self.part,self.level])
        signup_idpw = self.db.create("saveIDPW",["Id","Pw"],[self.idValue,self.pwValue])
        self.ui.pageset -= 5
        self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
        self.dialog = Config.Dialog()
        self.dialog.message.setText("Successed to Sign up.")
        self.dialog.result.show()
        for index in range(0,5):
            self.ui.inputinfor_makeaccountpage[index].clear()

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
        print("1")
        #  self.ui.button_makeaccount.setStyleSheet(
        #         "border-image : '';"
        #         "background-color : black;"    
        #         "border : 4px solid black;"
        #         "color : white;"
        #     )
    def leave_makeaccountbtn_event(self,event):
        print("1")
        # self.ui.button_makeaccount.setStyleSheet(
        #         "border-image : '';"
        #         "background-color : grey;"    
        #         "border : 4px solid black;"
        #     )
    def back_event(self,event):
        self.ui.pageset -= 5
        self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
    def enter_button_event(self,event):
            self.ui.button_back_makeaccountpage.setStyleSheet("border-image : url(Pic/BackBtnEvent.png);")
    def leave_button_event(self,event):
            self.ui.button_back_makeaccountpage.setStyleSheet("border-image : url(Pic/Back_VideoSearchPage.png);")

## makeID 깜빡이는거 안되는 에러 빼고 다 됨.