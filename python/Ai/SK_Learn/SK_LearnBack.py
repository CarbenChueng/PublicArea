import matplotlib.pyplot as plt
from sklearn import linear_model,svm,neighbors,datasets,preprocessing
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,f1_score
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,explained_variance_score


# #使用sklearn创建线性回归数据
# from sklearn.datasets.samples_generator import make_regression
#                 #个数           特征值       方差（偏移量）斜率
# x,y,cofe = make_regression(n_samples=100,n_features=1,noise=30,coef=True)#如果斜率为True，会返回三样东西：x,y,斜率
# plt.scatter(x,y)
# plt.plot(x,x*cofe,color="pink",linewidth=6)
# plt.show()

#===============================================================================================
# rng = np.random.RandomState(0)
#
# x = 5*rng.rand(100,1)
# y = np.sin(x).ravel()#降维
#
# y[::5] += 3*(0.5-rng.rand(x.shape[0]//5))#噪音
#
# kr = GridSearchCV(KernelRidge(),
#                   param_guide = {"kernel":["rbf","laplacian","polynomial","sigmoid"],
#                                 "alpha":[1e0,0.1,1e-2,1e-3],
#                                  "gamma":np.logspace(-2,2,5)})
#
# kr.fit(x,y)
# print(kr.best_score_,kr.best_params_)
#
# x_plot = np.linspace(0,5,100)
# y_kr = kr.predict(x_plot[:,None])
#
# plt.scatter(x,y)
# plt.plot(x_plot,y_kr,color="red")
# plt.show()


#===============================================================================================
#屏蔽警告
# import warnings
# warnings.filterwarnings("ignore")

# np.random.RandomState(0)
#
# iris = datasets.load_iris()
# x,y = iris.tag,iris.target
#
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)
# scaler = preprocessing.StandardScaler().fit(x_train)
# x_train = scaler.transform(x_train)
# x_test = scaler.transform(x_test)
#
# clf = svm.SVC()
#
# clf.fit(x_train,y_train)
# #预测
# yPred = clf.predict(x_test)
# # print(x_test.shape)
# # print(yPred.shape)
# #评估
# print(accuracy_score(y_test,yPred))#准确度
# print(y_test)
# print(yPred)
# # f1得分
# print(f1_score(y_test,yPred,average="micro"))
# 分类报告
# print(classification_report(y_test,yPred))
# 混淆矩阵
# print(confusion_matrix(y_test,yPred))


#===============================================================================================
x = np.array([[1.,-1.,2.],[2.,0.,0.],[0.,1.,-3.]])

# 标准化（例子）
# x_scale = preprocessing.scale(x)
# print(x_scale)
# print(x_scale.mean(axis=0),x_scale.std(0))#均值（列），标准差

# 标准化
#获取标准化对象
# scaler = preprocessing.StandardScaler()
# x_scaler = scaler.fit_transform(x)
# print(x_scaler)
# print(x_scaler.mean(0),x_scaler.std(0))

# minmax
# scaler = preprocessing.MinMaxScaler()
# x_scale = scaler.fit_transform(x)
# print(x_scale)
# print(x_scale.mean(0), x_scale.std(0))
# exit()

# MaxAbsScaler
# scaler = preprocessing.MaxAbsScaler()
# x_scale = scaler.fit_transform(x)
# print(x_scale)
# print(x_scale.mean(0), x_scale.std(0))

# RobustScaler
# scaler = preprocessing.RobustScaler()
# x_scale = scaler.fit_transform(x)
# print(x_scale)
# print(x_scale.mean(0), x_scale.std(0))
# exit()

# Normalizer
# scaler = preprocessing.Normalizer(norm="l2")
# x_scale = scaler.fit_transform(x)
# print(x_scale)
# print(x_scale.mean(0), x_scale.std(0))
# exit()
# 二值化
# scaler = preprocessing.Binarizer(threshold=0)
# x_scale = scaler.fit_transform(x)
# print(x_scale)
# exit()

# one_hot
# enc = preprocessing.OneHotEncoder(n_values=3, sparse=False)
# ans = enc.fit_transform([[0], [1], [2],[1]])
# print(ans)
# exit()

#缺失
imp = SimpleImputer(np.nan,"mean")
data = np.array([[np.nan,2],[6,np.nan],[7,6]])
y_imp = imp.fit_transform(data)
print(data)
print(y_imp)




