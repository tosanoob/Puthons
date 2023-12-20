from scipy.io.wavfile import read,write
from scipy.interpolate import CubicSpline 
from sounddevice import play
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

# upsampling -----------------------------------------------------
def linear(sample_input, ratio): # bổ sung tuyến tính 
    sample_up = []
    for i in range(0, len(sample_input)-1):
        temp = np.linspace(sample_input[i], sample_input[i+1], ratio, endpoint=False).astype(np.int16)
        sample_up.append(temp)

    sample_up = np.array(sample_up)
    sample_up = sample_up.reshape(sample_up.shape[1]*sample_up.shape[0],1)
    return sample_up 

def zero_padding(sample_input, ratio):
    sample_up = []
    for i in range(0, len(sample_input)):
        temp = []
        temp.append(sample_input[i])
        for j in range (0,ratio-1):
            temp.append(0)
        sample_up.append(temp)
    sample_up = np.array(sample_up)
    sample_up = sample_up.reshape(sample_up.shape[1]*sample_up.shape[0],1)
    return sample_up

def cubic_spline(sample_input, ratio): # chia làm các đoạn nội suy đa thức bậc 3
    l = len(sample_input)
    x_axis = np.arange(0,l)
    y_axis = sample_input
    inter_pol = CubicSpline(x_axis,y_axis)
    new_x = np.linspace(0,l,l*ratio)
    new_y = inter_pol(new_x)
    return new_y.astype(np.int16)

# downsampling ---------------------------------------------------
def cut_decimation(sample_input,ratio): # chỉ lấy các chỉ số bội của ratio
    sample_down = []
    for i in range(0, len(sample_input), ratio):
        sample_down.append(sample_input[i])
    return np.array(sample_down)

def average(sample_input, ratio): # lấy trung bình đoạn
    sample_down = []
    for i in range(0, len(sample_input)//ratio-1):
        temp = []
        for k in range(0, ratio):
            temp.append(sample_input[i*ratio + k])
        sample_down.append(np.average(temp).astype(np.int16))
        temp.clear()
    return np.array(sample_down)

# ----------------------------------------------------------------

# tín hiệu gốc, sample_rate = 22050Hz, duration = 3s
original_srate, original_sound = read('CantinaBand3.wav')
sd.play(original_sound,original_srate);

# lấy mẫu lần 1 => x[n], Fs1 = 5000Hz
Fs1 = 10000
t = np.linspace(0.,3., Fs1*3, endpoint=False) # tạo ra tập 15000 vị trí lấy mẫu theo thời gian từ 0 - 3s
indexes = np.round(original_srate*t).astype(np.int32) # tập các index của các mẫu sẽ lấy từ trong original_sound
sample_demo = []
for i in indexes: 
    sample_demo.append(original_sound[i]) # mô phỏng việc lấy mẫu tín hiệu liên tục
sample_demo = np.array(sample_demo)

# ghi file lấy mẫu lần 1
write('CantinaBand3_sampled_at_10kHz.wav',Fs1,sample_demo)

# upsampling
ratio = 2
F_up = Fs1*ratio
sample_up = linear(sample_demo,ratio)
write('CantinaBand3_up_Linear.wav',F_up,sample_up)

# downsampling
ratio = 2
F_down = Fs1//ratio
sample_down = cut_decimation(sample_demo, ratio)
write('CantinaBand3_downsampling_5kHz.wav',F_down,sample_down)

# ------------parameters for plotting-----------------
view_range = np.array([0.5, 0.6]) # seconds
y_height = 2000


plt.subplot(2,2,1)
range = (view_range*original_srate).astype(np.int16)
plt.plot(original_sound[range[0]:range[1]])
plt.ylim(-y_height,y_height)
plt.title('Original signal - 22050Hz')

plt.subplot(2,2,2)
range = (view_range*Fs1).astype(np.int16)
plt.plot(sample_demo[range[0]:range[1]])
plt.ylim(-y_height,y_height)
plt.title('First sampling signal at 10000Hz')

plt.subplot(2,2,3)
range = (view_range*F_up).astype(np.int16)
plt.plot(sample_up[range[0]:range[1]])
plt.ylim(-y_height,y_height)
plt.title('Upsampling with linear method, 20000Hz')

plt.subplot(2,2,4)
range = (view_range*F_down).astype(np.int16)
plt.plot(sample_down[range[0]:range[1]])
plt.ylim(-y_height,y_height)
plt.title('Downsampling by decimation, 5000Hz')

plt.tight_layout()
plt.show()