import pandas as pd

data = pd.read_csv("Dataset .csv")

total = len(data)

online_yes = data[data['Has Online delivery'] == 'Yes']
online_no = data[data['Has Online delivery'] == 'No']

percent_yes = (len(online_yes) / total) * 100
percent_no = (len(online_no) / total) * 100

print("Online Delivery Yes:", round(percent_yes, 2), "%")
print("Online Delivery No:", round(percent_no, 2), "%")

avg_yes = online_yes['Aggregate rating'].mean()
avg_no = online_no['Aggregate rating'].mean()

print("\nAverage Rating (Online Delivery Yes):", round(avg_yes, 2))
print("Average Rating (Online Delivery No):", round(avg_no, 2))
