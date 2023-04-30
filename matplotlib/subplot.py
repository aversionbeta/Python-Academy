import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2 

plt.subplot(1,2,1)
plt.plot(x,y, 'r--')
plt.plot(y,x, 'b:')
plt.subplot(1,2,2)
plt.hist(x,y)
plt.show()

plt.subplot(2,1,1)
plt.plot(x,y, 'r--')
plt.plot(y,x, 'b:')
plt.subplot(2,1,2)
plt.hist(x,y)
plt.show()