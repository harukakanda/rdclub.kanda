from machine import Pin
import utime

sw = Pin(17, Pin.IN, Pin.PULL_UP)
l = Pin(2, Pin.OUT)
y = Pin(3, Pin.OUT)
g = Pin(4, Pin.OUT)
b = Pin(5, Pin.OUT)
w = Pin(6, Pin.OUT)

while True:
    print("sw = {:d}".format(sw.value()))
    
    if sw.value() == 0:
        l.value(1)
        utime.sleep(1)
        l.value(0)
        utime.sleep(0.1)
    else:
        l.value(0)
    
    if sw.value() == 0:
        y.value(1)
        utime.sleep(1)
        y.value(0)
        utime.sleep(0.1)
    else:
        y.value(0)
        
    if sw.value() == 0:
        g.value(1)
        utime.sleep(1)
        g.value(0)
        utime.sleep(0.1)
    else:
        g.value(0)
        
    if sw.value() == 0:
        b.value(1)
        utime.sleep(1)
        b.value(0)
        utime.sleep(0.1)
    else:
        b.value(0)
        
    if sw.value() == 0:
        w.value(1)
        utime.sleep(1)
        w.value(0)
        utime.sleep(1)
    else:
        w.value(0)