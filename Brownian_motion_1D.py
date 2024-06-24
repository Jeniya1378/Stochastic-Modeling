# -*- coding: utf-8 -*-
"""
MTH 653 Stochastic Modeling

Computer Simulation: Please simulation a standard Brownian Motion in 1D.

Jeniya Sultana
"""
import random
import matplotlib.pyplot as plt

# Parameters
T = 1      # Total time
N = 1000   # Number of time steps
dt = T/N   # Time step size

# Initial condition
x0 = 0

# Generate Brownian path
W = [x0]
for i in range(N):
    dW = random.gauss(0,1) * dt**0.5
    W.append(W[-1] + dW)

# Plot Brownian path
t = [i*dt for i in range(N+1)]
plt.plot(t, W)
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Standard Brownian Motion in 1D')
plt.show()
