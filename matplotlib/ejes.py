import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)
y= np.sin(x)

fig, axes = plt.subplots(1,2,figsize=(5,5))
axes[0].plot(x,y, label="$sin (x)$")
axes[0].set_title('Relacion X Y')
axes[0].set_xlabel('Eje X')
axes[0].set_ylabel('Eje Y')
axes[0].legend(loc='lower right')
axes[1].plot(y,x)
axes[1].set_title('Relacion Y X')
axes[1].set_xlabel('Eje X')
axes[1].set_ylabel('Eje Y')
plt.show()