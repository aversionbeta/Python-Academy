
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
plt.show()