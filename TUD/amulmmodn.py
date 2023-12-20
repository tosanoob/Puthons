print("Tinh a mu m mod n")
# a,m,n = map(int, input("Nhap lan luot a,m,n: ").split())
a = 100009
m = 98765
n = 10008
counter = 0
res = 1
while (counter<m):
    counter+=1
    res=res*a%n

print(res)