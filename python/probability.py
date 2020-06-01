import numpy
a = numpy.array([[1,2],[3,4],[5,6]])
#偏向，喜好。分解成三个矩阵.svd提取特征
u,s,v = numpy.linalg.svd(a)
print(u,s,v,sep="\n")