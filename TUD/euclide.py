a,b = map(int, input().split())

print("Tim uoc chung lon nhat bang thuat toan euclide")
print(a,b)

if a>b:
    temp=a
    a=b
    b=temp

while a!=b and a!=0 and b!=0:
    a = a%b
    temp=a
    a=b
    b=temp

print(a)