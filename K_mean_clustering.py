import numpy as np
import pandas as pd

def result_distance(centroids,idx):
    distances = np.sqrt(np.sum((X - centroids[idx])**2, axis=1))
    sum_of_distances = np.sum(distances)
    return sum_of_distances
#############################################################
def initialize_K_centroid(X,K):
    centroids = X[np.random.choice(X.shape[0], K, replace=False), :]
    return centroids

def find_closest_centroid(X, centroids):
    distances = np.sqrt(np.sum((X - centroids[:, np.newaxis])**2, axis=2))
    idx = np.argmin(distances, axis=0)
    return idx

def compute_means(X,idx,K,centroids):
    for k in range (K):
        centroids[k] = np.mean(X[idx == k], axis=0)
    return centroids

def find_k_means(X, K, max_iters = 10): 
    centroids = initialize_K_centroid(X,K)
    for i in range (max_iters):
        idx = find_closest_centroid(X, centroids)
        centroids = compute_means(X,idx,K,centroids)
    return centroids, idx
############################################################
data = pd.read_csv("Countries-exercise.csv",header=None)
data = data.drop(0,axis = 0)
data = data.drop(0,axis = 1)

X = np.array(data.astype(float))
save = []
# result = k_means_clustering(X,10)
# print(result[0])
# print(result[1])

for K in range (1,11):
    result = find_k_means(X,K)
    save.append(result_distance(result[0],result[1]))
for K in range (0,10):
    print(K+1)
    print(save[K]) 
    


