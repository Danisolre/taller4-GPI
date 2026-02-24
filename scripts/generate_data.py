import numpy as np
import pandas as pd
import random
import os
np.random.seed(42)
random.seed(42)
n = 500
modalidades = ['Contratacion Directa', 'Licitacion Publica',
    'Seleccion Abreviada', 'Minima Cuantia', 'Concurso de Meritos']
estados = ['Ejecutado', 'En ejecucion', 'Incumplido', 'Liquidado']
entidades = [f'Entidad_{i}' for i in range(1, 21)]
datos = {
    'id_contrato': [f'CT-2024-{str(i).zfill(4)}' for i in range(1, n+1)],
    'modalidad': [random.choice(modalidades) for _ in range(n)],
    'entidad': [random.choice(entidades) for _ in range(n)],
    'monto': np.random.lognormal(mean=17, sigma=1.5, size=n).round(0),
    'duracion_dias': np.random.randint(30, 365, size=n),
    'estado': [random.choice(estados) for _ in range(n)],
    'tiene_adicion': [random.random() < 0.3 for _ in range(n)]
}

df = pd.DataFrame(datos)
df['fecha_firma'] = pd.date_range('2024-01-01', periods=n, freq='D')
os.makedirs('data/raw', exist_ok=True)
df.to_csv('data/raw/contratos_simulados.csv', index=False)
print(f"Datos generados: {len(df)} contratos")
