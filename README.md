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

## 修改历史

- 实现基本的线性回归功能
- 添加数据归一化
- 添加参数还原功能
- 修复梯度计算问题
- 完善可视化 # 添加一行测试内容
