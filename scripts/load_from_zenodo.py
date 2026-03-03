import requests
import pandas as pd
import io
# DOI del dataset en Zenodo
ZENODO_RECORD_ID = "18855024"

# Obtener metadatos del registro via API
api_url = f"https://zenodo.org/api/records/{ZENODO_RECORD_ID}"
response = requests.get(api_url)
data = response.json()

# Extraer URL de descarga del archivo
file_url = data["files"][0]["links"]["self"]

# Descargar y leer el CSV directamente en memoria
file_response = requests.get(file_url)
df = pd.read_csv(io.BytesIO(file_response.content))

# Guardar localmente para que el pipeline existente funcione
df.to_csv("data/raw/contratos_simulados.csv", index=False)
print(f"Datos descargados desde Zenodo (DOI: 10.5281/zenodo.18855024)")
print(f"Registros: {len(df)}, Columnas: {list(df.columns)}")
