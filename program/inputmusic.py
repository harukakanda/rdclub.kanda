from machine import Pin, PWM, Timer
# ピタゴラスイッチのメロディーを配列で作成。
# 1要素が8分3連符ひとつ分の音の長さになる。 " "は無音（休符）
melody = []

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
        word = n[count]
        t = n[count+1]
        melody.append(word+t)
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
    

# 回路依存の定数 -  回路構成に応じて変更必要
GPIO_SPEAKER = 18  # スピーカー
GPIO_RED     = 2  # 各色のLED
GPIO_YELLOW  = 3
GPIO_GREEN   = 4
GPIO_BLUE    = 5
GPIO_WHITE   = 6

# GPIOの宣言
SPEAKER = PWM(Pin(GPIO_SPEAKER, Pin.OUT)) # スピーカー
RED     = Pin(GPIO_RED,     Pin.OUT) # LED
BLUE    = Pin(GPIO_BLUE,    Pin.OUT)
YELLOW  = Pin(GPIO_YELLOW,  Pin.OUT)
GREEN   = Pin(GPIO_GREEN,   Pin.OUT)
WHITE   = Pin(GPIO_WHITE,   Pin.OUT)

# 使用する音を定義（ピタゴラスイッチは低いラ～高いドまでの音を使う）
# dict型でキーは音のID、値は音の属性 リスト
# 属性の内容は周波数、光らせるLED の色
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
    "i4": [ 415.305, WHITE  ],  # G4s
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


# bps = 6.4 # 原曲128bpm / 60秒 = 2.1333...bps * 3連符 = 6.4bps
mspb = b # 6.4bpsの逆数 = 0.156ms　これが8分3連符ひとつ分の音の長さ、音の間隔となる


# カウンター
i = 0

# 全部のLEDを消す
def turn_off_all_led():
    RED.value(0)
    BLUE.value(0)
    YELLOW.value(0)
    GREEN.value(0)
    WHITE.value(0)

# 音を鳴らすためのコールバック関数
def beat(timer):
    global melody
    global i
    global SPEAKER
    

    if i >= len(melody): # メロディーを最後まで演奏し終えたら
        SPEAKER.deinit() # スピーカーのPWMを破棄して
        turn_off_all_led() # LEDを消して
        timer.deinit() # タイマーを破棄して終了

    elif melody[i] == "//": # メロディー音が0、つまり無音（休符）の場合
        SPEAKER.duty_u16(0) # PWMのDutyを0とすることで波形は出力されずLOWとなり、音は出ない
        turn_off_all_led() # LEDを消す

    else:
        SPEAKER.freq(int(tone[melody[i]][0] + 0.5)) # PWMの周波数を次のメロディー音の周波数に変更する。整数で渡す必要があるので、+0.5してから小数点以下切り捨て（thanks @naohiro2g）
        SPEAKER.duty_u16(0x8000) # PWMのDutyを50％に戻し、音を出す。Dutyは0～0xFFFFつまり65535までの間の値で設定
        turn_off_all_led() # LEDを消す        
        tone[melody[i]][1].value(1) # LEDを光らせる

        
    i += 1 # メロディーを次に進めて終わり

# 8分3連符の間隔でコールバックを呼ぶタイマーを作成し、メロディースタート
tim = Timer()
tim.init(period=mspb, mode=Timer.PERIODIC, callback=beat)


# ア・ホール・ニューワールド 240