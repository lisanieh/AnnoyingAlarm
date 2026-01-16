from datetime import datetime
import os
import time

PATH = "./goodmorning/"
now = datetime.now()

hour = str(int(now.strftime("%H")))
minute = str(int(now.strftime("%M")))
second = str(int(now.strftime("%S")))
is_morning = "morning"
with open("temp_mos.txt", "r") as f:
    temp = f.readline().split("\n")[0].split(".")[0]
    mos = f.readline().split("\n")[0].split(".")[0]
    f.close()

if int(hour) > 17:
    is_morning = "night"
elif int(hour) > 12:
    is_morning = "afternoon"

os.system("mpg123 "+ PATH + "greeting1.mp3") #現在時間是
os.system("mpg123 "+ PATH + is_morning+".mp3") 
os.system("mpg123 "+ PATH + "numbers_audio/"+hour+".mp3") #點
os.system("mpg123 "+PATH + "time.mp3")
os.system("mpg123 "+PATH + "numbers_audio/"+minute+".mp3") #分
os.system("mpg123 "+PATH + "minute.mp3")
os.system("mpg123 "+PATH + "numbers_audio/"+second+".mp3") #秒
os.system("mpg123 "+PATH + "second.mp3")
time.sleep(0.5)
os.system("mpg123 "+PATH + "greeting2.mp3") #今天的氣溫是


os.system("mpg123 "+PATH + "numbers_audio/"+temp+".mp3")
os.system("mpg123 "+PATH + "greeting3.mp3") #度
os.system("mpg123 "+PATH + "greeting4.mp3") #濕度為百分之
os.system("mpg123 "+PATH + "numbers_audio/" + mos + ".mp3")
os.system("mpg123 "+PATH + "greeting5.mp3") #早安，今天也要乖乖起床喔，請投入五顆球
