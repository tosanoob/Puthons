import numpy as np

P = np.array([
    [0, 0.75, 0.25],
    [0.25,0.25,0.5],
    [0.25,0.5,0.25]
])
# tổng hàng = 1, Pij = xác suất từ trạng thái i sang trạng thái j

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
        
Pstart = np.array([1,0,0])

def P_of_time_t(P,t):
    P_copy = np.copy(P)
    for i in range(t-1):
        P_copy=P_copy@P
    return P_copy

# ma trận xác suất tại thời điểm t
print(format_matrix(P_of_time_t(P,3)))
# vector xác suất tại thời điểm t, dựa trên bắt đầu
print(format_vector(Pstart@P_of_time_t(P,3))) 