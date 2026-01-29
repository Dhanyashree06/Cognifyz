import pandas as pd

df = pd.read_csv("Dataset .csv")

total_restaurants = len(df)

df = df.dropna(subset=['Cuisines'])

all_cuisines = df['Cuisines'].str.split(', ').explode()

cuisine_counts = all_cuisines.value_counts()

top_3_cuisines = cuisine_counts.head(3)

print("--- Top 3 Cuisines and their Percentages ---")

for cuisine, count in top_3_cuisines.items():
    percentage = (count / total_restaurants) * 100
    print(f"{cuisine}: {percentage:.2f}%")
