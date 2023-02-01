from rpi_ws281x import PixelStrip, Color
from programms import clear

LED_COUNT = 24
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0


if __name__ == '__main__':
    strip = PixelStrip(
        LED_COUNT, 
        LED_PIN, 
        LED_FREQ_HZ, 
        LED_DMA,
        LED_INVERT,
        LED_BRIGHTNESS,
        LED_CHANNEL
    )
    
    strip.begin()
    
    strip.setPixelColor(1, Color(255, 0, 0))
    strip.setPixelColor(2, Color(0, 255, 0))
    
    try:
        while True:
            pass
        
    except KeyboardInterrupt:
        clear()