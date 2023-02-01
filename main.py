from rpi_ws281x import PixelStrip, Color
from led_functions.clear import clear
from led_functions.static import static_white
from led_functions.light_follow import light_follow

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
    
    try:
        while True:
            light_follow(strip)
        
    except KeyboardInterrupt:
        clear(strip)