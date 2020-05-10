# -*- coding: utf-8 -*-

import numpy as np
from scipy.stats import norm, uniform
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
np.random.seed(0)



#
# X = np.linspace(-5, 5, num=20)
#
# # 第一种调用方式
# gauss = norm(loc=1, scale=2)  # loc: mean 均值， scale: standard deviation 标准差
# r_1 = gauss.pdf(X)
#
# # 第二种调用方式
# r_2 = norm.pdf(X, loc=0, scale=3)
#
# for i in range(len(X)):
#     ax.scatter(X[i], 0, s=100)
# for g, c in zip([r_1, r_2], ['r', 'g']):  # 'r': red, 'g':green
#     ax.plot(X, g, c=c)
#
# plt.show()





# 第三种方案
# X = np.linspace(-5, 5, num=1000)
r_3 = norm.rvs(loc=3, scale=1, size=1000)
r_4 = uniform.rvs(loc=0, scale=13, size=1000)
plt.hist(r_3, 30)
plt.hist(r_4, 30, facecolor='red', alpha=0.7)

# ax.plot(X, r_3, c='b')
plt.show()

