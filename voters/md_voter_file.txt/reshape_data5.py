import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Set the matplotlib backend to Agg for headless environments
matplotlib.use('Agg')

# Load the data from the CSV file
df = pd.read_csv('agg_MD.csv')

# Group the data by age bracket, gender, and party, then sum the counts
grouped_df = df.groupby(['age_bracket', 'Gender', 'Party']).sum().reset_index()

# Calculate total counts for each age bracket
total_counts = grouped_df.groupby('age_bracket')['Count'].sum().reset_index()
total_counts.rename(columns={'Count': 'Total'}, inplace=True)

# Prepare data for Male_REP
male_rep_data = grouped_df[
    (grouped_df['Gender'] == 'Male') & (grouped_df['Party'] == 'REP')
]

# Merge total counts with the filtered data
male_rep_merged = pd.merge(male_rep_data, total_counts, on='age_bracket')

# Calculate the percentage of Male_REP relative to the total for each age bracket
male_rep_merged['Percentage'] = (male_rep_merged['Count'] / male_rep_merged['Total']) * 100

# Define a custom color palette with distinct colors for each age group
custom_palette = ['brown', 'teal', 'lime', 'navy', 'gold']

# Plot the data using seaborn
plt.figure(figsize=(12, 8))
sns.barplot(
    data=male_rep_merged, 
    x='age_bracket', 
    y='Percentage', 
    palette=custom_palette
)
plt.title('Male_REP Participation in each Age Group')
plt.xticks(rotation=45)
plt.ylabel('Percentage')
plt.xlabel('Age Group')
plt.tight_layout()

# Save the plot to a file instead of displaying it
plt.savefig('male_rep_percentage_distribution_chart.png')
print("Chart saved as 'male_rep_percentage_distribution_chart.png'")