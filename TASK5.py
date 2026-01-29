import pandas as pd

data = pd.read_csv("Dataset .csv")

data = data.dropna(subset=['Rating text'])

data['Rating text'] = data['Rating text'].str.lower()

positive_words = ['good', 'great', 'excellent', 'amazing', 'nice', 'love']
negative_words = ['bad', 'poor', 'worst', 'average', 'slow', 'disappointed']

positive_count = {}
for word in positive_words:
    positive_count[word] = data['Rating text'].str.contains(word).sum()

negative_count = {}
for word in negative_words:
    negative_count[word] = data['Rating text'].str.contains(word).sum()

print("Most common positive keywords:")
print(positive_count)

print("\nMost common negative keywords:")
print(negative_count)

data['Review Length'] = data['Rating text'].apply(len)

avg_length = data['Review Length'].mean()
print("\nAverage review length:", round(avg_length, 2))

relation = data[['Review Length', 'Aggregate rating']].corr()

print("\nRelationship between review length and rating:")
print(relation)
