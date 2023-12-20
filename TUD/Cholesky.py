import numpy as np

# a = np.array([
#     [4,10,8],
#     [10,26,26],
#     [8,26,61]
# ])

# khởi tạo ma trận input
a = np.zeros((15,15))
a[0,0] = 1
a[0,1] = 2
a[14,13] = 2
a[14,14] = 5
for i in range(1,14):
    a[i,i-1] = 2
    a[i,i] = 5
    a[i,i+1] = 2

eigen = np.linalg.eigvals(a)

    # kiểm tra ma trận vuông:
if a.shape[0] != a.shape[1]:
    print('Ma trận không vuông')
    
    # kiểm tra ma trận đối xứng:
elif (a != np.transpose(a)).any():
    print('Ma trận không đối xứng')

    # kiểm tra ma trận xác định dương
elif (eigen<=0).any():
    print('Ma trận không xác định dương')

else:
    # thuật toán chính
    n = a.shape[0]
    l = np.zeros(a.shape)
    for i in range(0,n):
        for j in range(0,i+1):
            if i == j: # trường hợp i = j
                sum = 0
                for k in range(0,j):
                    sum += l[i,k]**2
                l[i,j] = np.sqrt(a[i,j] - sum)
            else: # trường hợp i!= j
                sum = 0
                for k in range(0,j):
                    sum += l[i,k]*l[j,k]
                l[i,j] = 1/l[j,j]*(a[i,j] - sum)
    print("Ma trận Cholesky:")
    print(l)
