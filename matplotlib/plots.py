import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(1,50,100)

plt.hist(data, bins=50, width=5, histtype='step')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(1,50,100)

plt.boxplot(data, vert=False, patch_artist=True, notch=True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

N = 50

x = np.random.rand(N)
y = np.random.rand(N)
area = (30 * np.random.rand(N))**2
colors = np.random.rand(N)
plt.scatter(x,y, s= area, c=colors, marker='p', alpha=0.5 )
plt.show()