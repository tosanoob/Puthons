import numpy as np
import math as m
import pandas as pd

inp = pd.read_csv("input.csv",header=None)
inp.drop(0,axis = 0)
inp.drop(0,axis = 1)

# print(inp)

# định nghĩa hàm phi(n)
def phi(n):
    res = n
    i = 2
    while i<n*n:
        if n%i==0:
            while n%i==0:
                n/=i
            res -= res/i
        i+=1
    if n!=1: 
        res -= res//n
    return res

# khởi tạo ma trận đầu vào mat, tham số M, Mi và Y; res là kết quả
mat = np.array(inp)
M = 1
Mi = np.ones((mat.shape[0],1))
Y = np.ones((mat.shape[0],1))
res = 0

# tính M = m1.m2...mk
for i in range (0,mat.shape[0]):
    M*=mat[i,1]

# thuật toán chính
for i in range (0,mat.shape[0]):
    Mi[i] = M/mat[i,1] # tính Mi = M/mi

    # tính Yi = nghịch đảo module Mi (mod mi)
    # sử dụng hàm phi: Yi = Mi^(phi(mi) - 1) (mod mi)
    Y[i] = m.pow(Mi[i]%mat[i,1],phi(mat[i,1])-1)%mat[i,1] 

    # cộng ai*Mi*Yi vào res, lấy modulo M
    res += mat[i,0]*Mi[i]*Y[i]
    res %= M

print("x dong du voi",int(res),"modulo",M)
