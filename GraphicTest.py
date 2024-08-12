# Example functions to use display on RP2040-LCD-0.96
# Based on graphicstest.py
# This Test Programme requires GraphicTestLib.py which is a modified version of ST7735.PY
# Dependencies:
#               Firmware used: pico_micropython_20210121.uf2
#               ST7735G.py Library file
#               Robot.BMP image

import ST7735G as lib
from ST7735G import TFT
from sysfont import sysfont
from machine import SPI,Pin
import time
import math

spi = SPI(1, baudrate=20000000, sck=Pin(10), mosi=Pin(11))
tft=TFT(spi,8,12,9) #DC,RST,CS

tft.initr()
tft.rgb(False)
tft.invertcolor(True) # otherwise image is inverted
tft.rotation(3)
time.sleep(0.1)


tft.fill(TFT.BLACK)
tft.text((30, 34), "RP2040", TFT.GREEN, sysfont, 3)
tft.text((35, 70), "LCD-0.96", TFT.YELLOW, sysfont, 2)
tft.rect((1, 26), (tft.size()[0]-1, tft.size()[1]-49), TFT.BLUE)
time.sleep(1)

# the screen initial X seems to be 1 and Y seems to be 26 pixels (0,0) == (1,27)
# Realistically can only use Font 1 and 2

#Format Text to fill the screen
tft.fill(TFT.BLACK);
v = 26 # initial Y position that represents 0
tft.text((1, v), "Hello World!", TFT.RED, sysfont, 1, nowrap=True)
v += sysfont["Height"]
tft.text((1, v), "Hello World!", TFT.YELLOW, sysfont, 2, nowrap=True)
v += sysfont["Height"] * 2
tft.text((1, v), "Hello ....", TFT.GREEN, sysfont, 3, nowrap=True)
v += sysfont["Height"] * 3
tft.text((1, v), str(1234.567), TFT.BLUE, sysfont, 4, nowrap=True)
time.sleep(2)


tft.fill(TFT.RED)
time.sleep(0.3)
tft.fill(TFT.WHITE)
time.sleep(0.3)
tft.fill(TFT.MAROON)
time.sleep(0.3)
tft.fill(TFT.GREEN)
time.sleep(0.3)
tft.fill(TFT.FOREST)
time.sleep(0.3)
tft.fill(TFT.BLUE)
time.sleep(0.3)
tft.fill(TFT.NAVY)
time.sleep(0.3)
tft.fill(TFT.CYAN)
time.sleep(0.3)
tft.fill(TFT.YELLOW)
time.sleep(0.3)
tft.fill(TFT.PURPLE)
time.sleep(0.3)
tft.fill(TFT.GRAY)
time.sleep(0.3)
tft.fill(TFT.BLACK)
time.sleep(0.3)


#Fill Screen with Text Font 1 * only can do with Black background
tft.fill(TFT.BLACK)
tft.text((1, 26), "1234567890 ABCDEFGHIJ 2234567890 ABCDEFGHIJ 3234567890 ABCDEFGHIJ 4234567890 ABCDEFGHIJ 5234567890 ABCDEFGHIJ 6234567890 ABCDEFGHIJ 7234567890 ABCDEFGHIJ 8234567890 ABCDEFGHIJ 9234567890 ABCDEFGHIJ 0234567890",TFT.YELLOW, sysfont, 1)
time.sleep(2)

#Spacing between font sizes and screen fill
tft.fill(TFT.BLACK)
tft.text((1, 26), "Line 1- Font 2", TFT.WHITE, sysfont, 2)
tft.text((1, 45), "Line 2--------------Font 1", TFT.RED, sysfont, 1)
tft.text((1, 55), "Line 3--------------Font 1", TFT.GREEN, sysfont, 1)
tft.text((1, 65), "Line 4--------------Font 1", TFT.YELLOW, sysfont, 1)
tft.text((1, 75), "Line 5--------------Font 1", TFT.BLUE, sysfont, 1)
tft.text((1, 85), "Line 6--------------Font 1", TFT.FOREST, sysfont, 1)
time.sleep(2)

# Formatted Text to Fill Screen
tft.fill(TFT.BLACK);
v = 26
tft.text((1, v), "Hello Again!", TFT.RED, sysfont,2)
v += 20
tft.text((1, v), "Want is pi? ", TFT.GREEN, sysfont)
tft.text((len("Want is pi? ")*sysfont["Width"]+10, v), str(math.pi), TFT.GREEN, sysfont)
v += sysfont["Height"] + 4
tft.text((1, v), "Print HEX: ", TFT.GREEN, sysfont)
tft.text((len("Print HEX: ")*sysfont["Width"]+10, v), hex(8675309), TFT.GREEN, sysfont)
v += sysfont["Height"] + 10
tft.text((1, v), "Sketch has been Running", TFT.WHITE, sysfont)
v += sysfont["Height"]+1
tft.text((1, v), "for: ", TFT.WHITE, sysfont)
tft.text((len("for: ")*sysfont["Width"]+10, v), str(time.ticks_ms() / 1000), TFT.PURPLE, sysfont)
tft.text((100, v), " seconds.", TFT.WHITE, sysfont)
time.sleep(2)


# Draw Blue Rectangles
tft.fill(TFT.BLACK);
for x in range(1,tft.size()[0]-1,6):
    tft.rect((tft.size()[0]//2 - x//2, tft.size()[1]//2 - x/2), (x, x), TFT.BLUE)


# Draw Circle
#tft.circle(aPos, aRadius, aColor)
tft.circle( (80, 63), 25, TFT.YELLOW)

# Fill Circle
#tft.fillcircle(aPos, aRadius, aColor)
tft.fillcircle( (80, 63), 24, TFT.BLUE)

#tft.rect((1, 26), (159, 79), TFT.YELLOW)
#print(tft.size()[0]-1, tft.size()[1]-49)
tft.rect((1, 26), (tft.size()[0]-1, tft.size()[1]-49), TFT.YELLOW)

# Draw Line
#tft.line(aStart, aEnd, aColor)
tft.line( (80, 30), (80, 98), TFT.YELLOW )
tft.line( (45, 64), (115, 64), TFT.YELLOW )

time.sleep(2)
# the image needs to be W128 H160 but it only displays W90xH160 like Robot.bmp
tft.rgb(False)
tft.invertcolor(True) # otherwise image is inverted
tft.fill(TFT.BLACK)
#tft.ScreenSize = (128, 160)
tft.rotation(0)
time.sleep(0.1)

f=open('Robot.bmp', 'rb')
if f.read(2) == b'BM':  #header
    dummy = f.read(8) #file size(4), creator bytes(4)
    offset = int.from_bytes(f.read(4), 'little')
    hdrsize = int.from_bytes(f.read(4), 'little')
    width = int.from_bytes(f.read(4), 'little')
    height = int.from_bytes(f.read(4), 'little')
    if int.from_bytes(f.read(2), 'little') == 1: #planes must be 1
        depth = int.from_bytes(f.read(2), 'little')
        if depth == 24 and int.from_bytes(f.read(4), 'little') == 0:#compress method == uncompressed
            rowsize = (width * 3 + 3) & ~3
            print("Image size:", width, "x", height, "Offset", offset, "rowsize", rowsize)
            offset= 0
            if height < 0:
                height = -height
                flip = False
            else:
                flip = True
            w, h = width, height
            if w > 128: w = 128
            if h > 160: h = 160
            tft._setwindowloc((0,0),(w - 1,h - 1))
            for row in range(h):
                if flip:
                    pos = offset + (height - 1 - row) * rowsize
                else:
                    pos = offset + row * rowsize
                if f.tell() != pos:
                    dummy = f.seek(pos)
                for col in range(w):
                    bgr = f.read(3)
                    tft._pushcolor(lib.TFTColor(bgr[2],bgr[1],bgr[0]))
spi.deinit()
tft.rotation(3)

time.sleep(2)
tft.text((83, 90), "THE END", TFT.YELLOW, sysfont, 2)

time.sleep(2)
