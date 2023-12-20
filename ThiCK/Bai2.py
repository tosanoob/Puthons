import numpy as np
import pandas as pd

def convert_labels(y):
    Y1 = []
    Y2 = []
    Y3 = []
    for item in y:
        if item==0:
            Y1.append(1)
            Y2.append(0)
            Y3.append(0)
        if item==1:
            Y1.append(0)
            Y2.append(1)
            Y3.append(0)
        if item==2:
            Y1.append(0)
            Y2.append(0)
            Y3.append(1)
    return np.array([Y1,Y2,Y3])

def softmax(Z):
    Z = np.array(Z, dtype=object)
    e_Z = np.exp(Z)
    A = e_Z / e_Z.sum(axis = 0)
    return A

# cost or loss function  
def cost(X, Y, W):
    A = softmax(W.T.dot(X))
    return -np.sum(Y*np.log(A))

def grad(X, Y, W):
    A = softmax((W.T.dot(X)))
    E = A - Y
    return X.dot(E.T)
    
def numerical_grad(X, Y, W, cost):
    eps = 1e-6
    g = np.zeros_like(W)
    for i in range(W.shape[0]):
        for j in range(W.shape[1]):
            W_p = W.copy()
            W_n = W.copy()
            W_p[i, j] += eps 
            W_n[i, j] -= eps
            g[i,j] = (cost(X, Y, W_p) - cost(X, Y, W_n))/(2*eps)
    return g 

def softmax_regression(X, y, W_init, eta, tol = 1e-4, max_count = 10000):
    W = [W_init]    
    C = W_init.shape[1]
    Y = convert_labels(y)
    it = 0
    N = X.shape[1]
    d = X.shape[0]
    
    count = 0
    check_w_after = 20
    while count < max_count:
        # mix data 
        mix_id = np.random.permutation(N)
        for i in mix_id:
            xi = X[:, i].reshape(d, 1)
            yi = Y[:, i].reshape(C, 1)
            ai = softmax(np.dot(W[-1].T, xi))
            W_new = W[-1] + eta*xi.dot((yi - ai).T)
            count += 1
            # stopping criteria
            if count%check_w_after == 0:                
                if np.linalg.norm(W_new - W[-check_w_after]) < tol:
                    return W
            W.append(W_new)
    return W

#đọc file trả về tập dữ liệu
def read_file(file):
    with open(file) as inp:
        reader = pd.read_csv(inp).values
        return reader

#chỉnh sửa thành giá trị số, trả về tập X, y (np array)
def modify_data(data, y_available = True):
    if y_available:
        for item in data:
            if item[4] == 'Iris-setosa':
                item[4] = 0
            elif item[4] == 'Iris-versicolor': item[4] = 1
            elif item[4] == 'Iris-virginica': item[4] = 2
        return np.array(data[:,0:4]), np.array(data[:,4])
    else:
        return np.array(data[:,0:data.shape[1]-1])

C = 3 #phân 3 lớp

(X , y) = modify_data(read_file("input.csv"))
N = X.shape[0]
d = X.shape[1]
X.reshape((d,N))
d = X.shape[0]
eta = .05 
W_init = np.random.randn(d, C)
y = np.asarray(y).T
W = softmax_regression(X, y, W_init, eta)

X_test = modify_data(read_file('output_01.csv'))[0]
df_result = pd.DataFrame(columns=['sepal_length','sepal_width','petal_length','petal_width','Labeling'])

for i in range (0,X_test.shape[0]):
        #versicolor = 1, setosa = 0
        label_1 , label_2, label_3 = 'Iris-setosa' , 'Iris-versicolor', 'Iris-virginica'
        if (np.dot(W[-1].T,X_test[i])>0.5):
            print(label_2)
            new_row = pd.DataFrame({'sepal_length':X_test[i,0],
                       'sepal_width':X_test[i,1],
                       'petal_length':X_test[i,2],
                       'petal_width':X_test[i,3],
                       'Labeling':label_2
                       }, index=[0])
        else:
            print(label_1) 
            new_row = pd.DataFrame({'sepal_length':X_test[i,0],
                       'sepal_width':X_test[i,1],
                       'petal_length':X_test[i,2],
                       'petal_width':X_test[i,3],
                       'Labeling':label_1
                       }, index=[0])
        if (np.dot(W[-1].T,X_test[i])>0.5):
            print(label_3) 
            new_row = pd.DataFrame({'sepal_length':X_test[i,0],
                       'sepal_width':X_test[i,1],
                       'petal_length':X_test[i,2],
                       'petal_width':X_test[i,3],
                       'Labeling':label_1
                       }, index=[0])
        df_result = df_result._append(new_row, ignore_index=True)
df_result.to_csv('output.csv',index=False)
