import numpy as np
import matplotlib.pyplot as plt

def euclidean_distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def closest_pair(x, y): #this return the closest pair and their distance
    n = len(x)
    # Base case: if there is only one point => return infinite
    if n == 1: return 1e8, (x[0], y[0]), (x[0], y[0])
    # Base case: if there are only two points, return their distance and the points
    if n == 2:
        return euclidean_distance(x[0], y[0], x[1], y[1]), (x[0], y[0]), (x[1], y[1])

    # Sort points based on their x-coordinates
    sorted_indices = sorted(range(n), key=lambda i: x[i])
    sorted_x = [x[i] for i in sorted_indices]
    sorted_y = [y[i] for i in sorted_indices]

    # Split the points into two halves
    mid = n // 2
    left_x, left_y = sorted_x[:mid], sorted_y[:mid]
    right_x, right_y = sorted_x[mid:], sorted_y[mid:]

    # Recursively find the closest pair in each half
    left_closest_pair_distance, left_point1, left_point2 = closest_pair(left_x, left_y)
    right_closest_pair_distance, right_point1, right_point2 = closest_pair(right_x, right_y)

    # Determine the minimum distance and corresponding points
    if left_closest_pair_distance < right_closest_pair_distance:
        min_distance = left_closest_pair_distance
        closest_p = (left_point1, left_point2)
    else:
        min_distance = right_closest_pair_distance
        closest_p = (right_point1, right_point2)

    # Check for points in the middle strip
    mid_x, mid_y = sorted_x[mid], sorted_y[mid]
    strip_indices = [i for i in range(n) if abs(x[i] - mid_x) < min_distance]
    strip_indices.sort(key=lambda i: y[i])

    for i in range(len(strip_indices)):
        for j in range(i + 1, min(i + 8, len(strip_indices))):
            idx1, idx2 = strip_indices[i], strip_indices[j]
            distance = euclidean_distance(x[idx1], y[idx1], x[idx2], y[idx2])
            if distance < min_distance:
                min_distance = distance
                closest_p = ((x[idx1], y[idx1]), (x[idx2], y[idx2]))

    return min_distance, closest_p[0], closest_p[1]


N = 30
x = np.random.rand(N)*10
y = np.random.rand(N)*10

min_dist, closest_p1, closest_p2 = closest_pair(x,y)
print('Khoảng cách ngắn nhất: ',min_dist)
plt.plot(x,y,'go')
x_closest = [closest_p1[0],closest_p2[0]]
y_closest = [closest_p1[1],closest_p2[1]]
plt.plot(x_closest,y_closest,'ro-')
plt.show()