import pandas as pd
import matplotlib.pyplot as plt

# read dataset
data = pd.read_csv("Dataset .csv")

# count price range
price_count = data['Price range'].value_counts().sort_index()

# bar chart
plt.bar(price_count.index, price_count.values)
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.title("Price Range Distribution")
plt.show()

# calculate percentage
total = price_count.sum()

print("Price Range Percentage:")
for price, count in price_count.items():
    percent = (count / total) * 100
    print("Price Range", price, ":", round(percent, 2), "%")
