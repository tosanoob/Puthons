import numpy as np
def round_digits(x):
    formatted = format(x,".2f")
    return float(formatted)

def format_matrix(X):
    X_copy = np.zeros(X.shape)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            X_copy[i,j] = round_digits(X[i,j])
    return X_copy

def format_vector(X):
    X_copy = []
    for x in X:
        X_copy.append(round_digits(x))
    return np.array(X_copy)

inp = np.array([
    [1,1,4],
    [2,3,5],
    [3,4,6]
])

def det(a):
    # tinh dinh thuc = laplace + gauss
    res = 0
    inp = np.copy(a)
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

# nghịch đảo bằng phần bù đại số:
def inv(a):
    AT = np.transpose(a)
    n = AT.shape[0]
    A_star = np.zeros(a.shape)
    for i in range(n):
        for j in range(n):
            temp = np.copy(AT)
            temp = np.delete(temp,i,0)
            temp = np.delete(temp,j,1)
            A_star[i,j]=np.power(-1,i+j)*det(temp)
    return A_star/det(a)

# nghịch đảo bằng biến đổi gauss
# def inv(a):
#     inp = np.copy(a)
#     n = inp.shape[0]
#     res = np.zeros(inp.shape)
#     for i in range (0,n):
#         res[i,i] = 1
    
#     for k in range (0,n-1):
#         #tìm đổi hai hàng
#         if inp[k,k] == 0:
#             for i in range (k+1,n):
#                 if inp[i,k] != 0:
#                     temp = inp[i,0:n]
#                     inp[i,0:n] = inp[0,0:n]
#                     inp[0,0:n] = temp
#                     temp = res[i,0:n]
#                     res[i,0:n] = res[0,0:n]
#                     res[0,0:n] = temp
#                 break
#         for i in range (k+1,n):
#             m = inp[i,k]/inp[k,k]
#             for j in range (0,n):
#                 inp[i,j]-= inp[k,j]*m
#                 res[i,j]-= res[k,j]*m


#     for k in range (0,n):
#         if np.allclose(inp[k,k],1):
#             m = inp[k,k]
#             for j in range (0,n):
#                 res[k,j]/=m
#                 inp[k,j]/=m

#     for k in range (n-1,-1,-1): #duyệt n-1 hàng từ 0 tới n-1 2 1 0
#         #không cần tìm đổi hai hàng
#         for i in range (k-1,-1,-1): #với pivot ở hàng k, duyệt các hàng i từ 0 tới k-1 1 0
#             m = inp[i,k]/inp[k,k]
#             for j in range (0,n): # tính toán với mọi phần tử hàng i
#                 inp[i,j]-= inp[k,j]*m
#                 res[i,j]-= res[k,j]*m

#     for k in range (0,n):
#         m = inp[k,k]
#         for j in range (0,n):
#             res[k,j]/=m
#             inp[k,j]/=m
#     return res

d = det(inp)
print(d)
if (d!=0):
    invert = inv(inp)
    print(format_matrix(invert))