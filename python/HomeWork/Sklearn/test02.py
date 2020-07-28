#使用SKlearn创建线性回归数据
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_regression
x,y,cofe = make_regression(n_samples=100,n_features=1,noise=10,coef=True)
print(cofe)
#画图
plt.scatter(x,y)
plt.plot(x,x*cofe,color="red",linewidth=2)
plt.show()
