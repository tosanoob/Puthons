import numpy as np

def f(x):
    return 0.5*(x-1)**2 - 2
def ff(x):
    return x-1
def GradientDescent(x_0, alpha = 1, loop = 1000, tol = 1e-3):
    x = [x_0]
    while loop > 0:
        new_x = x[-1] - alpha*ff(x[-1])
        x.append(new_x)
        if np.abs(x[-1] - x[-2]) < tol:
            return x
    return x

x_steps = GradientDescent(-1000)
print(x_steps)