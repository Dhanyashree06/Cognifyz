import pandas as pd

# Read the dataset
# Note: The file name in the directory is 'Dataset .csv'
df = pd.read_csv("Dataset .csv")

# Total number of restaurants (original count)
total_restaurants = len(df)

# Drop rows with missing Cuisines if any
df = df.dropna(subset=['Cuisines'])

# Split cuisines into a list and explode to count individual occurrences
all_cuisines = df['Cuisines'].str.split(', ').explode()

# Count the frequency of each cuisine
cuisine_counts = all_cuisines.value_counts()

# Get the top 3 most common cuisines
top_3_cuisines = cuisine_counts.head(3)

print("--- Top 3 Cuisines and their Percentages ---")

for cuisine, count in top_3_cuisines.items():
    percentage = (count / total_restaurants) * 100
    print(f"{cuisine}: {percentage:.2f}%")
