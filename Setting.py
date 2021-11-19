from PyQt5 import QtCore, QtGui, QtWidgets
class Setting:
    def __init__(self):
        self.login_font = QtGui.QFont()
        self.login_font.setFamily("Microsoft JhengHei UI")
        self.login_font.setPointSize(30)
        self.search_video_font = QtGui.QFont()
        self.search_video_font.setFamily("Microsoft JhengHei UI")
        self.search_video_font.setPointSize(20)
        self.search_video_font.setPixelSize(20)
        self.login_font_printinfor = QtGui.QFont()
        self.login_font_printinfor.setFamily("HY울릉도B")
        self.login_font_printinfor.setPointSize(20)
        self.login_font_printinfor.setPixelSize(20)
        
        self.findidpw_font = QtGui.QFont()
        self.findidpw_font.setFamily("HY울릉도B")
        self.findidpw_font.setPointSize(30)
        self.findidpw_font.setPixelSize(30)

        self.login_font_guide = QtGui.QFont()
        self.login_font_guide.setFamily("HY울릉도B")
        self.login_font_guide.setPointSize(15)
        self.login_font_guide.setPixelSize(15)

class Dialog:
    def __init__(self):
        self.result = QtWidgets.QDialog()
        self.result.resize(300,50)
        self.message = QtWidgets.QLabel(self.result) 
        self.message.resize(400,50)
        self.message.move(0,0)
class Type:
    def __init__(self):
        self.intType = ["1","2","3","4","5","6","7","8","9","0"]
        self.specialText = ["!","@","#","$","%","^","&","*","(",")","_","+","=",".","?","/","<",">","|","\\",".",","]
        self.english = ["q","Q","w","W","e","E","r","R","t","T","y","Y","u","U","i","I","o","O","p","P","a","A","s","S","d","D","f","F","g","G","h","H","j","J","k","K","l","L","z","Z","x","X","c","C","v","V","b","B","n","N","m","M"]
     