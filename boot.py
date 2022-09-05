'''
This is a simple example of how to light a strip of ws2812b pixels with the Raspberry Pi Pico using
a motion detector
'''
import time
from neopixel import NeoPixel
from machine import Pin

# How many pixels do we have?
PIXEL_COUNT = 24

# How long should we keep the light on?
LIGHT_MINUTES = 1

# Which pin controls the light strip?
PIXEL_PIN = Pin(0)

# Which pin controls the motion detector?
DOWN_MOTION_DETECTION_PIN = 1
UP_MOTION_DETECTION_PIN = 2
DARKNESS_DETECTION_PIN = 3

# Define the color we want to use for the light strip
WHITE = (127, 127, 127)

# Define how we want to turn off the light strip
OFF = (0, 0, 0)

# How long should we stay on after detecting motion?
SHINE_TIME = 10
#SHINE_TIME = 60 * LIGHT_MINUTES

pixels = NeoPixel(PIXEL_PIN, PIXEL_COUNT)
down = Pin(DOWN_MOTION_DETECTION_PIN, Pin.IN, Pin.PULL_DOWN)
up = Pin(UP_MOTION_DETECTION_PIN, Pin.IN, Pin.PULL_DOWN)
dark = Pin(DARKNESS_DETECTION_PIN, Pin.IN, Pin.PULL_DOWN)

pixels.fill(OFF)
pixels.write()

while True:
    if dark.value():
        if down.value():
            for i in range(PIXEL_COUNT):
                pixels[i] = WHITE
                pixels.write()
                time.sleep(.5)
            time.sleep(SHINE_TIME)
            pixels.fill(OFF)
            pixels.write()
        elif up.value():
            for i in range(PIXEL_COUNT-1, 0, -1):
                pixels[i] = WHITE
                pixels.write()
                time.sleep(.5)
            time.sleep(SHINE_TIME)
            pixels.fill(OFF)
            pixels.write()


