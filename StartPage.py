from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import QCoreApplication
import Ui
import MyDataBase
import Setting
import PlayListPage
import FindAccountPage
import MakeAccountPage
import VideoSearchPage
import ManageInforPage
import VideoPage
# setting => config
class StartPage:
    def __init__(self):
        self.ui = Ui.Ui()
        self.db = MyDataBase.MyDataBase() 
        # self.videoSearchPage = VideoSearchPage.VideoSearchPage(self.ui)
        # self.manageInforPage = ManageInforPage.ManageInforPage(self.ui)
        # self.videoPage = VideoPage.VideoPage(self.ui)
        # self.ui.inputIDPW[0].setPlaceholderText("ID")
        # self.ui.inputIDPW[1].setPlaceholderText("PW")
    #     # 로그인,회원가입,아이디 찾기 버튼 활성화
    #     for index in range(0,3):
    #         if index == 0:
    #             self.ui.button_startpage[index].mousePressEvent = lambda event, num = index: self.login_event(event, num)
    #         elif index == 1:
    #             self.ui.button_startpage[index].mousePressEvent = lambda event, num = index: self.makeaccount_event(event, num)
    #         else:
    #             self.ui.button_startpage[index].mousePressEvent = lambda event, num = index: self.findaccount_event(event, num)
    #         self.ui.button_startpage[index].enterEvent = lambda event, num = index: self.enter_event(event,num)
    #         self.ui.button_startpage[index].leaveEvent = lambda event, num = index: self.leave_event(event,num)
    #     # X버튼 활성화
    #     for index in range(0,len(self.ui.button_exit)):
    #         self.ui.button_exit[index].mousePressEvent = lambda event, num = index: self.exit_event(event,num)
    #         self.ui.button_exit[index].enterEvent = lambda event, num = index: self.enter_exit_event(event,num)
    #         self.ui.button_exit[index].leaveEvent = lambda event, num = index: self.leave_exit_event(event,num)
    # def exit_event(self,event,index):
    #     self.ui.mainWindow.close()
    # def enter_exit_event(self,event,index):
    #     self.ui.button_exit[index].setStyleSheet("border-image:url(Pic/ExitEvent.png);")
    # def leave_exit_event(self,event,index):
    #     self.ui.button_exit[index].setStyleSheet("border-image:url(Pic/Exit.png);")
    # def login_event(self, event, index):
    #     self.idValue = self.ui.inputIDPW[0].text()
    #     self.pwValue = self.ui.inputIDPW[1].text()
    #     readidwpw_login = self.db.read("saveIDPW",["Id","Pw"],[self.idValue,self.pwValue])
    #     # 아이디나 비밀번호 중 하나라도 입력하지 않은 경우
    #     if len(self.idValue) == 0 or len(self.pwValue) == 0:
    #         self.dialog = Setting.Dialog()
    #         self.dialog.message.setText(" 로그인 실패. 아이디와 비밀번호를 모두 입력해주세요")
    #         self.dialog.result.show()      
    #     else:
    #         # 로그인 되는 경우
    #         if len(readidwpw_login) == 1: 
    #             self.ui.pageset += 1
    #             self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
    #             self.sendIdValue = PlayListPage.PlayListPage(self.ui,self.idValue)
    #         else:
    #             self.dialog = Setting.Dialog()
    #             self.dialog.message.setText(" 로그인 실패. 아이디와 비밀번호를 확인해주세요")
    #             self.dialog.result.show()      
    # def enter_event(self, event, index):
    #     self.ui.button_startpage[index].setStyleSheet(
    #             "background-color: darkgrey;" # 배경
    #             "border-image: url'';" #이미지 넣는법
    #             "border : 2px solid black;" # 테두리 
    #     )
    # def leave_event(self, event, index):
    #     self.ui.button_startpage[index].setStyleSheet(
    #             "background-color: lightgrey;" # 배경
    #             "border-image: url'';" #이미지 넣는법
    #             "border : 2px solid black;" # 테두리 
    #     )
    # def makeaccount_event(self, event, index):
    #     self.ui.pageset += 5
    #     self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
    #     self.makeAccountPage = MakeAccountPage.MakeAccountPage(self.ui)
    # def findaccount_event(self, event, index):
    #     self.ui.pageset += 4
    #     self.ui.stackedWidget.setCurrentIndex(self.ui.pageset)
    #     self.findAccountPage = FindAccountPage.FindAccountPage(self.ui)
        


if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    var = StartPage()
    sys.exit(app.exec_())                              


