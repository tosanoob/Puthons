import numpy as np
import matplotlib.pyplot as plt

# Hàm tín hiệu gốc (A = 5, phi = 0, F0 = 400Hz):
def signal_function(t, A = 5, F0 = 400, phi = 0):
    return A*np.cos(2*np.pi*F0*t + phi)

# Hàm lấy mẫu theo sampling_rate, sampling_time
def signal_sample(sampling_rate, sampling_time):
    time_label = np.linspace(0., sampling_time, int(sampling_time*sampling_rate+1)) 
    sample = signal_function(time_label)
    return sampling_rate,sample,time_label

# Thực hiện lấy mẫu với 2 sampling_rate khác nhau: Fs1 = 2F0 = 800, Fs2 = 3F0 = 1200
s_rate_1, sample_1, time_1 = signal_sample(800, 0.1)
print(time_1)
s_rate_2, sample_2, time_2 = signal_sample(1200,0.1)
s_rate_max, data, time = signal_sample(22050,0.1)
# Vẽ biểu đồ chỉ với tập mẫu:
plt.plot(sample_1, 'r', label = 'Signal x1[n]')
plt.plot(sample_2, 'g', label = 'Signal x2[n]')
plt.title('Tập mẫu thu được khi lấy mẫu với 2 sampling rate khác nhau')
plt.xlabel('N')
plt.ylabel('Y')
plt.show()

# Kết hợp chỉ số thời gian:
# plt.plot(time, data, 'b', label = 'Original')
plt.plot(time_1, sample_1, 'r', label = 'Signal x1[n]')
plt.plot(time_2, sample_2, 'g', label = 'Signal x2[n]')
plt.title('Dựng lại tín hiệu khi có sampling rate')
plt.xlabel('Time t')
plt.ylabel('Amplitude')
plt.show()

