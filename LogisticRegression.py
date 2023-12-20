import numpy as np
import csv

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def logistic_sigmoid_regression(X, y, w_init, alpha, tol = 1e-4, loop = 100000):
    w = [w_init]
    N = X.shape[1]
    d = X.shape[0]
    count = 0
    check_w = 20
    while count < loop:
        # mix data
        mix_id = np.random.permutation(N)
        for i in mix_id:
            xi = X[:,i].reshape(d,1)
            yi = y[i]
            zi = sigmoid(np.dot(w[-1].T, xi))
            w_new = w[-1] - alpha*(zi - yi)*xi
            count += 1
            # stopping criteria
            if count%check_w == 0:
                if np.linalg.norm(w_new - w[-check_w]) < tol:
                    return w
            w.append(w_new)
    return w

with open('input.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    X = np.array((1,4), float)
    y = np.array((1,1), float)
    for row in reader:
        new_row = np.array((row[0],row[1],row[2],row[3]))
        X = np.insert(X, -1, new_row, axis=0)
        if row[4] == 'Iris-setosa': y = np.insert(y, -1, np.array(([0])), 0)
        else: y = np.insert(y, -1, np.array(([1])), 0)
    
X = np.delete(X,0,0)
X = np.delete(X,-1)
y = np.delete(y,0,0)
y = np.delete(y,-1)

X = X.reshape((4,80))
w_init = np.array([2,2,2,2]).reshape(4,1)
result = logistic_sigmoid_regression(X,y,w_init,0.001)

#logistic regression weight vector 

with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    Xnew = np.array((4,1), float)
    ynew = np.array((1,1),float)
    for row in reader:
        new_row = np.array(([row[0],row[1],row[2],row[3]]),float)
        print(row[0],row[1],row[2],row[3])
        new_row = new_row.reshape((4,1))
        r = np.dot(result[-1].T,new_row)
        label = sigmoid(np.dot(result[-1].T,new_row))
        print(label)



