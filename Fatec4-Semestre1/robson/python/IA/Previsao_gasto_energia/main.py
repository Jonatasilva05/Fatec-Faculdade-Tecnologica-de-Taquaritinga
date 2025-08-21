import numpy as np
import tensorflow as tf
from tensorflow import keras

# Gerar dados sintéticos
np.random.seed(42) # Para reprodutibilidade

num_dias = 20

# Temperatura Média do Dia (°C)
temperaturas = np.random.uniform(low=20.0, high=35.0, size=num_dias)

# Horas de Uso do Ar-Condicionado (horas)
horas_ac = np.random.uniform(low=0.0, high=12.0, size=num_dias)

# Consumo de Energia no Dia Seguinte (kWh)
# Fórmula: consumo_base + (temperatura * 0.5) + (horas_ac * 1.5) + ruído
consumo_base = 5.0
ruido = np.random.normal(loc=0.0, scale=2.0, size=num_dias) # Ruído aleatório

consumo_energia = consumo_base + (temperaturas * 0.5) + (horas_ac * 1.5) + ruido

# Organizar os dados em arrays NumPy
# Características (Temperatura e Horas de AC)
X = np.column_stack((temperaturas, horas_ac)).astype(np.float32)

# Rótulo (Consumo de Energia no Dia Seguinte)
y = consumo_energia.astype(np.float32)

print("Dados de Características (X):")
print(X[:5]) # Mostrar as primeiras 5 linhas
print("\nDados de Rótulo (y):")
print(y[:5]) # Mostrar as primeiras 5 linhas