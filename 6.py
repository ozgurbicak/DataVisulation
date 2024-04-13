import matplotlib.pyplot as plt
import pandas as pd

# Read the dataset
df = pd.read_csv('movies.csv', dtype={'score': float, 'country': str})

# Group by country, calculate total movie counts and average IMDb scores
country_stats = df.groupby('country').agg({'name': 'count', 'score': 'mean'}).sort_values(by='name', ascending=False).head(10)

# Visualization
fig, ax1 = plt.subplots(figsize=(12, 8))

# 1st Y-axis: Movie Counts
color = 'tab:blue'
ax1.set_xlabel('Country', fontsize=14)
ax1.set_ylabel('Movie Counts', color=color, fontsize=14)
bars = ax1.bar(country_stats.index, country_stats['name'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Rotate X-axis labels
plt.xticks(rotation=45, ha='right')

# 2nd Y-axis: Average IMDb Scores
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Average IMDb Score', color=color, fontsize=14)
ax2.plot(country_stats.index, country_stats['score'], color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)

# Title and Display
plt.title('Comparison of Total Movie Counts and Average IMDb Scores by Countries', fontsize=16)

# Add legend for the second Y-axis
lines, labels = ax2.get_legend_handles_labels()
ax2.legend(lines, labels, loc='upper left')

plt.tight_layout()
plt.show()
