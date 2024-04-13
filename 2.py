import matplotlib.pyplot as plt
import pandas as pd

# Read the dataset
df = pd.read_csv('movies.csv', parse_dates=['year'], dtype={'budget': float, 'gross': float})

# Calculate the average film budgets and gross revenues by year
average_budget_by_year = df.groupby(df['year'].dt.year)['budget'].mean()
average_gross_by_year = df.groupby(df['year'].dt.year)['gross'].mean()

# Visualization using area chart
plt.figure(figsize=(12, 8))
plt.fill_between(average_budget_by_year.index, average_budget_by_year.values, label='Average Budget', color='blue', alpha=0.5)
plt.fill_between(average_gross_by_year.index, average_gross_by_year.values, label='Average Gross Revenue', color='green', alpha=0.5)

plt.xlabel('Year', fontsize=14)
plt.ylabel('Average Values', fontsize=14)
plt.title('Average Film Budgets and Gross Revenues Over the Years (Area Chart)', fontsize=16)
plt.legend()
plt.show()
