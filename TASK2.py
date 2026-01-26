import pandas as pd
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

data = pd.read_csv("Dataset .csv")

city_count = data['City'].value_counts()
top_city = city_count.idxmax()

print("City with highest number of restaurants:", top_city)

avg_rating = data.groupby('City')['Aggregate rating'].mean()

print("\nAverage rating for each city:")
print(avg_rating)

best_city = avg_rating.idxmax()

print("\nCity with highest average rating:", best_city)
