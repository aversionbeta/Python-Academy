
import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset('tips')
tip.head(2)
sns.countplot(data=tip,x='day',hue='sex')
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset('tips')
tip.head(2)
plt.figure(figsize=(6,6))
sns.stripplot(data=tip,x='day',hue='sex', y='total_bill',dodge=True)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset('tips')
tip.head(2)
plt.figure(figsize=(6,6))
sns.swarmplot(data=tip,x='day',hue='sex', y='total_bill',dodge=True)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset('tips')
tip.head(2)
plt.figure(figsize=(6,6))
sns.boxplot(data=tip,x='day',hue='sex', y='total_bill',dodge=True)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset('tips')
tip.head(2)
plt.figure(figsize=(6,6))
sns.boxplot(data=tip,x='day',hue='sex', y='total_bill',dodge=True)
sns.swarmplot(data=tip,x='day',hue='sex', y='total_bill',dodge=True)
sns.countplot(data=tip,x='day',hue='sex')
sns.stipplot(data=tip,x='day',hue='sex', y='total_bill',dodge=Tru)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset('tips')
tip.head(2)
plt.figure(figsize=(8,8))
sns.scatterplot(data=tip, x='total_bill',y='tip', hue='day', style='time', size='size')
plt.legend(loc='center',bbox_to_anchor=(1.08,0.5))

plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset('tips')
tip.head(2)
sns.relplot(data=tip, x='total_bill',y='tip', hue='day', style='time', size='size', col='time')
plt.legend(loc='center',bbox_to_anchor=(1.08,0.5))

plt.show()