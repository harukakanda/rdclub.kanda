from machine import Pin, PWM, Timer
import utime

CIRCUIT = 1 # 全体をまとめた回路
#CIRCUIT = 2 # 神田実験用の回路

lc = 1  #ledの光らせ方
lc = 2

# 回路依存の定数 -  回路構成に応じて変更必要
if   CIRCUIT == 1:
    GPIO_SPEAKER = 4  # スピーカー
    GPIO_RED     = 2  # 各色のLED
    GPIO_BLUE    = 3
    GPIO_YELLOW  = 5
    GPIO_GREEN   = 6
    GPIO_BLUE2   = 7
    GPIO_YELLOW2 = 8
    GPIO_GREEN2  = 9
    GPIO_RED2    = 10
    # GPIOの宣言
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
elif CIRCUIT == 2:
    GPIO_SPEAKER = 18  # スピーカー
    GPIO_RED     = 2  # 各色のLED
    GPIO_YELLOW  = 2
    GPIO_GREEN   = 4
    GPIO_BLUE    = 5
    GPIO_WHITE   = 6
    SPEAKER = PWM(Pin(GPIO_SPEAKER, Pin.OUT)) # スピーカー
    RED     = Pin(GPIO_RED,     Pin.OUT) # LED
    BLUE    = Pin(GPIO_BLUE,    Pin.OUT)
    YELLOW  = Pin(GPIO_YELLOW,  Pin.OUT)
    GREEN   = Pin(GPIO_GREEN,   Pin.OUT)
    WHITE   = Pin(GPIO_WHITE,   Pin.OUT)
    button = machine.Pin(17,machine.Pin.IN,machine.Pin.PULL_DOWN)
    servo = PWM(Pin(16))
    servo.freq(50)
    
angle_0 = int(2.5 / 20 * 65536)
angle_90 = int(1.5 / 20 * 65536)
angle_180 = int(0.5 / 20 * 65536)


# 使用する音を定義（ピタゴラスイッチは低いラ～高いドまでの音を使う）
# dict型でキーは音のID、値は音の属性 リスト
# 属性の内容は周波数、光らせるLED の色
if   CIRCUIT == 1:
    tone = {
        "//": [   0.000, 0      ],  # 無音（休符）
        
        "d4": [ 261.626, RED    ],  # C4
        "r4": [ 277.183, RED2   ],  # C4s
        "f4": [ 293.665, YELLOW ],  # D4
        "t4": [ 311.127, YELLOW2],  # D4s
        "g4": [ 329.628, GREEN  ],  # E4
        "h4": [ 349.228, BLUE   ],  # F4
        "u4": [ 369.994, BLUE2  ],  # F4s
        "j4": [ 391.995, GREEN  ],  # G4
        "i4": [ 415.305, GREEN2 ],  # G4s
        "k4": [ 440.000, RED    ],  # A4
        "o4": [ 466.164, RED2   ],  # A4s
        "l4": [ 493.883, BLUE   ],  # B4

        "d5": [ 523.251, YELLOW ],  # C5
        "r5": [ 554.365, YELLOW2],  # C5s
        "f5": [ 587.330, GREEN  ],  # D5
        "t5": [ 622.254, GREEN2 ],  # D5s
        "g5": [ 659.255, BLUE   ],  # E5
        "h5": [ 698.456, GREEN2 ],  # F5
        "u5": [ 739.989, GREEN2 ],  # F5a
        "j5": [ 783.991, RED    ],  # G5
        "i5": [ 830.609, RED2   ],  # G5s
        "k5": [ 880.000, BLUE   ],  # A5
        "o5": [ 932.328, BLUE2  ],  # A5s
        "l5": [ 987.767, YELLOW ],  # B5
        
        "d6": [ 1046.502, GREEN  ],  # C6
        "r6": [ 1108.731, GREEN2 ],  # C6s
        "f6": [ 1174.659, BLUE   ],  # D6
        "t6": [ 1244.508, BLUE2  ],  # D6s
        "g6": [ 1318.510, GREEN  ],  # E6
        "h6": [ 1396.913, RED    ],  # F6
        "u6": [ 1479.978, RED2   ],  # F6s
        "j6": [ 1567.982, YELLOW ],  # G6
        "i6": [ 1661.219, YELLOW ],  # G6s
        "k6": [ 1760.000, GREEN  ],  # A6
        "o6": [ 1864.655, GREEN2 ],  # A6s
        "l6": [ 1975.533, BLUE   ],  # B6
    }
elif CIRCUIT == 2:
    tone = {
        "//": [   0.000, 0      ],  # 無音（休符）
        
        "d4": [ 261.626, RED    ],  # C4
        "r4": [ 277.183, RED    ],  # C4s
        "f4": [ 293.665, YELLOW ],  # D4
        "t4": [ 311.127, YELLOW ],  # D4s
        "g4": [ 329.628, GREEN  ],  # E4
        "h4": [ 349.228, BLUE   ],  # F4
        "u4": [ 369.994, BLUE   ],  # F4s
        "j4": [ 391.995, WHITE  ],  # G4
        "i4": [ 415.305, WHITE  ],  # G4sS
        "k4": [ 440.000, RED    ],  # A4
        "o4": [ 466.164, RED    ],  # A4s
        "l4": [ 493.883, BLUE   ],  # B4

        "d5": [ 523.251, YELLOW ],  # C5
        "r5": [ 554.365, YELLOW ],  # C5s
        "f5": [ 587.330, GREEN  ],  # D5
        "t5": [ 622.254, GREEN  ],  # D5s
        "g5": [ 659.255, BLUE   ],  # E5
        "h5": [ 698.456, WHITE  ],  # F5
        "u5": [ 739.989, WHITE  ],  # F5a
        "j5": [ 783.991, RED    ],  # G5
        "i5": [ 830.609, RED    ],  # G5s
        "k5": [ 880.000, BLUE   ],  # A5
        "o5": [ 932.328, BLUE   ],  # A5s
        "l5": [ 987.767, YELLOW ],  # B5
        
        "d6": [ 1046.502, GREEN  ],  # C6
        "r6": [ 1108.731, GREEN  ],  # C6s
        "f6": [ 1174.659, BLUE   ],  # D6
        "t6": [ 1244.508, BLUE   ],  # D6s
        "g6": [ 1318.510, WHITE  ],  # E6
        "h6": [ 1396.913, RED    ],  # F6
        "u6": [ 1479.978, RED    ],  # F6s
        "j6": [ 1567.982, YELLOW ],  # G6
        "i6": [ 1661.219, YELLOW ],  # G6s
        "k6": [ 1760.000, GREEN  ],  # A6
        "o6": [ 1864.655, GREEN  ],  # A6s
        "l6": [ 1975.533, BLUE   ],  # B6
    }



# ピタゴラスイッチのメロディーを配列で作成。
# 1要素が8分3連符ひとつ分の音の長さになる。 ""は無音（休符）
melody = []

if CIRCUIT == 1:
    leddir = [RED, BLUE, YELLOW, GREEN, BLUE2, YELLOW2, GREEN2, RED2]
elif CIRCUIT == 2:
    leddir = [RED, YELLOW, GREEN, BLUE, WHITE]

melodyn = {
    "1": [ 240, "g5g5f5h5h5g5d5d5j4j4j4j4j4j4j4//g5g5f5h5h5g5d5d5g5g5g5g5f5f5f5//f5f5r5g5g5f5l4l4f5f5d5d5l4l4d5d5k4l4l4f5f5f5d5j4j4j4j4j4j4j4//g5g5f5h5h5g5d5d5j4j4j4j4j4j4j4//g5g5f5h5h5g5d5d5g5g5g5g5f5f5f5//f5f5r5g5g5f5f5l4f5f5d5d5l4l4d5d5k4l4l4f5f5f5d5d5g5g5//g5h5h5k5k5j5j5j5j5j5j5j5j5j5j5//g5h5h5k5k5j5j5f5h5h5h5g5//g5g5//g5h5j5l5l5k5k5j5j5j5d5l5l5k5k5j5j5j5d5g5g5f5f5d5d5g5g5f5f5f5//g5h5h5k5k5j5j5j5j5j5j5j5j5j5//g5h5h5k5k5j5j5f5h5h5h5g5//g5g5//g5h5j5l5l5k5k5j5j5j5d5l5l5d6j5j5j5//g5g5f5f5d5d5f5f5h5h5g5g5d5d5l4l4d5d5d5d5d5d5d5d5d5d5"],
    "2": [ 240, "h4h4g4g4h4d4d4d4d4d4d4d4d4d4////h4h4g4g4h4k4k4k4k4k4k4k4k4//o4o4k4k4j4j4h4o4o4o4k4k4j4j4h4h4h4h4j4j4j4j4j4j4j4j4j4j4j4////h4h4g4g4h4d4d4d4d4d4d4d4d4d4////h4h4g4g4h4d5d5d5d5d5d5d5d5//o4//o4//o4k4j4o4o4o4o4o4//j4k4o4k4//k4//k4j4h4k4k4k4k4k4k4k4////f4f4g4g4h4h4j4f4//f4g4g4h4j4h4d5d5d5d5d5d5d5d5d5d5d5////h4j4k4o4d5//k4h4//d5//o4o4j4j4//////////o4//j4g4//o4//k4k4h4h4////////////r4r4h4h4o4o4k4k4d5h4h4h4h4k4o4k4o4k4o4k4h4j4j4j4////h4j4k4o4d5//k4h4//d5//o4o4j4j4//////////o4//j4g4//o4//k4k4h4h4//////f4f4f5f5d5o4k4o4d5d5d5h4h4h4h4h4k4o4k4h4o4k4h4f5d5d5d5d5d5d5d5d5d5////d4d4o4k4j4k4h4h4h4h4h4h4h4h4"],
    "3": [ 156, "f5g5//f5g5//j5u5//f5g5//f5g5//f5g5//d6l5//j5k5//f5g5//f5g5//j5u5//f5g5//l4k4//l4d5//r5f5////f5//f5g5//f5g5//j5u5//f5g5//f5g5//f5g5//d6l5//j5k5//f5g5//f5g5//j5u5//f5g5//l4k4k4k4k4k4k4k4k4k4////h5g5//g5u5g5u5j5j5j5f5//l4d5//d5f5r5f5l4l4l4////f5g5//f5g5//j5u5//f5g5//f5g5//f5g5//j5u5//f5g5//f5g5//f5g5//d6l5////j5//////////////////////////f5g5//f5g5//d6l5////j5//"],
    }

print("新規のメロディを入力　➔　”A”")
print("既存のメロディを出力　➔　”B”")

i = input()
if i == "A":    
    print("bpsを入力 = ")
    b = int(input())
    print("メロディを入力　= ")
    n = input()
    count = 0
    while count < len(n):
        word = n[count] + n[count+1]
        melody.append(word)
        count += 2

else:
    print("ア・ホール・ニューワールド　➔　”１”")
    print("さんぽ　➔　”２”")
    print("ピタゴラスイッチ　➔　”３”")
    i = input()
    b = melodyn[i][0]
    n = melodyn[i][1]
    count = 0
    while count < len(n):
        word = n[count]
        t = n[count+1]
        melody.append(word+t)
        count += 2
        
for _ in range(15):
    melody.append("//")
print(melody)

# bps = 6.4 # 原曲128bpm / 60秒 = 2.1333...bps * 3連符 = 6.4bps
mspb = b # 6.4bpsの逆数 = 0.156ms　これが8分3連符ひとつ分の音の長さ、音の間隔となる


# カウンター
i = 0
k = 0

# 全部のLEDを消す
def turn_off_all_led():
    if   CIRCUIT == 1:
        RED.value(0)
        BLUE.value(0)
        YELLOW.value(0)
        GREEN.value(0)
        RED2.value(0)
        BLUE2.value(0)
        YELLOW2.value(0)
        GREEN2.value(0)
    elif CIRCUIT == 2:
        RED.value(0)
        BLUE.value(0)
        YELLOW.value(0)
        GREEN.value(0)
        WHITE.value(0)

# 音を鳴らすためのコールバック関数
def beat(timer):
    global melody
    global i
    global k
    global SPEAKER
    global leddir
    
    if i == 0:
        turn_off_all_led() # LEDを消して
        
    if i >= len(melody): # メロディーを最後まで演奏し終えたら
        #SPEAKER.deinit() # スピーカーのPWMを破棄して
        #timer.deinit() # タイマーを破棄して終了
        turn_off_all_led() # LEDを消して
        i = 0
        k = 0

    elif melody[i] == "//": # メロディー音が0、つまり無音（休符）の場合
        SPEAKER.duty_u16(0) # PWMのDutyを0とすることで波形は出力されずLOWとなり、音は出ない
        turn_off_all_led() # LEDを消す

    else:
        SPEAKER.freq(int(tone[melody[i]][0] + 0.5)) # PWMの周波数を次のメロディー音の周波数に変更する。整数で渡す必要があるので、+0.5してから小数点以下切り捨て（thanks @naohiro2g）
        SPEAKER.duty_u16(0x8000) # PWMのDutyを50％に戻し、音を出す。Dutyは0～0xFFFFつまり65535までの間の値で設定
        if   lc == 1:
            tone[melody[i]][1].value(1) # LEDを光らせる
        elif lc == 2:
            leddir[k].value(1)
            if melody[i] != melody[i+1]:
                k += 1
            if k == len(leddir):
                k = 0
        
    i += 1 # メロディーを次に進めて終わり
# 8分3連符の間隔でコールバックを呼ぶタイマーを作成し、メロディースタート
tim = Timer()
tim.init(period=mspb, mode=Timer.PERIODIC, callback=beat)


if CIRCUIT == 1:
    while True:
        if button1.value() == 1:
            print("ボタン１が押された")
            utime.sleep(0.1)
            servo1.duty_u16(angle_0)
            utime.sleep(1)
            servo1.duty_u16(angle_90)
            utime.sleep(1)
            servo1.duty_u16(angle_180)
            utime.sleep(1)
            servo1.duty_u16(0)        
        elif button2.value() == 1:
            print("ボタン2が押された")
            utime.sleep(0.1)
            servo2.duty_u16(angle_0)
            utime.sleep(1)
            servo2.duty_u16(angle_90)
            utime.sleep(1)
            servo2.duty_u16(angle_180)
            utime.sleep(1)
            servo2.duty_u16(0)        
        elif button3.value() == 1:
            print("ボタン3が押された")
            utime.sleep(0.1)
            servo3.duty_u16(angle_0)
            utime.sleep(1)
            servo3.duty_u16(angle_90)
            utime.sleep(1)
            servo3.duty_u16(angle_180)
            utime.sleep(1)
            servo3.duty_u16(0)
        else:
            servo1.duty_u16(0)
            servo2.duty_u16(0)
            servo3.duty_u16(0) 
            
elif CIRCUIT == 2:
    while True:
        if button.value() == 1:
            print("ボタンが押された")
            servo.duty_u16(angle_0)
            utime.sleep(0.1)
            servo.duty_u16(angle_90)
            utime.sleep(0.1)
            servo.duty_u16(angle_180)
            utime.sleep(0.1)
            servo.duty_u16(0)
