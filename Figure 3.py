import pandas as pd
import matplotlib.pyplot as plt

# read the data
file_path = 'onlinefoods.csv'

# Read the dataset
data = pd.read_csv(file_path)

# Assuming each row represents an order, count the number of orders by family size
order_counts_by_family_size = data['Family size'].value_counts().sort_index()

# Create the bar chart
plt.figure(figsize=(10, 6))
order_counts_by_family_size.plot(kind='bar', color='teal')
plt.title('Bar Chart of Family Size & Online Food Orders')
plt.xlabel('Family size')
plt.ylabel('Number of Online Food Orders')
plt.xticks(rotation=0)  
plt.tight_layout() 
plt.show()