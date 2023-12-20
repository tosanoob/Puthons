a,b = map(int, input().split())

print("Tim uoc chung lon nhat bang thuat toan euclide")
print(a,b)

if a>b:
    (a,b) = (b,a)

while a!=b and a!=0 and b!=0:
    a = a%b
    (a,b) = (b,a)

print(a)