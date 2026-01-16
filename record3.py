"""
copyright WMMKSLab Gbanyan

modified by wwolfyTC 2019/1/24
"""
import time
import threading
import socket
import struct
import re
import os
import sys
from subprocess import call
from enum import Enum, unique
from traceback import print_exc
import argparse

from aiy.board import Board
from aiy.voice.audio import AudioFormat, play_wav, record_file, Recorder

Lab = AudioFormat(sample_rate_hz=16000, num_channels=1, bytes_per_sample=2)


def record(string):
    print("開始錄音")
    def wait():
        start = time.monotonic()
        start_time = time.time()
        while time.time() - start_time <= 3:
            print(time.time() - start_time)
            duration = time.monotonic() - start
            print("錄音中: %.02f 秒 [共錄製3秒]" % duration)
            time.sleep(0.5)


    record_file(Lab, filename="recording"+string+".wav", wait=wait, filetype="wav")
    time.sleep(1)

def main(string):
#    while True:
    record(string)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "--num",
            type=str,
            default="0"
    )
    arg = parser.parse_args()
    main(arg.num)


