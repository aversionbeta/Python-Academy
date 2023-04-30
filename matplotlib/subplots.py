import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y = np.sin(x)

fig,axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x,y,'k')
axes[1].plot(x,y, 'g')
plt.show()

fig, axes = plt.subplots(2,4)
axes[0,0].plot(x,np.cos(x))
axes[0,1].plot(x,np.sin(x),'r')
axes[0,2].plot(x,np.tan(x),'y')
axes[0,3].plot(x,np.cos(x)**2,'k')
axes[1,0].plot(x,np.tanh(x),'b')
axes[1,1].plot(x,np.cos(x)**2,'r')
axes[1,2].plot(x,np.cos(x)**3,'g')
axes[1,3].plot(x,np.cos(x)**5,'k')
fig.tight_layout()
plt.show()