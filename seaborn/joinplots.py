import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset('tips')
tip.head(2)

sns.jointplot(data=tip,x='total_bill', y='tip',hue='sex', kind='hist', marginal_ticks=True, marginal_kws=dict(bins=25,fill=False, multiple='dodge'))
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset('tips')
tip.head(2)

sns.pairplot(data=tip, hue='sex', palette='Spectral', kind='scatter')
plt.show()