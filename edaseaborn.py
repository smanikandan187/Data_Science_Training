import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Age': [25, 30, 22, 35, 28, 40],
    'Salary': [50000, 60000, 45000, 80000, 52000, 90000],
    'Experience': [3, 5, 2, 7, 4, 10]
})

sns.histplot(df['Age'], kde=True)
plt.title("Age Distribution")
plt.show()

sns.pairplot(df)
plt.show()
