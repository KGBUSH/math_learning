# -*- coding: utf-8 -*-
"""
参考https://www.cnblogs.com/pinard/p/6638955.html

在例子里，我们的目标平稳分布: 是一个均值3，标准差2的正态分布，
而选择的马尔可夫链状态转移矩阵𝑄(𝑖,𝑗)的条件转移概率: 是以𝑖为均值,方差1的正态分布在位置𝑗的值。
这个例子仅仅用来让大家加深对M-H采样过程的理解。
毕竟一个普通的一维正态分布用不着去用M-H采样来获得样本。
"""
import random
import math
from scipy.stats import norm, uniform
import matplotlib.pyplot as plt


# %matplotlib inline

def norm_dist_prob(theta):
    y = norm.pdf(theta, loc=3, scale=2)  # loc: mean 均值， scale: standard deviation 标准差
    return y


if __name__ == '__main__':
    T = 5000
    pi = [0 for i in range(T)]  # 随机变量那条马尔科夫链，一开始全是0只是初始化而已
    sigma = 4
    t = 0
    while t < T - 1:
        t = t + 1
        pi_star = norm.rvs(loc=pi[t - 1], scale=sigma, size=1, random_state=None)
        # pi_star = uniform.rvs(loc=pi[t - 1], scale=sigma, size=1, random_state=None)

        # 很多时候，我们选择的马尔科夫链状态转移矩阵𝑄如果是对称的, 即满足𝑄(𝑖,𝑗)=𝑄(𝑗,𝑖),这时我们的接受率可以进一步简化为：
        # 𝛼(𝑖,𝑗)= 𝑚𝑖𝑛{𝜋(𝑗)/𝜋(𝑖), 1}
        # pi_star就是状态𝜋(𝑗); pi[t - 1]是状态𝜋(𝑖)
        alpha = min(1, (norm_dist_prob(pi_star[0]) / norm_dist_prob(pi[t - 1])))

        u = random.uniform(0, 1)
        if u < alpha:
            pi[t] = pi_star[0]
        else:
            pi[t] = pi[t - 1]

    plt.scatter(pi, norm.pdf(pi, loc=3, scale=2))
    num_bins = 50
    plt.hist(pi, num_bins, normed=1, facecolor='red', alpha=0.7)
    plt.show()
