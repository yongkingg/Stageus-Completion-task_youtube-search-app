# import vlc
# import pafy
# import urllib.request 

# url = 'https://www.youtube.com/watch?v=4poNayP6bBs'
# try:
#     video = pafy.new(url)
# except KeyError:
#     pass
# best = video.getbest()
# playurl = best.url
# ins = vlc.Instance() 
# player = ins.media_player_new() 
# code = urllib.request.urlopen(url).getcode() 
# if str(code).startswith('2') or str(code).startswith('3'):
#     print('Stream is working')
# else:
#     print('Stream is dead')
# Media = ins.media_new(playurl)  
# Media.get_mrl()
# player.set_media(Media)
# player.play()
# good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
# while str(player.get_state()) in good_states:
#     print('Stream is working. Current state = {}'.format(player.get_state()))
# print('Stream is not working. Current state = {}'.format(player.get_state()))
# player.stop()

# import vlc
# import pafy
# import urllib.request 

# url = 'https://www.youtube.com/watch?v=4poNayP6bBs'
# video = pafy.new(url)
# print(f"영상제목: {video.title}")
# print(f"별점: {video.rating}")
# print(f"제작자: {video.author}")
# print(f"플레이길이(초): {video.length}")
# print(f"플레이시간: {video.duration}")
# print(f"유투브ID: {video.videoid}")

import vlc
import pafy
import urllib.request 

url = 'https://www.youtube.com/watch?v=4poNayP6bBs'
try:
    video = pafy.new(url)
except KeyError:
    pass
audio_url = video.getbestaudio(preftype="m4a").url

try:
    video = pafy.new(audio_url)
except KeyError:
    pass
best = video.getbest()
playurl = best.audio_url
ins = vlc.Instance() 
player = ins.media_player_new() 
code = urllib.request.urlopen(audio_url).getcode() 
if str(code).startswith('2') or str(code).startswith('3'):
    print('Stream is working')
else:
    print('Stream is dead')
Media = ins.media_new(playurl)  
Media.get_mrl()
player.set_media(Media)
player.play()
good_states = ["State.Playing", "State.NothingSpecial", "State.Opening"]
while str(player.get_state()) in good_states:
    print('Stream is working. Current state = {}'.format(player.get_state()))
print('Stream is not working. Current state = {}'.format(player.get_state()))
player.stop()
