import numpy as np
import matplotlib.pyplot as plt

age = np.array([25, 30, 22, 35, 28, 40])
salary = np.array([50000, 60000, 45000, 80000, 52000, 90000])

plt.hist(age)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

plt.scatter(age, salary)
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

plt.boxplot(salary)
plt.title("Salary Boxplot")
plt.ylabel("Salary")
plt.show()
