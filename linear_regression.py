import numpy as np
import matplotlib.pyplot as plt

from matplotlib import font_manager
# macOS系统中文字体设置
plt.rcParams['font.family'] = ['Arial Unicode MS']  # macOS自带Unicode字体
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号



#生成样本,f_x=5x1+7x2+9
def generate_samples(num_samples):
    x1 = 3 * np.random.randn(num_samples) + 10
    x2 = 6 *np.random.randn(num_samples) + 2
    noise = np.random.randn(num_samples) 
    x = np.column_stack((x1, x2))
    y = 5 * x1 + 7 * x2 + 9 + noise  #这个模型要跟predict函数中的模型一致
    return x,y
#预测
def predict(X,W,b):
    return np.matmul(X, W) + b
#误差
def error(X,Y,W,b):
    return Y - predict(X,W,b)
#损失函数
def loss(X,Y,W,b):
    return np.mean(error(X,Y,W,b)**2)
#成本函数（添加正则化）
def cost_function(X,Y,W,b,reg_type='l2',lambda_=0.01):
    cost = 1/2 * loss(X,Y,W,b)
    if reg_type == 'l2':
        # L2正则化 (Ridge)
        cost += lambda_ * np.sum(W**2) / 2
    elif reg_type == 'l1':
        # L1正则化 (Lasso)
        cost += lambda_ * np.sum(np.abs(W))
    return cost
#梯度（添加正则化）
def gradient(X,Y,W,b,reg_type='l2',lambda_=0.01):
    n = len(Y)
    err = error(X,Y,W,b)
    dW = -2/n * np.matmul(X.T, err)
    
    # 添加正则化项的梯度
    if reg_type == 'l2':
        # L2正则化的梯度
        dW += lambda_ * W
    elif reg_type == 'l1':
        # L1正则化的梯度
        dW += lambda_ * np.sign(W)
        
    db = -2/n * np.sum(err)
    return dW, db
#更新参数
def update_parameters(X,Y,W,b,learning_rate,reg_type='l2',lambda_=0.01):
    dW,db = gradient(X,Y,W,b,reg_type,lambda_)
    W = W - learning_rate * dW
    b = b - learning_rate * db
    return W,b
#训练（添加正则化参数）
def train(X,Y,W,b,learning_rate,num_iterations,reg_type='l2',lambda_=0.01):
    W_history = []
    b_history = []
    cost_history = []
    for i in range(num_iterations):
        W,b = update_parameters(X,Y,W,b,learning_rate,reg_type,lambda_)
        W_history.append(W)
        b_history.append(b)
        cost_history.append(cost_function(X,Y,W,b,reg_type,lambda_))
        print(f"Iteration {i+1}/{num_iterations}, Cost: {cost_history[-1]},W:{W},b:{b}")
    return W,b,cost_history,W_history,b_history

def normalize(X):
    mean = np.mean(X, axis=0)
    std = np.std(X, axis=0)
    return (X - mean) / std, mean, std

def denormalize_parameters(W, b, mean_X, std_X, mean_Y, std_Y):
    """
    将归一化后训练得到的参数还原回原始尺度
    
    参数:
    W - 归一化特征训练的权重
    b - 归一化特征训练的偏置
    mean_X - 特征均值
    std_X - 特征标准差
    mean_Y - 标签均值
    std_Y - 标签标准差
    
    返回:
    W_original - 原始尺度的权重
    b_original - 原始尺度的偏置
    """
    # 还原权重
    W_original = W * std_Y / std_X
    
    # 还原偏置
    b_original = b * std_Y + mean_Y - np.sum(W_original * mean_X)
    
    return W_original, b_original

def main():
    X,Y = generate_samples(100)
    X_norm, mean_X, std_X = normalize(X)
    Y_norm, mean_Y, std_Y = normalize(Y)
    W = np.zeros(2)
    b = 0
    learning_rate = 0.01 #学习率
    num_iterations = 500 #迭代次数
    
    # 增加正则化参数
    reg_type = 'l2'  # 可选 'l1' 或 'l2'
    lambda_ = 0.01   # 正则化强度
    
    W,b,cost_history,W_history,b_history = train(X_norm,Y_norm,W,b,learning_rate,num_iterations,reg_type,lambda_)
    
    # 还原参数到原始尺度
    W_original, b_original = denormalize_parameters(W, b, mean_X, std_X, mean_Y, std_Y)
    print(f"原始尺度参数 - W: {W_original}, b: {b_original}")
    
    # 验证还原后的参数
    y_pred_norm = predict(X_norm, W, b)
    y_pred_original = predict(X, W_original, b_original)
    mse_norm = np.mean((Y_norm - y_pred_norm)**2)
    mse_original = np.mean((Y - y_pred_original)**2)
    print(f"归一化数据MSE: {mse_norm}")
    print(f"原始数据MSE: {mse_original}")

    # 可视化
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(range(num_iterations), cost_history)
    plt.title('损失函数历史')
    plt.xlabel('迭代次数')
    plt.ylabel('损失')
    
    ax = plt.subplot(1, 2, 2, projection='3d')
    # 创建网格点
    x1_grid = np.linspace(min(X[:,0]), max(X[:,0]), 20)
    x2_grid = np.linspace(min(X[:,1]), max(X[:,1]), 20)
    X1, X2 = np.meshgrid(x1_grid, x2_grid)
    # 计算预测平面
    X_grid = np.column_stack((X1.ravel(), X2.ravel()))
    Y_pred = predict(X_grid, W_original, b_original)
    Y_pred = Y_pred.reshape(X1.shape)
    
    # 绘制预测平面
    ax.plot_surface(X1, X2, Y_pred, alpha=0.3, cmap='viridis')
    # 绘制实际数据点
    ax.scatter(X[:,0], X[:,1], Y, c='r', marker='o', alpha=0.5, label='实际值')
    
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Y')
    ax.legend()
    ax.set_title('3D预测结果')
    plt.show()

if __name__ == "__main__":

    main()

