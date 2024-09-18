from machine import Pin, PWM, Timer
import utime

GPIO_SPEAKER = 4  # スピーカー
GPIO_RED     = 2  # 各色のLED
GPIO_BLUE    = 3
GPIO_YELLOW  = 5
GPIO_GREEN   = 6
GPIO_BLUE2   = 7
GPIO_YELLOW2 = 8
GPIO_GREEN2  = 9
GPIO_RED2    = 10

SPEAKER = PWM(Pin(GPIO_SPEAKER, Pin.OUT)) # スピーカー
RED     = Pin(GPIO_RED,     Pin.OUT) # LED
BLUE    = Pin(GPIO_BLUE,    Pin.OUT)
YELLOW  = Pin(GPIO_YELLOW,  Pin.OUT)
GREEN   = Pin(GPIO_GREEN,   Pin.OUT)
BLUE2   = Pin(GPIO_BLUE2,   Pin.OUT)
YELLOW2 = Pin(GPIO_YELLOW2, Pin.OUT)
GREEN2  = Pin(GPIO_GREEN2,  Pin.OUT)
RED2    = Pin(GPIO_RED2,    Pin.OUT)

button1 = machine.Pin(19,machine.Pin.IN,machine.Pin.PULL_DOWN)
button2 = machine.Pin(20,machine.Pin.IN,machine.Pin.PULL_DOWN)
button3 = machine.Pin(21,machine.Pin.IN,machine.Pin.PULL_DOWN)

servo1 = PWM(Pin(16))
servo2 = PWM(Pin(17))
servo3 = PWM(Pin(18))

servo1.freq(50)
servo2.freq(50)
servo3.freq(50)

angle_0 = int(2.5 / 20 * 65536)
angle_90 = int(1.5 / 20 * 65536)
angle_180 = int(0.5 / 20 * 65536)
