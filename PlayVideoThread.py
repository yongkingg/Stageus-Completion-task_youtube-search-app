import threading
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import random
import Config
import pafy
import vlc
import time
import urllib.request
import re
class VideoThread(threading.Thread):
    def __init__(self,revui):
        threading.Thread.__init__(self)
        self.ui = revui
        self.search_keyword = self.ui.searchvideo_videosearchpage.text()
        self.search_keyword = self.search_keyword.replace(" ","")
        
        if len(self.search_keyword) == 0:
            self.dialog = Config.Dialog()
            self.dialog.message.setText("Please enter the search word")
            self.dialog.result.show()
        else:
            self.run()

    def control(self):
        pass
    def run(self): 
        if self.search_keyword.encode().isalpha(): # 영어로만 이루어진 경우
                html =  urllib.request.urlopen("https://www.youtube.com/results?search_query=" + self.search_keyword)
                video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())
                url = "https://www.youtube.com/watch?v=" + video_ids[0]
                try:
                    video = pafy.new(url)
                except KeyError:
                    video = pafy.new(url)
                best = video.streams[0]
                media = vlc.MediaPlayer(best.url)
                media.play()
                time.sleep(20)
        else: # 혼합
            search = str(self.search_keyword.encode('utf-8'))
            search = search.replace("\\x","%")
            search = search.replace("'","")
            html =  urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search[1:])
            video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())
            url = "https://www.youtube.com/watch?v=" + video_ids[0]
            try:
                video = pafy.new(url)
            except KeyError:
                video = pafy.new(url)
            best = video.streams[0]
            media = vlc.MediaPlayer(best.url)
            media.play()
            time.sleep(20)