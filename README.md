# rpi_project
## 躁躁起床記 : 鬧鐘大挑戰

**Gadgets**

1. speaker:播音樂、當前時間、天氣、濕度
2. OLED:顯示當前投進球數
3. 超音波感測器:感測物體是否命中目標
4. 步進馬達:旋轉籃框
5. Mic:錄製使用者回答
6. 溫濕度感測器:檢測當前的溫、濕度
7. LCD:顯示當前的時間、天氣、狀態

**Process**
1.	溫溼度感測器 : 感測溫溼度
2.	Speaker(aplay)播放很躁的音樂(或昨天錄出來的美音)
3.	步進馬達開始旋轉，帶動籃框旋轉
4.	Speaker播放當前時間「現在時間是上午幾點幾分幾秒」，「今天的氣溫是幾度，濕度為百分之幾」「早安，今天也要乖乖起床喔，請投入五顆球」
5.	LCD顯示當前時間與溫濕度(持續顯示直到系統結束)
6.	超音波感測器，感測球有沒有投進，直到五顆球都進。同時，Speaker會繼續播放很躁的音樂(或昨天錄出來的美音)，當球投進的時候，會有華麗的進球音樂，再說「早安，今天也要乖乖起床喔，請投入幾顆球」，在繼續播放音樂
7.	OLED會不斷顯示投進球數，直到投籃環節完成
8.	speaker問室友問題，共15個
9.	麥克風錄音要聽室友回答什麼，並且丟給speech to text(asr)，然後檢查答案是否正確(正確率50%即可)
10.	Speaker詢問「接下來您有五秒鐘可以回答，請問您對今天的裝置使用體驗如何，請在逼聲後開始回答。逼」
11.	麥克風錄音5秒
12.	檢查錄音檔案的Energy，如果大於某個threshold，就將它設為隔天的鬧鐘

**Liscense**

This project utilizes a proprietary TTS/STT engine provided by Mi2S. Due to licensing restrictions, the core library and access tokens are excluded from this repository. However, the integration logic can be found in mi2s_asr_exp.py
