import pandas as pd

df = pd.read_csv('data/processed/contratos_limpios.csv')

media = df['monto'].mean()
mediana = df['monto'].median()
print(f"Media: {media}")
print(f"Mediana: {mediana}")
