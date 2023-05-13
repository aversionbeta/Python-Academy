import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11)

print(plt.style.available)
plt.style.use('dark_background')

fig,axe = plt.subplots(figsize=(8,8))
axe.plot(x,x+1, color='red', alpha=0.9, linewidth=5, linestyle=':', marker='o', markersize=0.1, markersize=0.8)
axe.plot(x,x+2, 'b-')
axe.plot(x,x+3, color = '#66ff66',linestyle='dashed', marker='v',)
axe.plot(x,x+4, 'yo:')

plt.show()
