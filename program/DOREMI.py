from machine import Pin, PWM, Timer

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
    ""   : [   0.000, 0      ],  # 無音（休符）
    "A4 ": [ 440.000, RED    ],  # ラ　A4はラの音で赤LEDを光らせる
    "B4 ": [ 493.883, BLUE   ],  # シ　以下同様
    "C5 ": [ 523.251, YELLOW ],
    "C5s": [ 554.365, YELLOW ],
    "D5 ": [ 587.330, GREEN  ],
    "D5s": [ 622.254, GREEN  ],
    "E5 ": [ 659.255, BLUE   ],
    "F5 ": [ 698.456, WHITE  ],
    "F5s": [ 739.989, WHITE  ],
    "G5 ": [ 783.991, RED    ],
    "G5s": [ 830.609, RED    ],
    "A5 ": [ 880.000, BLUE   ],
    "A5s": [ 932.328, BLUE   ],
    "B5 ": [ 987.767, YELLOW ],
    "C6 ": [1046.502, GREEN  ],
}

# bps = 6.4 # 原曲128bpm / 60秒 = 2.1333...bps * 3連符 = 6.4bps
mspb = 190 # 6.4bpsの逆数 = 0.156ms　これが8分3連符ひとつ分の音の長さ、音の間隔となる

# ピタゴラスイッチのメロディーを配列で作成。
# 1要素が8分3連符ひとつ分の音の長さになる。 ""は無音（休符）
melody = [ "C5 ","C6 ","B5 ","A5 ","G5 ","F5 ","E5 ","D5 ",
           "C5 ","C5 ","C5 ","D5 ","E5 ","E5 ","E5 ","C5 ",
           "E5 ","E5 ","C5 ","C5 ","E5 ","E5 ",""   ,""   ,
           "D5 ","D5 ","D5 ","E5 ","F5 ","F5 ","E5 ","D5 ", 
           "F5 ","F5 ","F5 ","F5 ","F5 ","F5 ",""   ,""   , 
           "E5 ","E5 ","E5 ","F5 ","G5 ","G5 ","G5 ","E5 ", 
           "G5 ","G5 ","E5 ","E5 ","G5 ","G5 ",""   ,""   , 
           "F5 ","F5 ","F5 ","G5 ","A5 ","A5 ","G5 ","F5 ",
           "A5 ","A5 ","A5 ","A5 ","A5 ","A5 ",""   ,""   ,
           "G5 ","G5 ","G5 ","C5 ","D5 ","E5 ","F5 ","G5 ",
           "A5 ","A5 ","A5 ","A5 ","A5 ","A5 ",""   ,""   ,
           "A5 ","A5 ","A5 ","D5 ","E5 ","F5s","G5 ","A5 ",
           "B5 ","B5 ","B5 ","B5 ","B5 ","B5 ",""   ,""   ,
           "B5 ","B5 ","B5 ","E5 ","F5s","G5s","A5 ","B5 ",
           "C6 ","C6 ","C6 ","C6 ","C6 ","C6 ",""   ,
           "C6 ","B5 ","A5 ","A5 ","F5 ","F5 ","B5 ","B5 ",
           "G5 ","G5 ","C6 ","C6 ","C6 ","C6 ","C6 ","C6 ",
           "C6 ","C6 ",""   ,"C5 ","D5 ","E5 ","F5 ","G5 ",
           "A5 ","B5 ","C6 ","C6 ","G5 ","G5 ","C6 ","C6 ",
           ]

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

    elif melody[i] == "": # メロディー音が0、つまり無音（休符）の場合
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