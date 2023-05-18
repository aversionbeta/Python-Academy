import seaborn as sns
import matplotlib.pyplot as plt

tip=sns.load_dataset('tips')
print(tip)

sns.displot(data=tip, x= 'total_bill')
plt.show()

sns.displot(data=tip, x= 'total_bill', y='tip', hue= 'sex')
plt.show()

sns.displot(data=tip, x= 'total_bill', hue= 'sex')
plt.show()

sns.displot(data=tip, x= 'total_bill', hue= 'sex', kind= 'kde', legend=True, palette='dark',alpha=0.25)
plt.show()