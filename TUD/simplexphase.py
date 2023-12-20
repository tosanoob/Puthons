# Giải bài toán bằng phương pháp đơn hình
# input: tập hệ số cj, ma trận phương trình a sum aij*xj = b
# j from 1 to n, i from 1 to m

# chương trình chỉ nhận dạng chính tắc đặc biệt
# cần chuẩn bị bằng tay để đưa ra dạng chính tắc đặc biệt như sau:
# tổ chức các phương trình thoả mãn: 
#   các ẩn cơ bản nằm sau cùng phương trình
#   vị trí ẩn cơ bản tăng dần

# 4 bước trong một vòng lặp đơn hình:
#   1. Kiểm tra tối ưu
#   2. Kiểm tra vô nghiệm
#   3. Điều chỉnh phương án cơ bản
#   4. Tính bảng đơn hình mới
import numpy as np

def equalorlower0(arr):
    tol = 1e-9
    # có bất kì phần tử nào đó >0
    for i in arr:
        if i>0 and abs(i)>tol:
            return False
    return True

# ví dụ một input thoả
C = [0, 6, 5, -64, -4, 0, 0] # hệ số của n ẩn
b = [0, 0, 2] 
a = [
    [1/3, -2, -3, 12, 1, 0, 0], # m phương trình theo dạng chính tắc đặc biệt
    [1/2, -2, -1/6, 2/3, 0, 1, 0],
    [0, 1, 1, -9, 0, 0, 1]
]
X_index = [5, 6, 7] # chọn trước m ẩn cơ bản ban đầu

def simplex_single_phase(C,b,a,X_index):

    # Bảng đơn hình ban đầu:
    m = len(b)
    n = len(C)
    simplex_table = np.zeros((m+1,n+3))
    # Khởi tạo
    for i in range(m):
        simplex_table[i,0] = C[X_index[i]-1]
        simplex_table[i,1] = X_index[i]
        simplex_table[i,2] = b[i]
        simplex_table[i,3:3+n] = a[i]

    # Tính delta ban đầu
    simplex_table[m,2] = sum(b*simplex_table[0:m,0])
    for j in range(n):
        simplex_table[m,3+j] = sum(simplex_table[0:m,3+j]*simplex_table[0:m,0]) - C[j]

    print(simplex_table)

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
        print(simplex_table)

final_table = simplex_single_phase(C,b,a,X_index)
print(final_table)
