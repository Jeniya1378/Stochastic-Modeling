# -*- coding: utf-8 -*-
"""
MTH 653 Stochastic Modeling
Computer Simulation (for Graduate Students): Please generate a Possion process with rate 1, and plot a graph.
You can use any computer language (R, matlab, Python, ... ), but do not use the built-in function, if any.

Jeniya Sultana
"""
import math
import numpy as np
import matplotlib.pyplot as plt


def poisson(lmbda, x):
    return math.exp(-lmbda)*pow(lmbda,x)/math.factorial(x)


lmbda=1
 
# creating a numpy array for x-axis
# using step size as 1
X = np.arange(1, 20, 1)

#instead of using defined range of values, also can use random integers.
# X = np.random.randint(1, 100, 100)
 
Y=np.array([poisson(lmbda, x) for x in X])
 
# plotting the graph
plt.plot(X, Y,'bo',markersize=2)
plt.vlines(X, 0, Y, colors='b', lw=5, alpha=0.5)
 
# showing the graph
plt.show()