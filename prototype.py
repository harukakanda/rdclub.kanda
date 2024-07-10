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


while True:
    print("sw = {:d}".format(sw.value()))
    while n < len(lst):
        if sw.value() == 0:
            print(lst2[n])
            lst[n].value(1)
            utime.sleep(1)
        else:
            n = n + 1
            utime.sleep(1)