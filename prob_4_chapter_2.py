from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

# Âm hình sin có F0 = 400
sampling_rate = 44100; F0 = 800
amplitude = 30000
t = np.linspace(0., 1., sampling_rate+1)
# Đây là hàm tín hiệu âm thanh
data = amplitude * np.sin(2.*np.pi*F0*t)
sd.play(data, sampling_rate)
write("example.wav", sampling_rate, data.astype(np.int16))

# Lấy mẫu với Fs1 = 3*F0
# Âm thanh kéo dài 1s
Fs1 = 3*F0
n_1 = np.linspace(0., 1., Fs1+1)
sample_1 = amplitude * np.sin(2.*np.pi*F0*n_1)

# Lấy mẫu với Fs2 = 1.5*F0
Fs2 = 1.5*F0
n_2 = np.linspace(0., 1., int(Fs2)+1)
sample_2 = amplitude * np.sin(2.*np.pi*F0*n_2)

# Biểu diễn đồ thị 2 mẫu trên trục thời gian:
plt.plot(n_1,sample_1,'r',label = 'Fs1 = 3F0')
plt.plot(n_2,sample_2,'g',label = 'Fs2 = 1.5F0')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('2 tập mẫu tín hiệu với sampling rate khác nhau')
plt.show()

# Xuất file lấy mẫu ở dạng .wav:
write("example_sampled_Fs1.wav", int(Fs1), sample_1.astype(np.int16)) # Khôi phục được
write("example_sampled_Fs2.wav", int(Fs2), sample_2.astype(np.int16)) # Bị lỗi