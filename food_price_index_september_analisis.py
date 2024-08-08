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

print(pd.to_datetime(filter_df['Period']))

#filter_df['Period']