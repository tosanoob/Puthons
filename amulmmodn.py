print("Tinh a mu m mod n")
a,m,n = map(int, input("Nhap lan luot a,m,n: ").split())
counter = 0
res = 1
while (counter<m):
    counter+=1
    res=res*a%n

print(res)