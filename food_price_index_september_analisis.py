import matplotlib.pyplot as plt
import pandas as pd

food_price = pd.read_csv('input/food-price-index-september-2023-weighted-average-prices.csv')

print(food_price.head())
#print(len(set(food_price['Series_title_1'].values)))
#print(len(set(food_price['Series_reference'].values)))
print(len(food_price['Data_value'].values))


filter_df = food_price[food_price['Series_reference'] == 'CPIM.SAP0100']

print(filter_df.head())
print(filter_df.shape)

print(pd.to_datetime(filter_df['Period'], format='%Y.%m'))
""" 
ValueError: time data "2006" doesn't match format "%Y.%m", at position 0. You might want to try:
    - passing `format` if your strings have a consistent format;
    - passing `format='ISO8601'` if your strings are all ISO8601 but not necessarily in exactly the same format;
    - passing `format='mixed'`, and the format will be inferred for each element individually. You might want to use `dayfirst` alongside this.
"""


#filter_df['Period']

filter_df = filter_df.sort_values(by='Period')


