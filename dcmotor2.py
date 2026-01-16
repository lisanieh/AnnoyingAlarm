import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

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

sequence_index = 0
direction = 1
steps = 0

if len(sys.argv)>1:
  wait_time = int(sys.argv[1])/float(1000)
else:
  wait_time = 10/float(1000)

def turn_basket(steps,direction,sequence_index):
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
    time.sleep(wait_time)
    return steps,direction,sequence_index

try:
    print('按下 Ctrl-C 可停止程式')
    print('motor turning')
    for i in range(STEPS_PER_REVOLUTION*ROUND):
        steps,direction,sequence_index = turn_basket(steps,direction,sequence_index)
except KeyboardInterrupt:
    print('關閉程式')
finally:
    GPIO.cleanup()

