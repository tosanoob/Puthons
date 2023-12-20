import numpy as np

A = np.zeros((10,10))
A[0,0] = 1
A[0,1] = 2
A[9,8] = 2
A[9,9] = 5
for i in range(1,9):
    A[i,i-1] = 2
    A[i,i] = 5
    A[i,i+1] = 2

(U, D, V) = np.linalg.svd(A)
print("--U-------------------------")
print(U)
print("--D-------------------------")
print(np.diag(D))
print("--V-------------------------")
# print(np.transpose(V))
print(V)