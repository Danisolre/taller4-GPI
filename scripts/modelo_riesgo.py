import pandas as pd
df = pd.read_csv('data/processed/contratos_limpios.csv')
df['score_riesgo'] = 0
df.loc[df['monto'] > df['monto'].quantile(0.75), 'score_riesgo'] += 1
df.loc[df['duracion_dias'] > 300, 'score_riesgo'] += 1
df.loc[df['tiene_adicion'] == True, 'score_riesgo'] += 1
alto_riesgo = df[df['score_riesgo'] >= 2].sort_values('score_riesgo', ascending=False)
alto_riesgo.head(20).to_csv('results/tables/contratos_alto_riesgo.csv', index=False)
print(f"Contratos alto riesgo: {len(alto_riesgo)}")
