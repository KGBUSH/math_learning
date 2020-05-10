# -*- coding: utf-8 -*-
"""
https://www.freesion.com/article/452412206/
"""
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
np.random.seed(0)

X = np.linspace(-5, 5, num=20)

# 第一种调用方式
gauss = norm(loc=1, scale=2)  # loc: mean 均值， scale: standard deviation 标准差
r_1 = gauss.pdf(X)

# 第二种调用方式
r_2 = norm.pdf(X, loc=0, scale=2)  # r_2 shape和X一致

# 第三种方案
r_3 = norm.rvs(loc=0, scale=0.1, size=X.shape[0])

for i in range(len(X)):
    ax.scatter(X[i], 0, s=100)
for g, c in zip([r_1, r_2, r_3], ['r', 'g', 'b']):  # 'r': red, 'g':green
    ax.plot(X, g, c=c)

plt.show()
