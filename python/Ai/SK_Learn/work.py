import numpy as np
import sklearn
import torch
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from  sklearn.cluster import KMeans
from sklearn import linear_model,neighbors
from sklearn.kernel_ridge import KernelRidge
from sklearn import metrics,model_selection
from sklearn import neighbors, datasets, preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score


#========================================汽车============================================
dat = np.loadtxt("car.tag",dtype=str,delimiter=',')
# print(dat)

CarData = np.array(dat)
# print(CarData)
print(CarData.shape)
y = CarData[:,2]
x1 = CarData[:,:2]
x2 = CarData[:,3:]
x = np.hstack([x1,x2])
# print(x)
# print(y)

x_train,x_test,y_train,y_test = model_selection.train_test_split(x,y,test_size=0.3)
# model = linear_model.LinearRegression()
# model = linear_model.Ridge(0.5)
# model = linear_model.Lasso(0.5)
# model = linear_model.ElasticNet(0.6,0.5)
# model = linear_model.LogisticRegression()
model = linear_model.BayesianRidge()
#
model.fit(x_train,y_train)
#
# yuce = model.predict(x_test)
# print(metrics.r2_score(y_test,yuce))




#========================================房价============================================
# dat = np.loadtxt("housing.tag",dtype=np.float)
# # print(dat.shape)
# housesData = np.array(dat)
# # print(housesData)
# # print(housesData.shape)
# y = housesData[:,-1]
# x = housesData[:,:-1]
# # print(x)
# # print(y)
#
# x_train,x_test,y_train,y_test = model_selection.train_test_split(x,y,test_size=0.3)
# # model = linear_model.LinearRegression()
# # model = linear_model.Ridge(0.5)
# # model = linear_model.Lasso(0.5)
# # model = linear_model.ElasticNet(0.6,0.5)
# # model = linear_model.LogisticRegression()
# model = linear_model.BayesianRidge()
#
# model.fit(x_train,y_train)
#
# yuce = model.predict(x_test)
# print(metrics.r2_score(y_test,yuce))


#========================================红酒============================================


# dat = np.loadtxt("wine.tag",dtype=np.float,delimiter=',')
#
# # wineData = np.array(dat)
# y = dat[:,0]
# x = dat[:,1:]
# # print(x)
# # print(y)
#
# x_train,x_test,y_train,y_test = model_selection.train_test_split(x,y,test_size=0.3)
#
# scaler = preprocessing.StandardScaler().fit(x_train)
# x_train = scaler.transform(x_train)
# x_test = scaler.transform(x_test)
#
# knn = neighbors.KNeighborsClassifier(n_neighbors=5)
#
# knn.fit(x_train,y_train)
#
# scores = cross_val_score(knn,x_train,y_train,cv=5,scoring = "accuracy")
# # print(scores)
# # print(scores.mean())
#
# yuce = knn.predict(x_test)
# print(accuracy_score(yuce,y_test))

#========================================3D分类============================================

#生成数据
# tag = np.random.rand(100,3)
#
# #构建模型
# model = KMeans(n_clusters=3)#分类的个数
#
# #训练
# train = model.fit_predict(tag)
# print(train)
#
# #获取聚类中心
# center = model.cluster_centers_
# print(center)
#
#
# #获取类别标签
# lablele = model.labels_
# print(lablele)
# print(center)

#创建画板
# fit = plt.figure()
# ax = Axes3D(fit)
# ax.scatter(tag[:,0],tag[:,1],tag[:,2],c=train,marker="^",s=80)
# ax.scatter(center[:,0],center[:,1],center[:,2],c=center[0],marker="*",s=30)
# plt.show()

#========================================one hot============================================

# numClasses = 10
# arr=[2,3,6,1]
# #eye是矩阵，（）填一个数是行列数相等，（2，3）两行三列
# one_hots = np.eye(numClasses)[arr]
# # print(one_hot)
# # print(np.argmax(one_hots))#取最大索引值
# tag = [np.argmax(one_hot) for one_hot in one_hots]
# print(tag)


#========================================one hot============================================

# numClass = 10
# t = torch.tensor([1,2,3,4,5,6])
# # print(t.size())
# # print(t)
# c= torch.zeros(t.size(0),numClass).scatter_(1,t.reshape(-1,1),1)
# print(c)
# print(c.shape)