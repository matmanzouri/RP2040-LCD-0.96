# RP2040-LCD-0.96
Example code to use RP2040-LCD-0.96



It seems that there is not enough information on the RP2040-LCD-0.96 that I could find on line.

When the RP2040-LCD-0.96 arrived it had CircuitPython on it and I couldn’t access the Virtual Drive as it was running the sample colour blink test program and wouldn’t let me break into it.

The official website seems to use Circuitpython, but all my Pico processors are running on micropython, so first I had to put the pico_micropython_20210121.uf2 from https://github.com/waveshare/Pico_code/blob/main/Python/pico_micropython_20210121.uf2 
The displays are connected to SPI pins and I managed to find three working examples to run the display:
These examples are all working:
	pico-LCD-0.96.py
	WS_0-96_160x80_MIN.py
	graphicstest.py (which needs sysfont.py)
however this was not a workable solution for me to use. I had to split the functions in a separate, module and create a test programme to use as my base for any project that I need this processor.

![20240813_083423](https://github.com/user-attachments/assets/c3657bc8-787d-4498-a4cc-5451ca208107)

