import machine 
import utime
from machine import PWM, Pin
from time import sleep

led_external = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14,machine.Pin.IN,machine.Pin.PULL_DOWN)
servo = PWM(Pin(26))
servo.freq(50)
angle_0 = int(2.5 / 20 * 65536)
angle_90 = int(1.5 / 20 * 65536)
angle_180 = int(0.5 / 20 * 65536)

while True:
    if button.value() == 1:
        print("ボタンが押された")
        led_external.on()
        utime.sleep(0.1)
        servo.duty_u16(angle_0)
        utime.sleep(1)
        servo.duty_u16(angle_90)
        utime.sleep(1)
        servo.duty_u16(angle_180)
        utime.sleep(1)
        servo.duty_u16(0)
        
        
    else:
        led_external.off()

