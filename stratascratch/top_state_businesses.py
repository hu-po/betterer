# Import your libraries
import pandas as pd

# top 5 states with most 5 star businesses
# output state name, # of 5 star businesses (descending)
# if ties, return all unique states ordered alphabetically

# Start writing code
yelp_business.head()
df = yelp_business[['state', 'stars']][yelp_business['stars'] == 5]
df = df.groupby(['state'], as_index=False).count()
df = df.sort_values(by='stars', ascending=False).head(6)
df[:-3] = df[:-3].sort_values(by='state')
df
