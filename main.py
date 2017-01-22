#!/usr/bin/python3

import sys
import alsaaudio
import wave
from PyQt5.QtWidgets import *

#Since I am going to only be using this on one device, I hard coded the audio card name
card = ''
if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Sample')
    window.adjustSize()
    window.move(300, 300)
    window.show()

    sys.exit(app.exec_())

def main():
    rec_dev = alsaaudio.PCM(alsaaudio.PCM_CAPTURE, alsaaudio.PCM_NONBLOCK, card)
