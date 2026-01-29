import pandas as pd

data = pd.read_csv("Dataset .csv")

city_count = data['City'].value_counts()
top_city = city_count.index[0]

print("City with highest number of restaurants:", top_city)

avg_rating = data.groupby('City')['Aggregate rating'].mean()

print("\nAverage rating for each city:")
print(avg_rating)

best_city = avg_rating.idxmax()

print("\nCity with highest average rating:", best_city)
