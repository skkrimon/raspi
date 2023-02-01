from rpi_ws281x import Color
from time import sleep


def light_follow(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(255, 0, 0))
        strip.show()
        sleep(25 / 1000.0)