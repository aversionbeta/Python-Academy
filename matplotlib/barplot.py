import matplotlib.pyplot as plt
import numpy as np

country= ['India', 'Mexico', 'EEUU', 'Australia', 'France']
population = [1000,800,900,1000,300]

plt.bar(country,population, width=0.5, color=['orange','yellow'])
plt.xticks(np.arange(5), ('Ind', 'Mex', 'EU', 'Aus','Fra'), rotation=45)

plt.barh(country,population)

plt.show()