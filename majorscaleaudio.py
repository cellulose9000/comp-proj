"""audio of notes"""
import numpy as np
import simpleaudio as sa
import majorscale as ms
def gscale():
    freq=ms.gM()
    for i in range(len(freq)):
        audio=freq[i]*(2**15 - 1) / np.max(np.abs(freq[i]))
        audio=audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, 44100)
        play_obj.wait_done()
def ascale():
    freq=ms.aM()
    for i in range(len(freq)):
        audio=freq[i]*(2**15 - 1) / np.max(np.abs(freq[i]))
        audio=audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, 44100)
        play_obj.wait_done()
def fscale():
    freq=ms.fM()
    for i in range(len(freq)):
        audio=freq[i]*(2**15 - 1) / np.max(np.abs(freq[i]))
        audio=audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, 44100)
        play_obj.wait_done()
def cscale():
    freq=ms.cM()
    for i in range(len(freq)):
        audio=freq[i]*(2**15 - 1) / np.max(np.abs(freq[i]))
        audio=audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, 44100)
        play_obj.wait_done()
def dscale():
    freq=ms.dM()
    for i in range(len(freq)):
        audio=freq[i]*(2**15 - 1) / np.max(np.abs(freq[i]))
        audio=audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, 44100)
        play_obj.wait_done()
def escale():
    freq=ms.eM()
    for i in range(len(freq)):
        audio=freq[i]*(2**15 - 1) / np.max(np.abs(freq[i]))
        audio=audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, 44100)
        play_obj.wait_done()
def bscale():
    freq=ms.bM()
    for i in range(len(freq)):
        audio=freq[i]*(2**15 - 1) / np.max(np.abs(freq[i]))
        audio=audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, 44100)
        play_obj.wait_done()