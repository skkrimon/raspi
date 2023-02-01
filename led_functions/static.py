from rpi_ws281x import Color


def static_white(strip):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(255, 255, 255))
    
    strip.show()