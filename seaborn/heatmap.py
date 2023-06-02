import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')
print(tips)

tips.corr()

sns.heatmap(tips.corr(), annot=True, cmap='coolwarm', linewidths=5, linecolor='black')
plt.show()