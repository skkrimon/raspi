from rpi_ws281x import Color
from time import sleep


def light_follow(strip):
    prev_color = Color(0, 0, 0)
    
    while True:
        color = generate_color(prev_color)
        
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
                
        sleep(500 / 1000.0)
        
        prev_color = color
    

def generate_color(prev_color):
    if prev_color == Color(0, 0, 0):
        return Color(255, 0, 0)
    
    return Color(255, 255, 255)