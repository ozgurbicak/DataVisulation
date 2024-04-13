import matplotlib.pyplot as plt
import pandas as pd

# Read the dataset
df = pd.read_csv('movies.csv', dtype={'gross': float})

# Calculate the average gross revenues by genre
average_gross_by_genre = df.groupby('genre')['gross'].mean().sort_values(ascending=False)

# Visualization with horizontal bar chart
plt.figure(figsize=(12, 8))
average_gross_by_genre.plot(kind='barh', color='skyblue')
plt.xlabel('Average Gross Revenue', fontsize=14)
plt.ylabel('Movie Genre', fontsize=14)
plt.title('Average Gross Revenues by Genre (Horizontal Bar Chart)', fontsize=16)
plt.show()
