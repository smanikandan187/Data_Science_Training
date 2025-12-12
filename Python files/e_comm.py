import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = pd.read_csv('2019.csv', encoding='latin1')

print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.describe())    

scores = df['Score']
gdf = df['GDP per capita']

plt.figure(figsize=(10, 6))
plt.plot(gdf, scores,marker='x', linestyle='-.', color='blue')
plt.title('GDP per Capita vs Scores')
plt.xlabel('GDP per Capita')    
plt.ylabel('Scores')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x=gdf, y=scores, hue=df['Region'], palette='Set1')
plt.title('GDP per Capita vs Scores by Region')    