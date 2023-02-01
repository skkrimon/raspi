from rpi_ws281x import Color
from time import sleep


def light_follow(strip):
    initial = True

    for j in range(strip.numPixels()):
        for i in range(strip.numPixels() - j):
            if not initial:
                strip.setPixelColor(i - 1, Color(0, 0, 0))
                strip.show()
            
            strip.setPixelColor(i, Color(242, 0, 255))
            strip.show()
            sleep(25 / 1000.0)
            initial = False