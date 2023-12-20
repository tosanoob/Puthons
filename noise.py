from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import numpy as np

Fs = 44100 
t = np.linspace(0.,1.,Fs)
data = 15000 * np.sin(2*np.pi*800*t) + 15000
write("test.wav",44100,data.astype(np.int16))
