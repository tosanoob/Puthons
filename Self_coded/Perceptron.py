import numpy as np

def pred(w,x):
    #trả về dấu của phép nhân w.T * x
    return np.sign(np.dot(w.T,x))

def has_converged(X, y, w):
    return np.array_equal(pred(w,X),y)

#pocket algorithm:

def perceptron(X, y, w_init, loop = 1000):
    w = [w_init]
    #w_init là vector (1,d)
    d = X.shape[0]
    N = X.shape[1]
    #X nhập vào là d hàng, N cột (d,N)
    #d là số đặc trưng, N là số sample
    #y là vector 1,N => label của sample
    pocket = [] #lưu các mis_points của các optimal solution
    optimum = [] #lưu các optimal_solution
    min_mis = X.shape[1] #khởi tạo bằng N
    count = 0
    while True:
        mis_points = []
        #mix data:
        mix_id = np.random.permutation(N)
        for i in range (N):
            #lấy riêng cột i để tính
            xi = X[:,mix_id[i]].reshape(d,1)
            yi = y[:,mix_id[i]]
            if pred(w[-1],xi)[0] != yi:
                mis_points.append(mix_id[i]) #nếu label k match => missed
                #hàm cost
                w_new = w[-1] + yi*xi
                w.append(w_new)
        #sau khi hoàn tất lặp một vòng lại kiểm tra mis_points và optimum
        if (len(mis_points)<min_mis):
            min_mis = len(mis_points)
            pocket.append(mis_points)
            optimum.append(w[-1])        
        count+=1
        if has_converged(X,y,w[-1]) or count==loop:
            break
    return (optimum[-1], pocket[-1])

def generate_data(N = 10):
    means = [[-1,0], [1,0]]
    cov = [[.3,.2], [.2,.3]]
    X0 = np.random.multivariate_normal(means[0], cov, N).T
    X1 = np.random.multivariate_normal(means[1], cov, N).T
    #random ra 2 ma trận 2xN

    X = np.concatenate((X0,X1), axis=1)
    #axis = 1 => nối cộng cột => 2x2N
    #axis = 0 => nối cộng hàng => 4xN
    y = np.concatenate((np.ones((1,N)), -1*np.ones((1,N))), axis=1)
    #tạo ma trận 1xN toàn giá trị 1 và ma trận 1xN toàn giá trị -1, nối cộng cột => 1x2N gồm 1 và -1
    print(X)
    print(y)
    print("--------------")
    w_init = np.random.randn(X.shape[0],1)
    return (X, y, w_init)

if __name__ == "__main__":
    (X,y,w_init) = generate_data(10)
    (w, mis) = perceptron(X, y, w_init)
    print(w.T)
    
    s = 'missed: '
    for i in mis:
        s+=str(i)+' '
    print(s)


