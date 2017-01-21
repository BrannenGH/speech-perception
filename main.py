#!/usr/bin/python3

import pyaudio
import wave
import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle('Sample')
    window.adjustSize()
    window.show()
