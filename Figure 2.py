import pandas as pd
import matplotlib.pyplot as plt

# read the dataset
df = pd.read_csv('onlinefoods.csv')

# Calculate the distribution of occupation
occupation_distribution = df['Occupation'].value_counts()

# Create a pie chart with a 'donut' style
plt.figure(figsize=(8, 6))
plt.pie(occupation_distribution, labels=occupation_distribution.index, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.4))

# Draw a circle at the center to create a 'donut' style
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Donut Chart of Occupation Distribution')
plt.axis('equal') 

# Show the plot
plt.show()