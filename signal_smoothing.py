import numpy as np
from scipy.io.wavfile import read,write
import scipy.signal as ss

# tạo tín hiệu sin
s_rate = 44100
F0 = 400
dur = 1.
amplitude = 30000

t = np.linspace(0., dur, s_rate)
data = amplitude*np.cos(2*np.pi*t)
filename = "sinusoid_signal.wav"
write("Noise_free_sinusoid.wav",s_rate,data)

# đọc tín hiệu đầu vào
filename = "CantinaBand3.wav"
s_rate, data = read(filename)

# tạo nhiễu
noise_level = 200
noise = np.random.normal(0,noise_level,len(data))
noisy_data = data + noise
write("Noisy_"+filename,s_rate,noisy_data)

# khử nhiễu
M = 1
average_kernel = np.ones(2*M+1)/(2*M+1)
denoised_data = ss.convolve()

y[n] = n*x[n]