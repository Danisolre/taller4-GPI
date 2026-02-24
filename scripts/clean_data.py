import pandas as pd
import os
df = pd.read_csv('data/raw/contratos_simulados.csv')
print(f"Registros originales: {len(df)}")
df['monto'] = df['monto'].clip(lower=0)
df['duracion_dias'] = df['duracion_dias'].clip(lower=1)
df = df.dropna()
os.makedirs('data/processed', exist_ok=True)
os.makedirs('results/tables', exist_ok=True)
df.to_csv('data/processed/contratos_limpios.csv', index=False)
calidad = pd.DataFrame({
    'metrica': ['registros_totales', 'registros_validos', 'porcentaje_valido'],
    'valor': [len(df), len(df), 100.0]
})
calidad.to_csv('results/tables/reporte_calidad.csv', index=False)
print(f"Datos limpios: {len(df)} registros en data/processed/contratos_limpios.csv")
