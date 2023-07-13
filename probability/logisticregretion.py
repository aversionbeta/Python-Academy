from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd
import seaborn as sns

def likelihood(y, yp):
    return yp*y+(1-yp)*(1-y)

fig = plt.figure()
ax = fig.gca(projection='3d')

Y = np.arange(0, 1, 0.01)
YP = np.arange(0, 1, 0.01)
Y, YP = np.meshgrid(Y, YP)
Z = likelihood(Y, YP)

surf = ax.plot_surface(Y, YP, Z, cmap=cm.coolwarm,linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

atrib_names = ['sepal length', 'sepal width', 'petal length', 'petal width']
X, y = load_iris(return_X_y=True)
X[:2]
y[:100]
clf = LogisticRegression(random_state=10, solver='liblinear').fit(X[:100], y[:100])
clf.coef_
model_coefs = pd.DataFrame(clf.coef_, columns=atrib_names)
model_coefs