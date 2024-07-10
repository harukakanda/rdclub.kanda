from machine import Pin
import utime

sw = Pin(17, Pin.IN, Pin.PULL_UP)
r = Pin(2, Pin.OUT)
y = Pin(3, Pin.OUT)
g = Pin(4, Pin.OUT)
b = Pin(5, Pin.OUT)
w = Pin(6, Pin.OUT)

lst = [r, y, g, b, w]
lst2 = ["red", "yellow", "green", "blue", "white"]
lst3 = [r, y, g, b, w, r, y, g, b, w]




while True:
    print("sw = {:d}".format(sw.value()))
    n = 0
    while True:
        if sw.value() == 0:
            if n >= len(lst3):
                n = 0
            if n <= 5:
                lst3[n].value(1)
                utime.sleep(0.7)
                n = n + 1
            if n >= 5:
                lst3[n].value(0)
                utime.sleep(0.7)
                n = n + 1
