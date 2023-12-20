# Cần chuẩn bị trước bài toán đã biến đổi để thực hiện đơn hình pha 1
# Bài toán ví dụ:
# Tìm argmin f(x) = -4x1 + 3x2 + x3
# Thoả
#   4x1 + 3x2 + 4x3 = 4
#   4x1 + x2 + 6x3 = 5
# Chuyển bài toán thành dạng chính tắc đặc biệt với 5 ẩn:
# Tìm min g(x) = 0x1 + 0x2 + 0x3 + x4 + x5
# Thoả
#   4x1 + 3x2 + 4x3 + x4 + 0x5 = 4
#   4x1 + x2 + 6x3 + 0x4 + x5 = 5

import numpy as np

def equalorlower0(arr):
    tol = 1e-9
    # có bất kì phần tử nào đó >0
    for i in arr:
        if i>0 and abs(i)>tol:
            return False
    return True

def init_table(C,b,a,X_index):
    # Bảng đơn hình ban đầu:
    m = len(b)
    n = len(C)
    simplex_table = np.zeros((m+1,n+3))
    # Khởi tạo
    for i in range(m):
        simplex_table[i,0] = C[X_index[i]-1]
        simplex_table[i,1] = X_index[i]
        simplex_table[i,2] = b[i]
        simplex_table[i,3:9] = a[i]

    # Tính delta ban đầu
    simplex_table[m,2] = sum(b*simplex_table[0:m,0])
    for j in range(n):
        simplex_table[m,3+j] = sum(simplex_table[0:m,3+j]*simplex_table[0:m,0]) - C[j]

    return simplex_table

def simplex_single_phase(C,init,m,n):
    simplex_table = init
    while True:
        # Kiểm tra tối ưu
        if equalorlower0(simplex_table[m,3:3+m]):
            print("Optimum solution")
            return simplex_table # phương án tối ưu

        # Kiểm tra vô nghiệm
        for j in range(n):
            if simplex_table[m,3+j] > 0 and equalorlower0(simplex_table[0:m,3+j]):
                print("No solution")
                return simplex_table
            
        # Điều chỉnh phương án
        maxdelta = 0
        s = 0
        for j in range(n):
            if simplex_table[m,3+j] > maxdelta:
                maxdelta = simplex_table[m,3+j]
                s = j+1

        mintemp = 1e6
        r = 0
        for i in range(m):
            if simplex_table[i,s+2] == 0: 
                continue
            if simplex_table[i,2] / simplex_table[i,s+2] < mintemp:
                mintemp = simplex_table[i,2]/simplex_table[i,s+2]
                r = i+1
        simplex_table[r-1,1] = s
        simplex_table[r-1,0] = C[s-1]

        # Tính lại bảng đơn hình
        a_new = np.copy(simplex_table)
        for i in range(m+1):
            for j in range(2,n+3):
                if i+1 == r:
                    a_new[i,j] = simplex_table[r-1,j]/simplex_table[r-1,s+2]
                else:
                    a_new[i,j] = simplex_table[i,j] - simplex_table[r-1,j]/simplex_table[r-1,s+2]*simplex_table[i,s+2]

        simplex_table = np.copy(a_new)

# Input của bài toán ví dụ
Ctemp = [0, 0, 0, 1, 1] # hệ số của n' ẩn trong bài toán phụ
C = [-4, 3, 1] # hệ số n ẩn trong bài toán chính
b = [4, 5] 
a = [
    [4, 3, 4, 1, 0], # m phương trình theo dạng chính tắc đặc biệt
    [4, 1, 6, 0, 1]
]
X_index = [4, 5] # chọn trước m ẩn phụ là ẩn cơ bản ban đầu

phase_1 = simplex_single_phase(Ctemp,init_table(Ctemp,b,a,X_index),len(b),len(Ctemp))

print("Bảng đơn hình sau pha 1: ")
print(phase_1)
# Chuyển pha
# Kiểm tra tính vô nghiệm

# Cắt bảng đơn hình mới
m = len(b)
n = len(C)
phase_1 = phase_1[:, :-m]
for i in range(m):
    index = int(phase_1[i,1])
    phase_1[i,0] = C[index-1]

phase_1[m,2] = sum(phase_1[0:m,0]*phase_1[0:m,2])
for j in range(n):
    phase_1[m,3+j] = sum(phase_1[0:m,3+j]*phase_1[0:m,0]) - C[j]

print("Bảng đơn hình chuyển đổi")
print(phase_1)

phase_2 = simplex_single_phase(C,phase_1,m,n)

print(phase_2)
