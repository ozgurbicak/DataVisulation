import matplotlib.pyplot as plt
import pandas as pd

# Read the dataset
df = pd.read_csv('movies.csv', dtype={'budget': float, 'gross': float, 'company': str})

# Calculate the total budget and gross revenue for each company
company_total_budget_gross = df.groupby('company')[['budget', 'gross']].sum().sort_values(by='budget', ascending=False).head(10)

# Visualize the total budget and gross revenue for companies
plt.figure(figsize=(12, 8))
bar_chart = company_total_budget_gross.plot(kind='bar', color=['blue', 'orange'])
plt.xlabel('Company', fontsize=14)
plt.ylabel('Total Budget and Gross Revenue', fontsize=14)
plt.title('Top Film Production Companies by Total Budget and Gross Revenue', fontsize=16)

# Rotate and align the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

plt.show()
