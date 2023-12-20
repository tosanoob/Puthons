from scipy.io.wavfile import read,write
import numpy as np
import matplotlib.pyplot as plt

def signal_reproduce(sampling_rate, sample):
    time_label = np.linspace(0., sample.size/sampling_rate, sample.size)
    # time_label = []
    # time = 0
    # for i in sample:
    #     time_label.append(time)
    #     time+=1/sampling_rate
    return time_label,sample

# Đọc file wav:
input_data = read("CantinaBand3.wav")
sampling_rate = input_data[0]
audio = input_data[1]
audio_over_time = signal_reproduce(sampling_rate, audio)

# Dựng đồ thị theo số mẫu
plt.plot(audio)
plt.ylabel("Amplitude")
plt.xlabel("Samples")
plt.title("Cantina Band sample, sampling rate = " + str(sampling_rate) + 'Hz')
plt.show()

# Dựng đồ thị sóng theo trục thời gian
plt.plot(audio_over_time[0][30000:32000],audio_over_time[1][30000:32000])
plt.ylabel("Amplitude")
plt.xlabel("Time (second)")
plt.title("Cantina Band sample, sampling rate = " + str(sampling_rate) + 'Hz')
plt.show()

#Xuất 3 file .wav với 3 sampling_rate khác nhau:
write('CantinaBand3_Fs.wav',sampling_rate,audio) # Tốc độ phát bình thường
write('CantinaBand3_Fs_2.wav',sampling_rate//2,audio) # Tốc độ phát = 1/2
write('CantinaBand3_2_Fs.wav',sampling_rate*2,audio) # Tốc độ phát x2
