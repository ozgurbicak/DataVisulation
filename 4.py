import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Read the dataset
df = pd.read_csv('movies.csv', dtype={'votes': float, 'score': float})

# Visualize the relationship between scores and votes with a scatter plot
plt.figure(figsize=(12, 8))
sns.scatterplot(x='score', y='votes', data=df, alpha=0.7, color='skyblue')
plt.xlabel('Score', fontsize=14)
plt.ylabel('Number of Votes', fontsize=14)
plt.title('Relationship Between Movie Scores and Number of Votes', fontsize=16)
plt.show()
