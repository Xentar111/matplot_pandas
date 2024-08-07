import matplotlib.pyplot as plt
import pandas as pd

food_price = pd.read_csv('input/food-price-index-september-2023-weighted-average-prices.csv')

print(food_price.head())

plt.plot(food_price['Data_value'], food_price['Period'])
plt.show()