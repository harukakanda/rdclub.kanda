from machine import Pin
import utime
l = Pin(2, Pin.OUT)
y = Pin(3, Pin.OUT)
g = Pin(4, Pin.OUT)
b = Pin(5, Pin.OUT)
w = Pin(6, Pin.OUT)
while True:
    l.value(1)
    utime.sleep(1)
    l.value(0)
    utime.sleep(0.1)
    y.value(1)
    utime.sleep(1)
    y.value(0)
    utime.sleep(0.1)
    g.value(1)
    utime.sleep(1)
    g.value(0)
    utime.sleep(0.1)
    b.value(1)
    utime.sleep(1)
    b.value(0)
    utime.sleep(0.1)
    w.value(1)
    utime.sleep(1)
    w.value(0)
    utime.sleep(1)
    
    
    
    
    