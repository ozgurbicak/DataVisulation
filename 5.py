import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Read the dataset
df = pd.read_csv('movies.csv', parse_dates=['year'], dtype={'rating': str})

# Group by year and rating, calculate the counts
rating_counts = df.groupby(['year', 'rating']).size().unstack()

# Visualize the change in ratings over the years with a line chart
plt.figure(figsize=(14, 8))
sns.lineplot(data=rating_counts, markers=True)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Number of Movies', fontsize=14)
plt.title('Change in Movie Ratings Over the Years', fontsize=16)
plt.legend(title='Rating Type', title_fontsize='12')
plt.show()
