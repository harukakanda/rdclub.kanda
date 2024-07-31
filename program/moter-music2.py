from machine import Pin, PWM, Timer
import utime

CIRCUIT = 1 # 全体をまとめた回路
#CIRCUIT = 2 # 神田実験用の回路

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
    
led_external = machine.Pin(2, machine.Pin.OUT)
angle_0 = int(2.5 / 20 * 65536)
angle_90 = int(1.5 / 20 * 65536)
angle_180 = int(0.5 / 20 * 65536)


# 使用する音を定義（ピタゴラスイッチは低いラ～高いドまでの音を使う）
# dict型でキーは音のID、値は音の属性 リスト
# 属性の内容は周波数、光らせるLED の色
if   CIRCUIT == 2:
    tone = {
        ""   : [   0.000, 0      ],  # 無音（休符）
        "A4" : [ 440.000, BLUE   ],  # ラ　A4はラの音で赤LEDを光らせる
        "B4" : [ 493.883, BLUE   ],  # シ　以下同様
        "C5" : [ 523.251, YELLOW ],  # ド
        "C5s": [ 554.365, GREEN  ],
        "D5" : [ 587.330, WHITE  ],
        "D5s": [ 622.254, YELLOW ],
        "E5" : [ 659.255, BLUE   ],
        "F5" : [ 698.456, YELLOW ],
        "F5s": [ 739.989, WHITE  ],
        "G5" : [ 783.991, GREEN  ],
        "G5s": [ 839.609, BLUE   ],
        "A5" : [ 880.000, GREEN  ],
        "A5s": [ 932.328, WHITE  ],
        "B5" : [ 987.767, GREEN  ],
        "C6" : [1046.502, YELLOW ],
    }
elif   CIRCUIT == 1:
    tone = {
        ""   : [   0.000, 0      ],  # 無音（休符）
        "A4" : [ 440.000, BLUE   ],  # ラ　A4はラの音で赤LEDを光らせる
        "B4" : [ 493.883, BLUE2   ],  # シ　以下同様
        "C5" : [ 523.251, YELLOW ],  # ド
        "C5s": [ 554.365, GREEN  ],
        "D5" : [ 587.330, RED  ],
        "D5s": [ 622.254, YELLOW ],
        "E5" : [ 659.255, BLUE   ],
        "F5" : [ 698.456, YELLOW ],
        "F5s": [ 739.989, RED2  ],
        "G5" : [ 783.991, GREEN  ],
        "G5s": [ 839.609, BLUE   ],
        "A5" : [ 880.000, GREEN  ],
        "A5s": [ 932.328, YELLOW2  ],
        "B5" : [ 987.767, GREEN  ],
        "C6" : [1046.502, YELLOW ],
    }

# bps = 6.4 # 原曲128bpm / 60秒 = 2.1333...bps * 3連符 = 6.4bps
mspb = 156 # 6.4bpsの逆数 = 0.156ms　これが8分3連符ひとつ分の音の長さ、音の間隔となる

# ピタゴラスイッチのメロディーを配列で作成。
# 1要素が8分3連符ひとつ分の音の長さになる。 ""は無音（休符）
melody = [ "D5" ,"E5" ,""  ,"D5","E5" ,"",
           "G5" ,"F5s",""  ,"D5","E5" ,"",
           "D5" ,"E5" ,""  ,"D5","E5" ,"",
           "C6" ,"B5" ,""  ,"G5","A5" ,"",
           "D5" ,"E5" ,""  ,"D5","E5" ,"",
           "G5" ,"F5s",""  ,"D5","E5" ,"",
           "B4" ,"A4" ,""  ,"B4","C5" ,"",
           "C5s","D5" ,""  ,""  ,"D5" ,"",
           "D5" ,"E5" ,""  ,"D5","E5" ,"",
           "G5" ,"F5s",""  ,"D5","E5" ,"",
           "D5" ,"E5" ,""  ,"D5","E5" ,"",
           "C6" ,"B5" ,""  ,"G5","A5" ,"",
           "D5" ,"E5" ,""  ,"D5","E5" ,"",
           "G5" ,"F5s",""  ,"D5","E5" ,"",
           "B4" ,"A4" ,"A4","A4","A4" ,"A4",
           "A4" ,"A4" ,"A4","A4",""   ,"",
           "F5" ,"E5" ,""  ,"E5","F5s","E5",
           "F5s","G5" ,"G5","G5","D5" ,"",
           "B4" ,"C5" ,""  ,"C5","D5" ,"C5s",
           "D5" ,"B4" ,"B4","B4",""   ,"",
           "D5" ,"E5" ,""  ,"D5","E5" ,"",
           "G5" ,"F5s",""  ,"D5","E5" ,"",
           "D5" ,"E5" ,""  ,"D5","E5" ,"",
           "G5" ,"F5s",""  ,"D5","E5" ,"",
           "D5" ,"E5" ,""  ,"D5","E5" ,"",
           "C6" ,"B5" ,""  ,""  ,"G5" ,"",
           ""   ,""   ,""  ,""  ,""   ,"",
           ""   ,""   ,""  ,""  ,""   ,"",
           "D5" ,"E5" ,""  ,"D5","E5" ,"",
           "C6" ,"B5" ,""  ,""  ,"G5" ,"",
           ""   ,""   ,""  ,""  ,""   ,"",
           ""   ,""   ,""  ,""  ,""   ,"",
           ""   ,""   ,""  ,
           ]

# カウンター
i = 0

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
    global SPEAKER
    

    if i >= len(melody): # メロディーを最後まで演奏し終えたら
        #SPEAKER.deinit() # スピーカーのPWMを破棄して
        #turn_off_all_led() # LEDを消して
        #timer.deinit() # タイマーを破棄して終了
        i = 0

    elif melody[i] == "": # メロディー音が0、つまり無音（休符）の場合
        SPEAKER.duty_u16(0) # PWMのDutyを0とすることで波形は出力されずLOWとなり、音は出ない
        turn_off_all_led() # LEDを消す

    else:
        SPEAKER.freq(int(tone[melody[i]][0] + 0.5)) # PWMの周波数を次のメロディー音の周波数に変更する。整数で渡す必要があるので、+0.5してから小数点以下切り捨て（thanks @naohiro2g）
        SPEAKER.duty_u16(0x8000) # PWMのDutyを50％に戻し、音を出す。Dutyは0～0xFFFFつまり65535までの間の値で設定
        tone[melody[i]][1].value(1) # LEDを光らせる
        
    i += 1 # メロディーを次に進めて終わり

# 8分3連符の間隔でコールバックを呼ぶタイマーを作成し、メロディースタート
tim = Timer()
tim.init(period=mspb, mode=Timer.PERIODIC, callback=beat)


if   CIRCUIT == 1:
    while True:
        if button1.value() == 1:
            print("ボタン１が押された")
            led_external.on()
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
            led_external.on()
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
            led_external.on()
            utime.sleep(0.1)
            servo3.duty_u16(angle_0)
            utime.sleep(1)
            servo3.duty_u16(angle_90)
            utime.sleep(1)
            servo3.duty_u16(angle_180)
            utime.sleep(1)
            servo3.duty_u16(0)        
        else:
            led_external.off()
            
elif CIRCUIT == 2:
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