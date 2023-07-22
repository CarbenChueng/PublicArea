from sklearn import neighbors,datasets,preprocessing
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score

#引入数据
iris = datasets.load_iris()
x = iris.data
y = iris.target
#设置k值为1到30，通过绘图来查看训练的分数
k_range = range(1,31)
k_scoker = []
for k in k_range:
    knn = neighbors.KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn,x,y,cv=5,scoring="accuracy")
    k_scoker.append(scores.mean())
plt.figure()
plt.plot(k_range,k_scoker)
plt.show()