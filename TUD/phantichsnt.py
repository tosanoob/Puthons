import numpy as np

def is_prime(x):
    if (x<=2): 
        return True
    k = int(np.sqrt(x))
    for i in range(3, k, 2):
        if x%i == 0:
            return False
    return True

# n = int(input())
n = 1024*3*6*7
k = 2
p = []
a = []
# phân tích n = p1^a1 * p2^a2 * ... * pn^an
while (n>1):
    if (n%k==0):
        p.append(k)
        a.append(0)
        while (n%k==0):
            a[-1]+=1
            n/=k
    k=k+1

print(p)
print(a)