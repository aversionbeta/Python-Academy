import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset('tips')
tip.head()
sns.histplot(data=tip, x='tip',bins=15,cumulative=False, hue='sex', stat='probability', multiple='fill')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset('tips')
tip.head()
sns.kdeplot(data=tip, x='tip', hue='sex', cumulative=False)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset('tips')
tip.head()
sns.ecdfplot(data=tip, x='tip',hue='sex', stat='count')
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset('tips')
tip.head()
sns.displot(data=tip,x='tip',hue='sex', kind='hist',multiple='stack')
plt.show()