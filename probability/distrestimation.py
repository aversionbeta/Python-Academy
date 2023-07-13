import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from numpy.random import normal
from scipy.stats import norm

sample = normal (size=10000)
plt.hist(sample,bins=30)
plt.show()
sample1 = normal (loc=50, scale=5,size=10000) 
mu = sample1.mean()
sigma = sample1.std()
dist = norm(mu,sigma)
values = [value for value in range(30,70)]
prob = [dist.pdf(value) for value in values]
plt.hist(sample1,bins=30,density=True)
plt.plot(values,prob)
plt.show()

from numpy import hstack
from sklearn.neighbors import KernelDensity

sample1 = normal(loc=20, scale=5, size=300)
sample2 = normal(loc=40, scale=5, size=700)
sample = hstack((sample1, sample2))

model = KernelDensity(bandwidth=2, kernel='gaussian')
sample = sample.reshape((len(sample), 1))
model.fit(sample)

values = np.asarray([value for value in range(1, 60)])
values = values.reshape((len(values), 1))
probabilities = model.score_samples(values) #probabilidad logarítmica
probabilities = np.exp(probabilities)  # inversión de probabilidad

plt.hist(sample, bins=50, density=True) 
plt.plot(values[:], probabilities)
plt.show()