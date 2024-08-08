import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

food_price = pd.read_csv('input/food-price-index-september-2023-weighted-average-prices.csv')

print(food_price.head())
#print(len(set(food_price['Series_title_1'].values)))
#print(len(set(food_price['Series_reference'].values)))
print(len(food_price['Data_value'].values))


filter_df = food_price[food_price['Series_reference'] == 'CPIM.SAP0100']

#print(filter_df.head())
#print(filter_df.shape)


def parse_period(period):
    try:
        print(pd.to_datetime(period, format='%Y.%m'))
    except ValueError:
        print(pd.to_datetime(period, format='%Y.%m', errors='corece'))
""" 
ValueError: time data "2006" doesn't match format "%Y.%m", at position 0. You might want to try:
    - passing `format` if your strings have a consistent format;
    - passing `format='ISO8601'` if your strings are all ISO8601 but not necessarily in exactly the same format;
    - passing `format='mixed'`, and the format will be inferred for each element individually. You might want to use `dayfirst` alongside this.
"""

filter_df['Period'] = filter_df['Period'].apply(parse_period)

filter_df = filter_df.dropna(subset=['Period'])
filter_df = filter_df.sort_values(by='Period')

print(filter_df.head())

#plt.bar(filter_df['Period'], filter_df['Data_value'], width=0.8)
#plt.xlabel('Data Value')
#plt.ylabel('Period')
#plt.title('Orange Price')
#plt.show()

plt.hist(filter_df['Data_value'])#, bins=np.unique(filter_df['Period']))
print(filter_df.tail())
plt.xlabel('Data Value')
plt.ylabel('Period')
plt.title('Orange Values')
plt.grid(True)
plt.show()