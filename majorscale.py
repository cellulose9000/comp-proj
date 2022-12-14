"""scalenotes"""
import numpy as np
def gM():
    freq=[]
    t = np.linspace(0, 1, 1 * 44100, False)
    for i in range(8):
        f1=np.sin((195.998+((i)*25.472))*t*2*np.pi)
        freq.append(f1)
    return(freq)
def aM():
    freq=[]
    t = np.linspace(0, 1, 1 * 44100, False)
    for i in range(8):
        f1=np.sin((220+((i)*26.962))*t*2*np.pi)
        freq.append(f1)
    return(freq)
def fM():
    freq=[]
    t = np.linspace(0, 1, 1 * 44100, False)
    for i in range(8):
        f1=np.sin((174.614+((i)*21.384))*t*2*np.pi)
        freq.append(f1)
    return(freq)
def cM():
    freq=[]
    t = np.linspace(0, 1, 1 * 44100, False)
    for i in range(8):
        f1=np.sin((130.813+((i)*16.019))*t*2*np.pi)
        freq.append(f1)
    return(freq)
def dM():
    freq=[]
    t = np.linspace(0, 1, 1 * 44100, False)
    for i in range(8):
        f1=np.sin((146.832+((i)*17.982))*t*2*np.pi)
        freq.append(f1)
    return(freq)
def eM():
    freq=[]
    t = np.linspace(0, 1, 1 * 44100, False)
    for i in range(8):
        f1=np.sin((164.814+((i)*20.183))*t*2*np.pi)
        freq.append(f1)
    return(freq)
def bM():
    freq=[]
    t = np.linspace(0, 1, 1 * 44100, False)
    for i in range(8):
        f1=np.sin((246.942+((i)*30.241))*t*2*np.pi)
        freq.append(f1)
    return(freq)