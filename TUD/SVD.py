import numpy as np

A = np.array([
    [1,3,5],
    [3,9,11],
    [5,11,17]
])

# A = np.array([
#         [1,-0.8],
#     [0,1],
#     [1,0]
# ])

# khởi tạo ma trận input
# A = np.zeros((10,10))
# A[0,0] = 1
# A[0,1] = 2
# A[9,8] = 2
# A[9,9] = 5
# for i in range(1,9):
#     A[i,i-1] = 2
#     A[i,i] = 5
#     A[i,i+1] = 2

def round_to_5_digits(x):
    formatted = format(x,".5f")
    return float(formatted)

def format_matrix(X):
    X_copy = np.zeros(X.shape)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            X_copy[i,j] = round_to_5_digits(X[i,j])
    return X_copy

def eigenvector(n, B, inp): # hàm tính vector riêng theo phương pháp Danilevski
    res = []
    for i in range(0,n):
        sum = 0
        for j in range(0,n):
            sum += B[i,j]*inp[j]
        res.append(sum)
    return np.array(res)

def eigenvalue_decomposition(input): # hàm tính trị riêng, vector riêng theo phương pháp Danilevski
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

    polynomial_param = [1]
    for i in range(0,n):
        polynomial_param.append((-1)*A[0,i])
    eig = np.roots(polynomial_param)
    eig = np.sort(eig)[::-1]

    eigvect = []
    for i in range (0,n):
        temp = []
        for j in range (0,n):
            temp.append(eig[i]**(n-j-1))
        eigvect.append(eigenvector(n,B,np.array(temp)))
        # chuẩn hoá về vector đơn vị
        eigvect[i] = eigvect[i]/np.linalg.norm(eigvect[i])
    eigvect = np.array(eigvect)
    return eig, np.transpose(eigvect)

#-------------------------------------------------
(row,col) = A.shape
# tính V trước, sau đó ui = Avi/delta i
ATA = np.matmul(np.transpose(A),A) 
diag, V = eigenvalue_decomposition(ATA) # tính tập trị riêng, vector riêng của ATA
delta = np.sqrt(diag)
U = []
D = np.zeros(A.shape)
for i in range(row):
    D[i,i] = delta[i] # tạo ma trận chéo D
    U.append(A@V[:,i]/delta[i]) # gán cột ui = Avi/deltai vào U

AAT = np.matmul(A,np.transpose(A)) 
diag_1, U_temp = eigenvalue_decomposition(AAT) # tính tập trị riêng, vector riêng của AAT
for i in range(row,col):
    U.append(U_temp[:,i]) # trong trường hợp row<col, gán thêm các cột U còn thiếu
U = np.array(U)
U = np.transpose(U)

check = U@D@np.transpose(V)
print("--U-------------------------")
print(format_matrix(U))
print("--D-------------------------")
print(format_matrix(D))
print("--VT-------------------------")
print(format_matrix(V))
# print(check)
# print(np.allclose(A,check))

# to check result with python library
# u, s, vh = np.linalg.svd(A)
# print(u)
# print(vh)
# print(s)
# d = np.zeros(A.shape)
# for i in range(0,len(s)):
#     d[i,i] = s[i]
# print(u@d@vh)
