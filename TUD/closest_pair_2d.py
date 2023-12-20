import math
import random
import numpy as np
import matplotlib.pyplot as plt

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair(p): #this just return the distance
    n = len(p)

    if n==2:
        return euclidean_distance(p[0],p[1])
    
    sorted_index = sorted(range(n), key=lambda i: p[i])
    sorted_p = [p[i] for i in sorted_index]

    mid = n//2
    left_p = sorted_p[:mid]
    right_p = sorted_p[mid:]
    
    left_closest_pair = closest_pair(left_p)
    right_closest_pair = closest_pair(right_p)

    min_dist = min(left_closest_pair, right_closest_pair)

    middle_strip = [i for i in range(n) if abs(p[i,0] - p[mid,0]) < min_dist]
    middle_strip.sort(key=lambda i: p[i])

    for i in range(len(middle_strip)):
        for j in range(i+1, min(i+8,len(middle_strip))): #limit the comparison time within middle strip
            dist = euclidean_distance(p[i],p[j])
            min_dist = min(dist,min_dist)
    
    # mid_closest_pair = closest_pair(middle_strip)
    # min_dist = min(min_dist, mid_closest_pair)
    return min_dist

# Example usage
if __name__ == "__main__":
    # Sample points as separate arrays for x and y coordinates
    n = 30
    x = [random.uniform(0,10) for _ in range(n)]
    y = [random.uniform(0,10) for _ in range(n)]
    p = np.array([x,y])
    p = np.transpose(p)

    dist = closest_pair(p)
    print('Khoang cach ngan nhat giua 2 diem:',dist)
    plt.plot(x,y)
    plt.imshow()

