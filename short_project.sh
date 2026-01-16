# kill the crontab process
#pid_of_stats="$(ps xao pid | grep stats.py)" 
#kill $pid_of_stats
#python3 clear_display.py

# command for Arduino
arduino-cli compile --fqbn arduino:avr:uno lcd_control
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno lcd_control
python3 tmp_humi.py # temperature & humidity txt file
aplay alarm.wav #Speaker(aplay)播放很躁的音樂(或昨天錄出來的美音) 
python3 goodmorning.py #Speaker 播放當前時間「現在時間是上午幾點幾分幾秒」，「今天的氣溫是幾度，濕度為百分之幾」「早安，今天也要乖乖起床喔，請投入五顆球」 
while true; do aplay alarm.wav; done &
python3 short_basketball.py #超音波感測器，感測球有沒有投進，直到五顆球都進，同時，OLED 會不斷顯示投進球數，直到投籃環節完成。同時，Speaker 會繼續播放很躁的音樂(或昨天錄出來的美音)，當球投進的時候，會有華麗的進球音樂，再說「早安，今天也要乖乖起床喔，請投入幾顆球」，在繼續播放音樂 #import ultrasonic #import oled #aplay
ppid_of_aplay="$(ps xao pid,ppid,pgid,sid,comm | grep aplay | awk '{print $2}')"
kill $ppid_of_aplay
correct=0
while [ $correct -ne 1 ]; do
    python3 question.py #speaker 問室友「二十五加二十五加三十等於?」或是機智問答「小明的媽媽有四個小孩，老大叫大寶，老二叫二寶，老三叫三寶，請問老四叫什麼?」(問題 15 個) #import random
    aplay question.wav 
    python3 record5.py --num=3 #麥克風錄音 3 秒要聽室友回答什麼
    aplay recording3.wav 
    python3 mi2s_asr.py --num=3 > my_ans.txt #並且丟給 speech to text(asr) 
    cat my_ans.txt
    correct=$((python3 short_check_answer.py) 2>&1) #然後檢查答案是否正確(正確率 50%即可)
    echo "$correct" 
done
mpg123 experience.mp3 #Speaker 詢問「接下來您有五秒鐘可以回答，請問您對今天的裝置使用體驗如何，請在逼聲後開始回答。逼」 
python3 record5.py #麥克風錄音 5 秒 

python3 change_alarm.py #檢查錄音檔案的 Energy，如果大於某個 threshold，就將它設為隔天的鬧鐘 
