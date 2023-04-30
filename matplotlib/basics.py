import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,5,11)
y = x**2 
plt.plot(x,y, 'yD:')
plt.show()

x=np.linspace(0,5,11)
y = x**2 
plt.hist(x,y)
plt.show()

x=np.linspace(0,5,11)
y = x**2 
plt.pie(x)
plt.show()

x=np.linspace(0,5,11)
y = x**2 
plt.scatter(x,y)
plt.show()

x=np.linspace(0,5,11)
y = x**2 
plt.boxplot(x,y)
plt.show()