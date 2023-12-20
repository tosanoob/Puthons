# ax + by = c, a,b,c la so nguyen

import math as m

def extended_gcd (a,b):
    if (b==0):
        return (1,0)
    (q,r) = (a//b,a%b)
    (s,t) = extended_gcd(b,r)
    return (t, s - q*t)

a = int(input())
b = int(input())
c = int(input())

d = m.gcd(a,b)

if c%d==0:
    (k,l) = extended_gcd(a,b)
    x,y = c/d*k,c/d*l
    print(int(x))
    print(int(y))
else:
    print("phuong trinh vo nghiem nguyen")


