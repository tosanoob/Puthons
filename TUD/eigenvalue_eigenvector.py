import numpy as np

input = np.array([
    [2,1,0],
    [1,3,1],
    [0,1,2],
])

# kiểm tra
# diag, V = np.linalg.eig(input)
# print('Tập trị riêng:')
# print(diag)
# print('Ma trận V - các vector đã được chuyển về vector đơn vị')
# print(V)
# print('Ma trận V^-1')
# print(np.linalg.inv(V))

# Phương pháp Danilevsky tìm trị riêng và vector riêng
n = input.shape[0]

B = np.zeros(input.shape)
for i in range (0,n):
    B[i,i] = 1
M = np.zeros(input.shape)
M_1 = np.zeros(input.shape)

A = np.copy(input)
for k in range(n-2,-1,-1):
    for i in range(0,n):
        for j in range(0,n):
            if (i!=k):
                if (i==j):
                    M[i,j] = 1
                    M_1[i,j] = 1
                else:
                    M[i,j] = 0
                    M_1[i,j] = 0
            else:
                M_1[i,j] = A[k+1,j]
                if (j==k):
                    M[i,j] = 1/A[k+1,k]
                else:
                    M[i,j] = -A[k+1,j]/A[k+1,k]
    A = np.matmul(np.matmul(M_1,A),M)
    B = np.matmul(B,M)

print("Ma trận sau biến đổi Danilevsky")
print(A)

print("Giải phương trình tìm trị riêng:")

polynomial_param = [1]
for i in range(0,n):
    polynomial_param.append((-1)*A[0,i])
eig = np.roots(polynomial_param)

# in ma trận chéo hoá:
def printeigval(eig):
    n = eig.shape[0]
    res = []
    for i in range(0,n):
        line = []
        for j in range (0,n):
            if i==j: line.append(eig[i])
            else: line.append(0.)
        res.append(line)
    print(np.array(res))
    return

print('Ma trận chéo hoá A')
printeigval(eig) #eig là tập trị riêng

# hàm tính vector riêng
def eigenvector(n, B, inp):
    res = []
    for i in range(0,n):
        sum = 0
        for j in range(0,n):
            sum += B[i,j]*inp[j]
        res.append(sum)
    return np.array(res)

# tìm ma trận vector riêng:
eigvect = []
for i in range (0,n):
    temp = []
    for j in range (0,n):
        temp.append(eig[i]**(n-j-1))
    eigvect.append(eigenvector(n,B,np.array(temp)))
eigvect = np.array(eigvect)
print('Ma trận vector riêng M')
eigvect = np.transpose(eigvect)
print(eigvect)
print('Ma trận M^-1')
print(np.linalg.inv(eigvect))