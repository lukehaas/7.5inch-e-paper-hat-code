##
 #  @filename   :   epdif.py
 #  @brief      :   EPD hardware interface implements (GPIO, SPI)
 #  @author     :   Yehui from Waveshare
 #
 #  Copyright (C) Waveshare     July 10 2017
 #
 # Permission is hereby granted, free of charge, to any person obtaining a copy
 # of this software and associated documnetation files (the "Software"), to deal
 # in the Software without restriction, including without limitation the rights
 # to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 # copies of the Software, and to permit persons to  whom the Software is
 # furished to do so, subject to the following conditions:
 #
 # The above copyright notice and this permission notice shall be included in
 # all copies or substantial portions of the Software.
 #
 # THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 # IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 # FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 # AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 # LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 # OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 # THE SOFTWARE.
 #

import spidev
import RPi.GPIO as GPIO
import time

# Pin definition
RST_PIN         = 17
DC_PIN          = 25
CS_PIN          = 8
BUSY_PIN        = 24


BCM2 = 3
BCM3 = 5
BCM4 = 7
BCM17 = 11
BCM27 = 13
BCM22 = 15
# BCM10 = 17
BCM9 = 21
BCM11 = 23
BCM0 = 27
BCM5 = 29
BCM6 = 31
BCM13 = 33
BCM19 = 35
BCM26 = 37
# BCM14 = 8
BCM15 = 10
BCM18 = 12
BCM23 = 16
BCM24 = 18
BCM25 = 22
# BCM8 = 24
BCM7 = 26
BCM1 = 28
BCM12 = 32
BCM16 = 36
BCM20 = 38
BCM21 = 40


# SPI device, bus = 0, device = 0
SPI = spidev.SpiDev(0, 0)

def epd_digital_write(pin, value):
    GPIO.output(pin, value)

def epd_digital_read(pin):
    return GPIO.input(BUSY_PIN)

def epd_delay_ms(delaytime):
    time.sleep(delaytime / 1000.0)

def spi_transfer(data):
    SPI.writebytes(data)

def epd_init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(RST_PIN, GPIO.OUT)
    GPIO.setup(DC_PIN, GPIO.OUT)
    GPIO.setup(CS_PIN, GPIO.OUT)
    GPIO.setup(BUSY_PIN, GPIO.IN)



    GPIO.setup(BCM2, GPIO.IN)
    # GPIO.setup(BCM3, GPIO.IN)
    # GPIO.setup(BCM4, GPIO.IN)
    # GPIO.setup(BCM17, GPIO.IN)
    # GPIO.setup(BCM27, GPIO.IN)
    # GPIO.setup(BCM22, GPIO.IN)
    # GPIO.setup(BCM9, GPIO.IN)
    # GPIO.setup(BCM11, GPIO.IN)
    # GPIO.setup(BCM0, GPIO.IN)
    # GPIO.setup(BCM5, GPIO.IN)
    # GPIO.setup(BCM6, GPIO.IN)
    # GPIO.setup(BCM13, GPIO.IN)
    # GPIO.setup(BCM19, GPIO.IN)
    # GPIO.setup(BCM26, GPIO.IN)
    # GPIO.setup(BCM15, GPIO.IN)
    # GPIO.setup(BCM18, GPIO.IN)
    # GPIO.setup(BCM23, GPIO.IN)
    # GPIO.setup(BCM24, GPIO.IN)
    # GPIO.setup(BCM25, GPIO.IN)
    # GPIO.setup(BCM7, GPIO.IN)
    # GPIO.setup(BCM1, GPIO.IN)
    # GPIO.setup(BCM12, GPIO.IN)
    # GPIO.setup(BCM16, GPIO.IN)
    # GPIO.setup(BCM20, GPIO.IN)
    # GPIO.setup(BCM21, GPIO.IN)


    SPI.max_speed_hz = 2000000
    SPI.mode = 0b00
    return 0;

### END OF FILE ###
