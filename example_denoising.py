import numpy as np
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt

# #sinh tín hiệu hàm sin
# s_rate = 44100
# F_0 = 500
# A = 30000;
# t = np.linspace(0.,1.,s_rate)
# data = 30000*np.cos(2*np.pi*t)
# filename = 'Sinusoidal '+ str(F_0) + 'Hz sound'

#đọc file
filename = 'CantinaBand3'
s_rate, data = read(filename+'.wav')

#thêm nhiễu
noise_level = 100
noisy_data = data + noise_level*np.random.randn(len(data))
write(filename+'noisy.wav',s_rate,noisy_data)

#khử nhiễu bằng average filter 2M+1
M = 1
filter = np.ones(2*M+1)/(2*M+1)
denoised_data = np.convolve(noisy_data,filter,'same')
write(filename+'denoised.wav',s_rate,denoised_data)

plt.subplot(3,1,1)
plt.plot(data)
plt.title('Original data')
plt.subplot(3,1,2)
plt.plot(noisy_data)
plt.title('Noisy data')
plt.subplot(3,1,3)
plt.plot(denoised_data)
plt.title('Denoised data')
plt.show()