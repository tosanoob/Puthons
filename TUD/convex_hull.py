import numpy as np
import matplotlib.pyplot as plt

def det(a,b,c):
    # tính det của ma trận sau
    # 1 ax ay
    # 1 bx by
    # 1 cx cy
    d = [[1,1,1]]
    d.append([a[0],b[0],c[0]])
    d.append([a[1],b[1],c[1]])
    d = np.array(d)
    return np.linalg.det(d)

def is_right(a,b,c):
    return (det(a,b,c)<=0) # True => phải, False: trái
    
def convex_hull(p): #input: một tập điểm 
    N = p.shape[0]
    p = p[p[:,0].argsort()] # sắp xếp tập điểm theo chiều tăng dần x
    
    # chia thành tập upper và lower
    leftmost = p[0]
    rightmost = p[-1]
    upper = [leftmost]
    lower = [leftmost]
    for i in range(1,N-1):
        # thay vì kẻ đường thẳng, ta kiểm tra một điểm p
        # nếu nằm bên trái đường leftmost-rightmost thì nó là upper
        # ngược lại nó là lower
        if not is_right(leftmost,rightmost,p[i]):
            upper.append(p[i])
        else:
            lower.append(p[i])
    upper.append(rightmost)
    lower.append(rightmost)

    Lupper = [] # khởi tạo Lupper, gán upper[0] = leftmost và upper[1]
    Lupper.append(upper[0])
    Lupper.append(upper[1])
    for i in range(2,len(upper)):
        if is_right(Lupper[-2],Lupper[-1],upper[i]): 
            Lupper.append(upper[i]) # nếu upper[i] nằm bên phải thì thêm vào Lupper
        else:
            # kiểm tra ngược bao Lupper
            if len(Lupper)>=1:
                Lupper.pop() # Xoá Lupper bên phải nhất
                while len(Lupper)>=2 and (not is_right(Lupper[-2],Lupper[-1],upper[i])):
                    Lupper.pop() # Tiếp tục xoá nếu không thoả điều kiện
                Lupper.append(upper[i]) # Gắn upper[i] vào Lupper sau khi xoá ngược
    
    Llower = [] # Tương tự Lupper
    Llower.append(lower[0])
    Llower.append(lower[1])
    for i in range(2,len(lower)):
        if not is_right(Llower[-2],Llower[-1],lower[i]): 
            Llower.append(lower[i]) # nếu lower[i] nằm bên trái thì thêm vào Llower
        else:
            # kiểm tra ngược bao Llower
            if len(Llower)>=1:
                Llower.pop() # Xoá Llower bên phải nhất
                while len(Llower)>=2 and (is_right(Llower[-2],Llower[-1],lower[i])):
                    Llower.pop() # Tiếp tục xoá nếu không thoả điều kiện
                Llower.append(lower[i]) # Gắn lower[i] vào Llower sau khi xoá ngược
                
    return np.array(Lupper), np.array(Llower) # Trả về Lupper và Llower

N = 20 # số điểm cần tính bao
x = np.random.rand(N)*10
y = np.random.rand(N)*10


# x = np.array([1,2,3,5,7,8,9]) 
# y = np.array([7,6,2,8,5,1,8])
p = np.array([x,y])
p = np.transpose(p)

Lupper, Llower = convex_hull(p)

# xuất kết quả ở dạng đồ thị
p = np.transpose(p)
Lupper = np.transpose(Lupper)
Llower = np.transpose(Llower)
plt.plot(p[0],p[1],'go')
plt.plot(Lupper[0],Lupper[1],'ro-')
plt.plot(Llower[0],Llower[1],'ro-')
plt.show()


