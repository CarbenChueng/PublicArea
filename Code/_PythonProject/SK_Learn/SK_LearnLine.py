#                   k近邻模型包，数据集   数据预处理（标准版或者归一化）
from sklearn import tree,neighbors, datasets, preprocessing
#                                   数据切分
from sklearn.model_selection import train_test_split
#                                   交叉验证
from sklearn.model_selection import cross_val_score
#                           评估
from sklearn.metrics import accuracy_score

import numpy as np


import matplotlib.pyplot as plt

# =======================简单调参==========================
# 引入数据
# iris = datasets.load_iris()
# x = iris.tag
# y = iris.target
# # 设置k值 1-30，通过绘图查看训练分数
# k_range = range(1, 31)
# k_socker = []
# for k in k_range:
#     knn = neighbors.KNeighborsClassifier(n_neighbors=k)
#     scores = cross_val_score(knn, x, y, cv=5, scoring="accuracy")
#     k_socker.append(scores.mean())
#
# plt.figure()
# plt.plot(k_range, k_socker)
# plt.show()
#
#
# # =======================机器学习（拟合问题，点线关系）==========================
# # 加载数据
# iris = datasets.load_iris()#有标签数据
#
# #划分训练集与测试集
# x,y = iris.tag,iris.target
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)
# #
# # #数据预处理（不是必须的，但是处理更快）
# scaler = preprocessing.StandardScaler().fit(x_train)
# x_train = scaler.transform(x_train)
# x_test = scaler.transform(x_test)
# #
# # #创建模型
# knn = neighbors.KNeighborsClassifier(n_neighbors=6)
# # #模型拟合
# knn.fit(x_train,y_train)
# #
# # #交叉验证                  模型   数据       验证数量    计算方法
# scroes = cross_val_score(knn,x_train,y_train,cv=5,scoring="accuracy")
# # print(scroes)
# print(scroes.mean())
# #
# # #预测
# y_pred = knn.predict(x_test)
# # #评估
# print(accuracy_score(y_test,y_pred))


# =======================机器学习（回归问题，点和点关系）==========================


# =======================决策树==========================
np.random.RandomState(0)

iris = datasets.load_iris()
wine = datasets.load_boston()
#显示值的属性
print(wine.feature_names)
#显示值
print(wine.data)

x,y = iris.data,iris.target
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)


