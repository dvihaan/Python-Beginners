import simpleaudio as sa
from playsound import playsound
import numpy as np


def beep(pitch = 1000,length = 1):    
    frequency = pitch

    fs = 44100

    seconds = length

    t = np.linspace(0,seconds,seconds*fs,False)

    note = np.sin(frequency*t*2*np.pi)

    audio = note*(2**15-1)/np.max(np.abs(note))
    audio = audio.astype(np.int16)

    play_obj = sa.play_buffer(audio,1,2,fs)
    play_obj.wait_done()

def loopFreq(min = 10,max = 1000, step = 50):
    for i in range(min,max,step):
        beep(i,1)

def HundredEightNotes():
    c = 1
    for i in range(-57,51):
        power = i/12
        print(c, i)
        beep(440*(2**power),1)
        c = c+1

def main():
    #loopFreq()
    HundredEightNotes()
       
if __name__ == '__main__':
    main()                                                                    