import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

annual_enterprise = pd.read_csv('annual-enterprise-survey-2023-financial-year-provisional.csv')

print(annual_enterprise.head())

fig, ax = plt.subplots()
#ax.plot(annual_enterprise['Industry_aggregation_NZSIOC'])
ax.scatter(y=annual_enterprise['Industry_name_NZSIOC'], x=annual_enterprise['Industry_aggregation_NZSIOC'])
ax.set_xlabel('Industry_NZSIOC')
ax.set_ylabel('Industry_name_NZSIOC')
ax.set_title('Enterprise_survey_2023')
#plt.plot(annual_enterprise['Industry_code_NZSIOC'])
plt.show()