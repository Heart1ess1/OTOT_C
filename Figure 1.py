import pandas as pd
import matplotlib.pyplot as plt

# Read data
data = pd.read_csv('onlinefoods.csv')

# Plotting histograms, one subgroup per 1 year of age
plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(data['Age'], bins=range(min(data['Age']), max(data['Age']) + 2), color='skyblue', edgecolor='black', align='left')

# Set the x-axis scale
plt.xticks(range(min(data['Age']), max(data['Age']) + 1))

plt.title('Age Distribution Histogram')
plt.xlabel('Age')
plt.ylabel('Count')
plt.grid(axis='y', alpha=0.75)
plt.show()