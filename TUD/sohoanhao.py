import numpy as np

def is_perfect(x):
    sum = 0
    for i in range(1,x):
        if (x%i==0):
            sum+=i
    if sum==x:
        return True
    else:
        return False
    
a = 1
b = 1000
for i in range(a,b+1):
    if is_perfect(i):
        print(i)