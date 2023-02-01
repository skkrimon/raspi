from rpi_ws281x import Color
from time import sleep


def light_follow(strip, color, prev_color = Color(0, 0, 0)):
    initial = True

    for j in range(strip.numPixels()):
        for i in range(strip.numPixels() - j):
            if not initial:
                strip.setPixelColor(i - 1, prev_color)
                strip.show()
            
            strip.setPixelColor(i, color)
            strip.show()
            sleep(50 / 1000.0)
            initial = False
            
    sleep(1)