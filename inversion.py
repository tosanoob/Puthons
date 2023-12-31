import pandas as pd
import numpy as np

inp = pd.read_csv("input.csv",header=None)
inp.drop(0,axis = 0)
inp.drop(0,axis = 1)

# tim nghich dao cua inp
# dung bien doi gauss

# 1 2 3
# 2 3 4
# 3 4 5

def det(inp):
    # tinh dinh thuc = laplace + gauss
    res = 0
    n = inp.shape[0]
    if (n>2):           
        if (inp[0,0]==0):
            #tìm đổi hai hàng
            count = 1
            for i in range (1,n):
                if inp[i,0] != 0:
                    temp = inp[i,0:n]
                    inp[i,0:n] = inp[0,0:n]
                    inp[0,0:n] = temp
                    break
                else: 
                    count+=1
            if count==n: 
                return 0
            
        for i in range (1,n):
            m = inp[i,0]/inp[0,0]
            for j in range (0,n):
                inp[i,j]-= inp[0,j]*m  
        res = (-1)**(i+j)*inp[0,0]*det(inp[1:n,1:n])
    else:
        res = inp[0,0]*inp[1,1] - inp[0,1]*inp[1,0]
    return res

def inv(inp):
    n = inp.shape[0]
    res = np.zeros(inp.shape)
    for i in range (0,n):
        res[i,i] = 1
    for k in range (0,n-1):
        #tìm đổi hai hàng
        for i in range (k+1,n):
            if inp[i,k] != 0:
                temp = inp[i,0:n]
                inp[i,0:n] = inp[0,0:n]
                inp[0,0:n] = temp
                temp = res[i,0:n]
                res[i,0:n] = res[0,0:n]
                res[0,0:n] = temp
                break
        for i in range (k+1,n):
            m = inp[i,k]/inp[k,k]
            for j in range (k,n):
                inp[i,j]-= inp[k,j]*m
                res[i,j]-= res[k,j]*m
    print(inp)
    return res

arr = np.array(inp)

d = det(arr)
if d == 0:
    print("Dinh thuc = 0, khong kha nghich")
else:
    print(inv(arr))
