import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

annual_enterprise = pd.read_csv('annual-enterprise-survey-2023-financial-year-provisional.csv')

print(annual_enterprise.head())
print(annual_enterprise.shape)

#print(annual_enterprise.columns)
print(annual_enterprise['Variable_code'])
#print(annual_enterprise.dtypes)

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

#provisional_.scatter(annual_enterprise['Units'], annual_enterprise['Value'])#mal implemetado
#provisional_.scatter(x=annual_enterprise['Units'], y=annual_enterprise['Value'])

# A;adir division de industry_code, variable_categoria, 
# variable_name, tambien year esas creo q son las mas importantes
#plt.show()