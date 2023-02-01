from rpi_ws281x import Color
from time import sleep


def light_follow(strip):
    initial = True
    n = range(strip.numPixels())
    
    for j in n:
        for i in n - j:
            if not initial:
                strip.setPixelColor(i - 1, Color(0, 0, 0))
                strip.show()
            
            strip.setPixelColor(i, Color(255, 0, 0))
            strip.show()
            sleep(25 / 1000.0)
            initial = False