from machine import Pin
import utime
import random

sw = Pin(17, Pin.IN, Pin.PULL_UP)
r = Pin(2, Pin.OUT)
y = Pin(3, Pin.OUT)
g = Pin(4, Pin.OUT)
b = Pin(5, Pin.OUT)
w = Pin(6, Pin.OUT)

lst = [r, y, g, b, w]
lst2 = ["red", "yellow", "green", "blue", "white"]


while True:
    print("sw = {:d}".format(sw.value()))
    for n in range(0, len(lst)):
        s = random.randint(1, 5)
        if sw.value() == 0:
            print(lst2[n] + " / " + str(0.1 * s))
            lst[n].value(1)
            utime.sleep(0.1 * s)
            lst[n].value(0)
            utime.sleep(0.1)
        else:
            lst[n].value(0)
            n = 0
        
        if n == len(lst):
            n = 0