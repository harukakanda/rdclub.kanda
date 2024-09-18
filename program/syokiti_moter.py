from machine import PWM, Pin
from time import sleep

servo1 = PWM(Pin(16))
servo2 = PWM(Pin(17))
servo3 = PWM(Pin(18))
servo1.freq(50)
servo2.freq(50)
servo3.freq(50)
button1 = machine.Pin(19,machine.Pin.IN,machine.Pin.PULL_DOWN)
button2 = machine.Pin(20,machine.Pin.IN,machine.Pin.PULL_DOWN)
button3 = machine.Pin(21,machine.Pin.IN,machine.Pin.PULL_DOWN)
angle_0 = int(2.5 / 20 * 65536)
angle_45 = int(2.0 / 20 * 65536)
angle_90 = int(1.5 / 20 * 65536)
angle_135 = int(1.0 / 20 * 65536)
angle_180 = int(0.5 / 20 * 65536)
angle_45=int(2.0/20*65536)


while True:
    if button1.value() == 1:
        print("ボダン赤が押された")
        servo1.duty_u16(angle_0)
        servo2.duty_u16(angle_0)
        servo3.duty_u16(angle_0)
        print("サーボが　”angle_0”　になった")
    if button2.value() == 1:
        print("ボダン赤が押された")
        servo1.duty_u16(angle_90)
        servo2.duty_u16(angle_90)
        servo3.duty_u16(angle_90)
        print("サーボが　”angle_90”　になった")            
    if button3.value() == 1:
        print("ボダン赤が押された")
        servo1.duty_u16(angle_180)
        servo2.duty_u16(angle_180)
        servo3.duty_u16(angle_180)
        print("サーボが　”angle_180”　になった")      