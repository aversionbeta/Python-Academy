import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = x ** 2 

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.9])
axes2 = fig.add_axes([0.2,0.55,0.4,0.3])
axes.plot(x, y, 'bD:')
axes2.plot(x, y, 'rX--')
axes2.set_facecolor('grey')
plt.show()