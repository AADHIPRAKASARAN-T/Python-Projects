import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Creating dataframe
dataframe = pd.read_csv(r"C:\Users\raja\OneDrive\Desktop\Zomato-data-.csv")
print(dataframe.head())

#Rebuilding the rate column
def handlerate(value):
    if isinstance(value, str) and '/' in value:
        try:
            return float(value.split('/')[0].strip())
        except:
            return np.nan
    return np.nan

dataframe['rate'] = dataframe['rate'].apply(handlerate)
print(dataframe['rate'].head())

#Approx cost for two people
dataframe['approx_cost(for two people)'] = dataframe['approx_cost(for two people)'].astype(str).str.replace(',', '')
dataframe['approx_cost(for two people)'] = pd.to_numeric(dataframe['approx_cost(for two people)'], errors='coerce')

#Votes By restaurant type
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum().sort_values(ascending=False)

pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)

#Create a figure with subplots 
fig, axes = plt.subplots(3, 3, figsize=(24, 18))# 3 rows x 3 cols = 9 plots
fig.suptitle("Zomato Data Analysis Dashboard", fontsize=24, fontweight='bold')
plt.subplots_adjust(hspace=0.5, wspace=0.4)

# 1. Count of Restaurant Types
sns.countplot(x='listed_in(type)', data=dataframe, ax=axes[0, 0])
axes[0, 0].set_title('Count of Restaurant Types')
axes[0, 0].tick_params(axis='x', rotation=90)

# 2. Total Votes by Restaurant Type
axes[0, 1].plot(grouped_data.index, grouped_data.values, c='green', marker='o')
axes[0, 1].set_title("Total Votes by Restaurant Type")
axes[0, 1].set_xlabel("Type", color="purple", size=10)
axes[0, 1].set_ylabel("Votes", color="orange", size=10)
axes[0, 1].tick_params(axis='x', rotation=90)

# 3. Online Order Availability
sns.countplot(x='online_order', data=dataframe, ax=axes[0, 2])
axes[0, 2].set_title("Online Order Availability")

# 4. Ratings Distribution
sns.histplot(dataframe['rate'].dropna(), bins=5, kde=True, ax=axes[1, 0])
axes[1, 0].set_title("Ratings Distribution")

# 5. Approximate Cost for Two People
sns.histplot(dataframe['approx_cost(for two people)'].dropna(), bins=20, ax=axes[1, 1])
axes[1, 1].set_title("Approximate Cost for Two People")

# 6. Ratings by Online Order Availability
sns.boxplot(x='online_order', y='rate', data=dataframe, ax=axes[1, 2])
axes[1, 2].set_title("Ratings by Online Order Availability")

# 7. Heatmap: Order Mode vs Restaurant Type
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d', ax=axes[2, 0])
axes[2, 0].set_title("Heatmap: Order Mode vs Restaurant Type")

# 8. Restaurant(s) with Max Votes (Text only, plotted as a table)
max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, ['name', 'votes']]
axes[2, 1].axis('off')  # No plot, just show text
axes[2, 1].set_title("Restaurant(s) with Max Votes")
axes[2, 1].table(cellText=restaurant_with_max_votes.values, colLabels=restaurant_with_max_votes.columns, loc='center')

# 9. Empty or custom plot slot
axes[2, 2].axis('off')

# Show all plots together
plt.show()

