# -*- coding: utf-8 -*-
"""
MTH 653 Stochastic Modeling

Computer Simulation: Please generate a pure birth process, the rate at each step is 1 more than the current population size.
Please generate a pure death process, starting with 50, and the rate at each step is 1.

Jeniya Sultana
"""

import numpy as np
import matplotlib.pyplot as plt

# Set the initial population size and the total number of time steps
N0 = 1
T = 100

# Initialize the population array and the time array
N = np.zeros(T+1, dtype=int)
N[0] = N0
t = np.arange(T+1)

# Simulate the process
for i in range(T):
    dt = 0.1 # time step
    rate = N[i] + 1 # birth rate
    prob_birth = rate * dt #probability of birth in time dt
    prob_same = 1 - prob_birth #Birth or no birth
    if np.random.uniform() < prob_birth:
        N[i+1] = N[i] + 1 #population increase
    else:
        N[i+1] = N[i] #population same

# Plot the results
fig,axs=plt.subplots(2)
plt.subplots_adjust(wspace=0.3, hspace=0.7) 
axs[0].step(t, N)
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Population size')
axs[0].set_title("Birth Process")
axs[0].grid()


# Set the initial population size and the total number of time steps
N0 = 50
T = 100

# Initialize the population array and the time array
N = np.zeros(T+1, dtype=int)
N[0] = N0
t = np.arange(T+1)

# Simulate the process
for i in range(T):
    dt = 0.1 # time step
    rate = 1 # death rate
    prob_death = rate * dt #probability of death in time dt
    prob_same = 1 - prob_death  #death or no death
    if np.random.uniform() < prob_death:
        N[i+1] = N[i] - 1 #population decrease
    else:
        N[i+1] = N[i]  #population same

# Plot the results
axs[1].step(t, N)
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Population size')
axs[1].set_title("Death Process")
axs[1].grid()

plt.show()
