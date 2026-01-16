#Libraries
import RPi.GPIO as GPIO
import time
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import sys
import time

import Adafruit_SSD1306

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 23
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

# set dcmotor
STEPS_PER_REVOLUTION = 16 * 64
ROUND = 100
SEQUENCE = [[1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 1],
            [1, 0, 0, 1]]


STEPPER_PINS = [17,18,27,22]
for pin in STEPPER_PINS:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

SEQUENCE_COUNT = len(SEQUENCE)
PINS_COUNT = len(STEPPER_PINS)

if len(sys.argv)>1:
    wait_time = int(sys.argv[1])/float(1000)
else:
    wait_time = 10/float(1000)

def turn_basket(sequence_index,direction,steps):
    for pin in range(0, PINS_COUNT):
        GPIO.output(STEPPER_PINS[pin], SEQUENCE[sequence_index][pin])

    steps += direction
    if steps >= STEPS_PER_REVOLUTION:
        direction = -1
    elif steps < 0:
        direction = 1

    sequence_index += direction
    sequence_index %= SEQUENCE_COUNT

    # print('index={}, direction={}'.format(sequence_index, direction))
    time.sleep(0.0001)
    return sequence_index,direction,steps

 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    start_time = time.time()
    stop_time = time.time()
 
    # save start_time
    while GPIO.input(GPIO_ECHO) == 0:
        start_time = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        stop_time = time.time()
 
    # time difference between start and arrival
    time_elapsed = stop_time - start_time
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (time_elapsed * 34300) / 2
 
    return distance


def display_text(text, *args):

    if len(args) < 2:
        FONT_SIZE = 60
    elif len(args) == 2:
        FONT_SIZE = 10
    else:
        FONT_SIZE = 8

    disp = Adafruit_SSD1306.SSD1306_128_64(rst = 0)

    disp.begin()
    disp.clear()
    disp.display()

    width = disp.width
    height = disp.height
    print(width, height)
    # 1 bit pixel
    image = Image.new('1', (width, height))
    # Create a new image (all black) with the binary mode

    draw = ImageDraw.Draw(image)
    # Create an object that can be used to draw in the given image

    font = ImageFont.truetype("./TT0129C_.TTF", FONT_SIZE)

    #try:
    draw.rectangle((0, 0, width, height), outline = 0, fill = 0)

    draw.text((26, -15), text, font = font, fill = 255)

    if len(args) > 0:
        for i, item in enumerate(args):
            draw.text((0, (i + 1) * FONT_SIZE-1), item, font = font, fill = 255)

    disp.image(image)
    disp.display()
    time.sleep(0.4)

    # except KeyboardInterrupt:
    #    print('terminated')

    # finally:
    #    disp.clear()
    #    disp.display()


def main():
    sequence_index = 0
    direction = 1
    steps = 0
    display_text("05")
    for i in range(4,-1,-1):
        time.sleep(3)
        dist = distance()
        while 5 < dist :
            dist = distance()
            sequence_index,direction,steps = turn_basket(sequence_index,direction,steps)
            print(dist)
        os.system("aplay ball.wav")
        display_text("0" + str(i))
        os.system("mpg123 ./goodmorning/greeting5.mp3")        
        os.system("mpg123 ./goodmorning/numbers_audio/"+ str(i) + ".mp3")
        os.system("mpg123 ./goodmorning/greeting6.mp3")
                

if __name__ == "__main__":

    main()



