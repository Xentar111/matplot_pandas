import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

#for root, dirs, files in os.walk('input'):
#    print(root, dirs, files)

annual_enterprise = pd.read_csv('input/annual-enterprise-survey-2023-financial-year-provisional.csv')

print(annual_enterprise.head())

annual_enterprise['Units'] = pd.Categorical(annual_enterprise['Units'])#series... no necesita conversion
annual_enterprise['Industry_name_NZSIOC'] = pd.Categorical(annual_enterprise['Industry_name_NZSIOC'])

# Únicamente los contadores enteros de cada categoría y convertir a numpy arreglos
units_codes = annual_enterprise['Units'].cat.codes.to_numpy()
variable_codes = annual_enterprise['Industry_name_NZSIOC'].cat.codes.to_numpy()

#print(units_codes)
#print(variable_codes)

industry_name = annual_enterprise['Industry_name_NZSIOC'].unique()

print(industry_name)

# Crear valores aleatorios para colores y áreas
N = len(annual_enterprise)
colors = np.random.rand(N)
area = (30 * np.random.rand(N)) ** 2

# Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))
scatter = plt.scatter(units_codes, variable_codes, s=area, c=colors, alpha=0.5, marker='.')

# Añadir etiquetas y título
plt.xlabel('Units')
plt.ylabel('Industry Name NZSIOC')
plt.title('Scatter Plot de Annual Enterprise Survey')

# Mostrar la gráfica
plt.show()