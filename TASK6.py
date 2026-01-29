import pandas as pd

# read dataset
data = pd.read_csv("Dataset .csv")

# remove missing values
data = data.dropna(subset=['Votes', 'Aggregate rating'])

# restaurant with highest votes
max_votes_row = data.loc[data['Votes'].idxmax()]
print("Restaurant with highest votes:", max_votes_row['Restaurant Name'])
print("Votes:", max_votes_row['Votes'])

# restaurant with lowest votes
min_votes_row = data.loc[data['Votes'].idxmin()]
print("\nRestaurant with lowest votes:", min_votes_row['Restaurant Name'])
print("Votes:", min_votes_row['Votes'])

# correlation between votes and rating
correlation = data[['Votes', 'Aggregate rating']].corr()

print("\nCorrelation between Votes and Rating:")
print(correlation)
