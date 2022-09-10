"""
This is an example of how to control a strip of ws2812b strip lights on a stairway. There are two motion detectors. One
is at the top of the stairs, and the other is at the bottom of the stairs. To control all of them is a light sensor
to detect if its dark enough to justify having the stairs lit.
"""
import time
from neopixel import NeoPixel
from machine import Pin


def top_to_bottom(strip, pixel_count, color):
    """
    This is a function to control the top of the stairs.
    :param strip: The ws2812b strip
    :param pixel_count: The number of pixels in the pixels strip
    :param color: The color of the pixels strip
    """
    for i in range(pixel_count):
        strip[i] = color
        strip.write()


def bottom_to_top(strip, pixel_count, color):
    """
    This is a function to control the bottom of the stairs.
    :param strip: The ws2812b strip
    :param pixel_count: The number of pixels in the pixels strip
    :param color: The color of the pixels strip
    """
    for i in range(pixel_count - 1, 0, -1):
        strip[i] = color
        strip.write()


# How many pixels do we have?
PIXEL_COUNT = 300

# How long should we keep the light on?
LIGHT_MINUTES = 3

# Which pin controls the light strip?
PIXEL_PIN = Pin(0)

# Which pin controls the motion detector?
DOWN_MOTION_DETECTION_PIN = 1
UP_MOTION_DETECTION_PIN = 2

# Which pin controls the light sensor?
DARKNESS_DETECTION_PIN = 3

# Define the color we want to use for the light strip
WHITE = (16, 16, 16)

# Define how we want to turn off the light strip
OFF = (0, 0, 0)

# How long should we stay on after detecting motion?
SHINE_TIME = 60 * LIGHT_MINUTES

pixels = NeoPixel(PIXEL_PIN, PIXEL_COUNT)
down = Pin(DOWN_MOTION_DETECTION_PIN, Pin.IN, Pin.PULL_DOWN)
up = Pin(UP_MOTION_DETECTION_PIN, Pin.IN, Pin.PULL_DOWN)
dark = Pin(DARKNESS_DETECTION_PIN, Pin.IN, Pin.PULL_DOWN)

pixels.fill(OFF)
pixels.write()

while True:
    if dark.value():
        if down.value():
            top_to_bottom(pixels, PIXEL_COUNT, WHITE)
            time.sleep(SHINE_TIME)
            top_to_bottom(pixels, PIXEL_COUNT, OFF)
        elif up.value():
            bottom_to_top(pixels, PIXEL_COUNT, WHITE)
            time.sleep(SHINE_TIME)
            bottom_to_top(pixels, PIXEL_COUNT, OFF)
