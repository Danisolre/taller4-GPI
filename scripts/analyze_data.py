import pandas as pd
import os
df = pd.read_csv('data/processed/contratos_limpios.csv')
resumen = df.groupby('modalidad').agg(
    n_contratos=('id_contrato', 'count'),
    monto_promedio=('monto', 'mean'),
    monto_total=('monto', 'sum'),
    duracion_promedio=('duracion_dias', 'mean')
).round(0)
os.makedirs('results/tables', exist_ok=True)
resumen.to_csv('results/tables/resumen_estadisticas.csv')
print("Tabla de resumen generada en results/tables/resumen_estadisticas.csv")
print(resumen)
