import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

#for root, dirs, files in os.walk('input'):
#    print(root, dirs, files)

annual_enterprise = pd.read_csv('input/annual-enterprise-survey-2023-financial-year-provisional.csv')

print(annual_enterprise.head())

annual_enterprise['Units'] = pd.Categorical(annual_enterprise['Units'])#series... no necesita conversion
annual_enterprise['Variable_code'] = pd.Categorical(annual_enterprise['Variable_code'])


# Crear valores aleatorios para colores y áreas
N = len(annual_enterprise)
colors = np.random.rand(N)
area = (30 * np.random.rand(N)) ** 2

# Crear el gráfico de dispersión
plt.figure(figsize=(10, 6))
scatter = plt.scatter( s=area, c=colors, alpha=0.5, marker='v')

# Añadir etiquetas y título
plt.xlabel('Units')
plt.ylabel('Variable Code')
plt.title('Scatter Plot de Annual Enterprise Survey')

# Mostrar la gráfica
plt.show()