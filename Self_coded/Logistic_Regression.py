import pandas as pd
import numpy as np

#đọc file trả về tập dữ liệu
def read_file(file, ):
    with open(file) as inp:
        reader = pd.read_csv(inp).values
        return reader

#chỉnh sửa thành giá trị số, trả về tập X, y (np array)
def modify_data(data, y_available = True):
    if y_available:
        for item in data:
            if item[4] == 'Iris-versicolor':
                item[4] = 1
            else: item[4] = 0
        return np.array(data[:,0:4]), np.array(data[:,4])
    else:
        return np.array(data[:,0:data.shape[1]-1])

#hàm logistic
def sigmoid(x):
    return 1/(1 + np.exp(-x))

#logistic regression Gradient Descent
def logistic_sigmoid_regression_GD(X, y, w_init, alpha, tol = 1e-4, loop = 20000):
    w = [w_init]
    #khởi tạo w

    #X là numpy_array (N,d) N: số mẫu dữ liệu, d: số chiều
    d = X.shape[1]
    N = X.shape[0]

    #count => đếm số lần lặp
    #check_w => kiểm tra kết quả sau cứ mỗi 100 lần lặp
    count = 0
    check_w=100
    while count < loop:
        #note: sum -> average -> w_new
        sum = 0
        for i in range(0, N):
            xi = X[i]
            yi = y[i]
            zi = sigmoid(np.dot(w[-1].T, xi))
            sum += 1/80*(yi - zi)*xi
        w_new = w[-1] + alpha * sum
        #alpha là hệ số học máy
        w.append(w_new)
        count += 1
        #cứ check_w lần thực hiện kiểm tra một lần, thoả thì return kq
        if (count%check_w == 0):
            if np.linalg.norm(w_new - w[-check_w]) < tol:
                return w
    return w

#logistic regression Stochastic Gradient Descent
def logistic_sigmoid_regression_SGD(X, y, w_init, alpha, tol = 1e-4, loop = 10000):
    w = [w_init]
    d = X.shape[0]
    count = 0
    check_w = 100
    while count < loop:
        # mix data
        mix_id = np.random.permutation(d)
        #note: mix data -> calculate directly w_new
        for i in mix_id:
            xi = X[i]
            yi = y[i]
            zi = sigmoid(np.dot(w[-1].T, xi))
            w_new = w[-1] + alpha*(yi - zi)*xi
            count += 1
            # stopping criteria
            if count%check_w == 0:
                if np.linalg.norm(w_new - w[-check_w]) < tol:
                    return w
            w.append(w_new)
    return w

#khởi tạo tĩnh vector w_init size dim
def static_w_init(dim):
    w_init = []
    for i in range (0,dim):
        w_init.append(1)
    return w_init

if __name__ == "__main__":
    X , y = modify_data(read_file('input.csv'))
    #đọc input.csv lưu vào X, y
    w_init = []
    for dim in range (0,X.shape[1]):
        sum = 0
        for rec in range (0,X.shape[0]):
            sum += X[rec,dim]
        #gán giá trị trung bình của các dim cho w_init
        w_init.append(sum/(X.shape[0]))

    w_init = np.array(w_init) #tạo np array từ mảng w_init
    w_result = logistic_sigmoid_regression_GD(X,y,w_init,0.001)
    print(w_result[-1])

    X_test = modify_data(read_file('output_01.csv'))[0]
    df_result = pd.DataFrame(columns=['sepal_length','sepal_width','petal_length','petal_width','Labeling'])

    for i in range (0,X_test.shape[0]):
        #versicolor = 1, setosa = 0
        label_1 , label_2 = 'Iris-setosa' , 'Iris-versicolor'
        if (np.dot(w_result[-1].T,X_test[i])>0.5):
            print(label_2)
            new_row = pd.DataFrame({'sepal_length':X_test[i,0],
                       'sepal_width':X_test[i,1],
                       'petal_length':X_test[i,2],
                       'petal_width':X_test[i,3],
                       'Labeling':label_2
                       }, index=[0])
        else:
            print(label_1) 
            new_row = pd.DataFrame({'sepal_length':X_test[i,0],
                       'sepal_width':X_test[i,1],
                       'petal_length':X_test[i,2],
                       'petal_width':X_test[i,3],
                       'Labeling':label_1
                       }, index=[0])
        df_result = df_result._append(new_row, ignore_index=True)
    
    df_result.to_csv('output.csv',index=False)