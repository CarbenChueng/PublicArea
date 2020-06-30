import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,explained_variance_score


# #使用sklearn创建线性回归数据
# from sklearn.datasets.samples_generator import make_regression
#                 #个数           特征值       方差（偏移量）斜率
# x,y,cofe = make_regression(n_samples=100,n_features=1,noise=30,coef=True)#如果斜率为True，会返回三样东西：x,y,斜率
# plt.scatter(x,y)
# plt.plot(x,x*cofe,color="pink",linewidth=6)
# plt.show()

#===============================================================================================
rng = np.random.RandomState(0)

x = 5*rng.rand(100,1)
y = np.sin(x).ravel()#降维

y[::5] += 3*(0.5-rng.rand(x.shape[0]//5))#噪音

kr = GridSearchCV(KernelRidge(),
                  param_guide = {"kernel":["rbf","laplacian","polynomial","sigmoid"],
                                "alpha":[1e0,0.1,1e-2,1e-3],
                                 "gamma":np.logspace(-2,2,5)})

kr.fit(x,y)
print(kr.best_score_,kr.best_params_)

x_plot = np.linspace(0,5,100)
y_kr = kr.predict(x_plot[:,None])

plt.scatter(x,y)
plt.plot(x_plot,y_kr,color="red")
plt.show()








