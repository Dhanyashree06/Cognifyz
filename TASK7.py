import pandas as pd

data = pd.read_csv("Dataset .csv")

online_delivery = data.groupby('Price range')['Has Online delivery'].value_counts(normalize=True) * 100

print("Online Delivery Percentage by Price Range:")
print(online_delivery)

table_booking = data.groupby('Price range')['Has Table booking'].value_counts(normalize=True) * 100

print("\nTable Booking Percentage by Price Range:")
print(table_booking)
