import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
# get data
data = genfromtxt('advertising.csv', delimiter=',', skip_header=1)

X = data[:, 0:3]

y = data[:, 3:4]
N = data.shape[0]
dimension = data.shape[1]

# normalize data
maxi = np.max(X)
mini = np.min(X)
avg = np.mean(X)
X = (X-avg) / (maxi-mini)

# get X bar [1,X]
X_b = np.c_[np.ones((N, 1)), X]

def batch_gradient_descent():
    epochs_max = 100
    learning_rate = 0.01
    momentum = 0.5
    learning_speed = 0
    tolerance = 1e-3
    relative_error = []

    # init theta
    thetas = np.random.randn(dimension, 1)
    thetas_path = [thetas]
    losses = []

    for i in range(epochs_max):
        # predict y_hat
        y_hat = X_b.dot(thetas)

        # compute loss
        loss = (y_hat - y) ** 2

        # compute gradient for loss
        d_loss = 2 * (y_hat - y) / N

        # compute gradient for params
        gradients = X_b.T.dot(d_loss)

        # update
        learning_speed = momentum*learning_speed + learning_rate*gradients #add momentum
        thetas = thetas - learning_speed
        thetas_path.append(thetas)

        mean_loss = np.sum(loss) / N
        losses.append(mean_loss)

        # check convergence
        relative_error.append(np.linalg.norm(thetas_path[-1] - thetas_path[-2])/np.linalg.norm(thetas_path[-1]))
        if relative_error[-1] < tolerance:
            return thetas_path, losses, relative_error

    return thetas_path, losses, relative_error

bgd_thetas, losses, rel_error = batch_gradient_descent()

print(bgd_thetas[-1])

# in loss cho 100 sample đầu
# x_axis = list(range(100))
plt.subplot(2,1,1)
plt.plot(losses, color="r")
plt.title("Loss graph")
plt.subplot(2,1,2)
plt.plot(rel_error, color="g")
plt.title("Relative error graph")
plt.show()