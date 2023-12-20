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


def mini_batch_gradient_descent():
    epoch_max = 50
    minibatch_size = 20
    learning_rate = 0.01
    momentum = 0.5
    learning_speed = 0
    # get random theta
    thetas = np.random.randn(dimension, 1)
    thetas_path = [thetas]
    losses = []
    relative_error = []
    tolerance = 1e-3
    for epoch in range(epoch_max):
        # shuffle data
        shuffled_indices = np.random.permutation(N)
        X_b_shuffled = X_b[shuffled_indices]
        y_shuffled = y[shuffled_indices]
        for i in range(0, N, minibatch_size):
            xi = X_b_shuffled[i:i + minibatch_size]
            yi = y_shuffled[i:i + minibatch_size]

            # predict y_hat
            y_hat = xi.dot(thetas + learning_speed*momentum)

            # compute loss
            loss = (y_hat - yi) ** 2

            # compute gradient for loss
            d_loss = 2 * (y_hat - yi) / minibatch_size

            # compute gradient for param
            gradients = xi.T.dot(d_loss)

            # update
            learning_speed = momentum*learning_speed + learning_rate*gradients #add momentum
            thetas = thetas - learning_speed
            thetas_path.append(thetas)

            loss_mean = np.sum(loss) / minibatch_size
            losses.append(loss_mean)

            # check convergence
            relative_error.append(np.linalg.norm(thetas_path[-1] - thetas_path[-2])/np.linalg.norm(thetas_path[-1]))
            if relative_error[-1] < tolerance:
                return thetas_path, losses, relative_error
    return thetas_path, losses, relative_error

mbgd_thetas, losses, rel_error = mini_batch_gradient_descent()

# in loss cho 100 sample đầu
# x_axis = list(range(200))
plt.subplot(2,1,1)
plt.plot(losses, color="r")
plt.title("Loss graph")
plt.subplot(2,1,2)
plt.plot(rel_error, color="g")
plt.title("Relative error graph")
plt.show()