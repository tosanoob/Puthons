import numpy as np
import csv
import math

def sigmoid(x):
    return 1/(1 + math.exp(-x))

def logistic_sigmoid_regression(X, y, w_init, alpha, tol = 1e-4, loop = 10000):
    w = [w_init]
    d = X.shape[0]
    count = 0
    check_w = 20
    while count < loop:
        # mix data
        mix_id = np.random.permutation(d)
        # print(mix_id)
        for i in mix_id:
            xi = X[i]
            yi = y[i]
            zi = sigmoid(np.dot(w[-1].T, xi))
            w_new = w[-1] + alpha*(yi - zi)*xi
            count += 1
            # stopping criteria
            if count%check_w == 0:
                if np.linalg.norm(w_new - w[-check_w]) < tol:
                    return w
            w.append(w_new)
    return w

i = 0
with open("input.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        i += 1
X = np.empty((i, 4))
y = np.empty((i, 1))
w_init = np.array([2, 1, 1, 1])
i = 0

with open("input.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        X[i] = [float(row[0]), float(row[1]), float(row[2]), float(row[3])]
        if (row[-1] == "Iris-setosa"):
            y[i] = 1
        else: 
            y[i] = 0
        #print(X[i],y[i])
        i+=1

i = 0
w_init = logistic_sigmoid_regression(X, y, w_init, 0.001)
# print(w_init[-1])
# print(sigmoid(np.dot(w_init[-1].T, X[41])))

XTemp = np.empty((10, 4))
with open("output_01.csv") as f:
    i = 0
    reader = csv.reader(f)
    for row in reader:
        XTemp[i] = [float(row[0]), float(row[1]), float(row[2]), float(row[3])]
        i += 1
with open("output_02.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["sepal_length","sepal_width","petal_length","petal_width","Labeling"])
    for j in range (0, 10):
        print(sigmoid(np.dot(w_init[-1].T, XTemp[j])))
        if (sigmoid(np.dot(w_init[-1].T, XTemp[j])) < 0.5):
            writer.writerow([float(XTemp[j][0]), float(XTemp[j][1]), float(XTemp[j][2]), float(XTemp[j][3]), "Iris-versicolor"])
        else:
            writer.writerow([float(XTemp[j][0]), float(XTemp[j][1]), float(XTemp[j][2]), float(XTemp[j][3]), "Iris-setosa"])           

