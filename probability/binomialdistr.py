import pandas as pd
from math import factorial
from numpy.random import binomial
from scipy.stats import binom
import matplotlib as plt

def my_binomial(k,n,p):
    return factorial(n)/(factorial(k)*(n-k))*pow(p,k)*pow(1-p,n-k)

print(my_binomial (2,3,0.5))

dist = binom(3,0.5)
print(dist.pmf(2)) #probabilitymathfunction = probability to obtain 2 results
print(dist.cdf(2)) #accumulated density function = probability to obtain 2 or less results

#random generator

from numpy.random import binomial
import numpy as np

p=0.5
n=3
print(binomial(n,p))

arr = []

for _ in range(100):
    arr.append(binomial(n,p))

print(arr)

def plot_hist(num_trials):
    values = [0,1,2,3]
    arr  = []
    for _ in range(num_trials):
        arr.append(binomial(n,p))

print(np.unique(arr,return_counts=True))
