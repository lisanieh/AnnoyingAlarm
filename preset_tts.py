from gtts import gTTS
import socket
import urllib
import os


def ch_tts(text, file_):
    tts = gTTS(text, lang="zh-tw")
    tts.save(file_ + ".wav")


if __name__ == "__main__":
    while True:
        try:
            urllib.request.urlopen("http://www.google.com")
        except urllib.error.URLError:
            print("Fail to connect Internet...")
            os.system("")
            time.sleep(1)
        else:
            print("Connected")
            tts = gTTS(text="現在時間是", lang="zh-tw")
#            tts.save("greeting1.mp3")
           
            tts = gTTS(text="點", lang="zh-tw")
#            tts.save("time.mp3")
            
            tts = gTTS(text="分", lang="zh-tw")
#            tts.save("minute.mp3")
            
            tts = gTTS(text="秒", lang="zh-tw")
#            tts.save("second.mp3")

            tts = gTTS(text="今天的氣溫是", lang="zh-tw")
#            tts.save("greeting2.mp3")
            
            tts = gTTS(text="度", lang="zh-tw")
#            tts.save("greeting3.mp3")

            tts = gTTS(text="濕度為百分之", lang="zh-tw")
#            tts.save("greeting4.mp3")

            tts = gTTS(text="早安，今天也要乖乖起床喔，請投入", lang="zh-tw")
            tts.save("greeting5.mp3")
            
            tts = gTTS(text="顆球", lang="zh-tw")
#            tts.save("greeting6.mp3")
            
            tts = gTTS(text="上午", lang="zh-tw")
#            tts.save("morning.mp3")

            tts = gTTS(text="下午", lang="zh-tw")
#            tts.save("afternoon.mp3")
            
            tts = gTTS(text="晚上", lang="zh-tw")
#            tts.save("night.mp3")
            
            tts = gTTS(text="接下來您有五秒鐘可以回答，請問您對今天的裝置使用體驗如何，請在逼聲後開始回答。逼", lang="zh-tw")
#            tts.save("experience.mp3")
            
            for i in range(61,101,1):
                tts = gTTS(text=str(i), lang="zh-tw")
                tts.save("./goodmorning/numbers_audio/"+str(i)+".mp3")

            break
