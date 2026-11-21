
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Penguins Data.csv')

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(df['Culmen Length (mm)'], df['Body Mass (g)'], color='blue')
plt.xlabel('Culmen Length (mm)')
plt.ylabel('Body Mass (g)')
plt.title('Culmen Length vs Body Mass')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.scatter(df['Culmen Depth (mm)'], df['Body Mass (g)'], color='red')
plt.xlabel('Culmen Depth (mm)')
plt.ylabel('Body Mass (g)')
plt.title('Culmen Depth vs Body Mass')
plt.grid(True)

plt.tight_layout()
plt.show()
