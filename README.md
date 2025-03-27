# 线性回归模型实现

## 项目简介

这个项目实现了一个完整的线性回归模型，包括基础的线性回归以及带有L1和L2正则化的变体（Lasso和Ridge回归）。该实现支持多特征输入，提供数据归一化处理，并包含详细的可视化功能，帮助理解模型训练过程和拟合结果。

## 功能特点

- 🔧 从零实现线性回归算法
- 📊 支持L1（Lasso）和L2（Ridge）正则化
- 🧮 自动数据归一化与反归一化
- 📈 训练过程可视化
- 🔍 3D数据拟合结果展示
- 🔄 完整的训练、验证流程

## 环境要求

- Python 3.6+
- NumPy
- Matplotlib

## 安装依赖

```bash
pip install numpy matplotlib
```
或者使用提供的requirements.txt：
```bash
pip install -r requirements.txt
```

## 使用方法

```bash
python linear_regression.py
```

## 算法原理

### 线性回归基础

线性回归模型假设目标变量y与特征向量x之间存在线性关系：

```
y = w₁x₁ + w₂x₂ + ... + wₙxₙ + b + ε
```

其中，w为权重向量，b为偏置项，ε为随机误差。

### 梯度下降优化

本实现使用梯度下降法最小化成本函数：
1. 计算当前参数下的预测误差
2. 计算成本函数对参数的梯度
3. 沿梯度反方向更新参数
4. 重复直到收敛或达到最大迭代次数

### 正则化技术

为了防止过拟合，实现了两种正则化方法：

#### L2正则化（Ridge回归）

通过添加权重平方和到损失函数中来惩罚较大的权重：

```
cost = MSE + λ∑w²/2
```

特点：
- 收缩所有权重
- 不会使权重变为精确零
- 适合处理多重共线性

#### L1正则化（Lasso回归）

通过添加权重绝对值和到损失函数中：

```
cost = MSE + λ∑|w|
```

特点：
- 产生稀疏解（某些权重会变为零）
- 具有特征选择功能
- 对异常值更加稳健

### 数据归一化

通过特征归一化加速训练过程并提高数值稳定性：
- 将特征缩放到均值为0，标准差为1
- 训练后通过反归一化还原参数到原始尺度

## 代码结构

- `generate_samples()`: 生成模拟数据
- `normalize()`: 数据归一化
- `denormalize_parameters()`: 参数反归一化
- `predict()`: 模型预测
- `error()`: 计算误差
- `loss()`: 计算损失函数
- `cost_function()`: 计算带正则化的成本函数
- `gradient()`: 计算梯度
- `update_parameters()`: 更新模型参数
- `train()`: 模型训练主函数
- `main()`: 程序入口，包含完整训练流程

## 参数调整

您可以在`main()`函数中调整以下参数：

```python
learning_rate = 0.01    # 学习率
num_iterations = 500    # 迭代次数
reg_type = 'l2'         # 正则化类型，可选 'l1' 或 'l2'
lambda_ = 0.01          # 正则化强度
```

## 可视化输出

程序将生成两个图形：
1. **损失函数历史**：展示训练过程中损失函数的变化
2. **3D预测结果**：展示特征、预测值和实际值的三维关系

## 示例结果解读

训练完成后，程序会输出以下信息：

- 原始尺度的权重和偏置
- 归一化和原始数据上的MSE（均方误差）

若模型训练成功，权重应接近真实值（本例中为w₁=5，w₂=7，b=9）。

## 修改历史

- 实现基本的线性回归功能
- 添加数据归一化
- 添加参数还原功能
- 修复梯度计算问题
- 完善可视化
- 添加L1和L2正则化功能
- 重构代码，提高可读性
- 扩展README文档

## 扩展方向

- 实现其他优化算法（如动量法、Adam等）
- 添加早停机制
- 实现交叉验证
- 扩展到多元线性回归

## 贡献与反馈

欢迎提交问题和改进建议！
