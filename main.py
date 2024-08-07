import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

#for root, dirs, files in os.walk('input'):
#    print(root, dirs, files)

annual_enterprise = pd.read_csv('input/annual-enterprise-survey-2023-financial-year-provisional.csv')

print(annual_enterprise.head())
#print(annual_enterprise.shape)

#print(annual_enterprise.columns)
#print(annual_enterprise['Variable_code'])
#print(annual_enterprise.dtypes)


series_units = pd.Series(pd.Categorical(annual_enterprise['Units']))
#print(type(series_units))
print(series_units)

plt.scatter(annual_enterprise['Units'], annual_enterprise['Variable_code'], color='red')
for i in range(series_units):
    plt.annotate(f"({annual_enterprise['Units'][i]}, {annual_enterprise['Variable_code'][i]}), (annual_enterprise['Units'][i]), annual_enterprise['Variable_code'][i]")

plt.legend()
plt.show()

fig, ax = plt.subplots()
#ax.plot(annual_enterprise['Industry_aggregation_NZSIOC'])

#Data
ax.scatter(y=annual_enterprise['Industry_name_NZSIOC'], x=annual_enterprise['Industry_aggregation_NZSIOC'])

#GUI
ax.set_xlabel('Industry_NZSIOC')
ax.set_ylabel('Industry_name_NZSIOC')
ax.set_title('Enterprise_survey_2023')

# Units provisional??
fig, provisional_ = plt.subplots()

#
#print(annual_enterprise['Units'])
#print(annual_enterprise['Value'])

#provisional_.scatter(annual_enterprise['Units'], annual_enterprise['Value'])#mal implementado
#provisional_.scatter(x=annual_enterprise['Units'], y=annual_enterprise['Value'])

# A;adir division de industry_code, variable_categoria, 
# variable_name, tambien year esas creo q son las mas importantes
# plt.show()