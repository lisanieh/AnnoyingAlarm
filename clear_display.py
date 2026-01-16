import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image

# Raspberry Pi pin configuration:
RST = 0
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

def clear_display():

    disp = Adafruit_SSD1306.SSD1306_128_64(rst = 0)

    disp.begin()
    disp.clear()
    disp.display()

    time.sleep(0.4)


clear_display()
