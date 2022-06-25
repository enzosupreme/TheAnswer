import random
import time
import board
from digitalio import DigitalInOut, Direction, Pull
import audioio
import audiocore
import neopixel
from colorpallette import colors

#Audio Files
response = [
        "yes.wav",
        "Utra Yes.wav",
        "of course.wav",
        "no.wav",
        "Ultra No.wav",
        "nope.wav"
        ]

# Button pins:
a = DigitalInOut(board.A4)
a.direction = Direction.INPUT
a.pull = Pull.UP

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1)


#Color Pallete import
col = [
    colors.GREEN,
    colors.RED,
    colors.MINT,
    colors.BLUE,
    colors.CYAN,
    colors.NEON,
    colors.CYBER,
    colors.MAGENTA,
    colors.ORANGE,
]


# Audio Play File
def play_file(playname, x):
    print("Playing File " + playname)
    wave_file = open(playname, "rb")
    with audiocore.WaveFile(wave_file) as wave:
        with audioio.AudioOut(board.A0) as audio:
            audio.play(wave)
            while audio.playing:
                for i in range(len(pixels)):
                    pixels[i] = col[x]
                    time.sleep(0.1)
                pixels.fill(0)
                time.sleep(0.3)
                pixels.show()


while True:
    ran = random.randint(0,5)
    x = 0
    if(ran < 3):
        x = 0
    else:
        x = 1
    if not a.value:
        play_file(response[ran],x)

