import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def gaussian (x,mu,sigma):
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-0.5*pow((x-mu)/sigma,2))

x = np.arange(-4,4,0.1)
y = gaussian(x,0.0,1)
plt.plot (x,y)
plt.show()

dist = norm(0,1)
x=np.arange(-4,4,0.1)
y = [dist.cdf(value) for value in x]
plt.plot (x,y)
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
df=[]
df = pd.read_csv(r'C:\Users\juand\Dropbox\Profesional\7. Delphus Lab\5. Delphus Lab Academy\Python-Academy\bestsellers-with-categories.csv')
arr = df['Reviews'].values[4:]

values, dist = np.unique(arr, return_counts=True)

plt.bar(values, dist)
plt.show()

mu = arr.mean()
sigma = arr.std()
x = np.arange(30,60,0.1)
dist = norm(mu,sigma)
y= [dist.pdf(value) for value in x]
plt.plot(x,y)
plt.show()