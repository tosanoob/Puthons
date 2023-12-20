#kmeans
#input Countries.csv
#k mean _ with k = 5

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#trả về np array 2 chiều: N hàng, d cột
def read_data(filename):
    with open(filename) as inp:
        reader = pd.read_csv(inp).values
        return np.array(reader)
    
def random_data(N, d):
    return 10*np.random.random((N,d))-5

#tạo K tâm => trả về một ap array 2 chiều: K hàng, d cột
def init_K(dim, K):
    return 100*np.random.random((K,dim))-50

#duyệt tất cả các record và label tâm
def clustering(X, centroids):
    N = X.shape[0]
    label = np.zeros((1,N))
    for i in range (N):
        xi = X[i,:]
        min = np.linalg.norm(xi - centroids[0])
        for index, c in enumerate(centroids):
            if np.linalg.norm(xi - c) < min:
                min = np.linalg.norm(xi - c)
                label[0,i] = index
    return label

def cluster_of_same_label(index, label, X):
    selected = []
    for i in range(label.shape[1]):
        if label[0,i] == index:
            selected.append(X[i])
    return np.array(selected)

def isEqual(last_label, label):
    for i in range (label.shape[1]):
        if last_label[0,i] != label[0,i]:
            return False
    return True

def K_means(X, centroids, loop = 20):
    count = 0
    last_label = np.zeros((1,X.shape[0]))
    while (count < loop):
        label = clustering(X, centroids)
        #kiểm tra, nếu tập label không đổi => thoát
        if isEqual(last_label, label):
            return centroids, label
        new_centroids = np.zeros(centroids.shape)
        for index in range (centroids.shape[0]):
            new_centroids[index] = np.mean(cluster_of_same_label(index,label,X), axis = 0)
        centroids = new_centroids.copy()
        last_label = label
        count+=1
    return centroids, label

if __name__ == "__main__":
    X = read_data("Countries.csv")[:,1:]
    
    K = 5
    print("Initial centroids:")
    centroids_init = init_K(X.shape[1], K)
    print(centroids_init)
    
    result_centroids, label = K_means(X, centroids_init)
    print("Centroids:")
    for c in result_centroids:
        print(c)
    print("----Clustering----")
    print(label)

    plt.scatter(X[:,0],X[:,1], c = label, cmap = 'viridis')
    plt.scatter(result_centroids[:,0], result_centroids[:,1],marker = 'x', color = 'red', s = 100, label = 'Centroids')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("K-means clustering")
    plt.show()
