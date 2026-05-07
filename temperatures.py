import requests
import json
from datetime import datetime

# Coordenades de Barcelona
LAT = 41.3888
LON = 2.159

# URL API Open-Meteo
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={LAT}&longitude={LON}"
    f"&hourly=temperature_2m"
    f"&forecast_days=1"
)

# Obtenir dades
response = requests.get(url)
data = response.json()

# Temperatures del dia
temps = data["hourly"]["temperature_2m"]

# Càlculs
temp_max = max(temps)
temp_min = min(temps)
temp_avg = sum(temps) / len(temps)

# Data actual
today = datetime.now().strftime("%Y%m%d")

# Nom fitxer
filename = f"temp_{today}.json"

# Dades exportar
resultat = {
    "data": today,
    "temperatura_maxima": temp_max,
    "temperatura_minima": temp_min,
    "temperatura_mitjana": round(temp_avg, 2)
}

# Guardar JSON
with open(filename, "w", encoding="utf-8") as f:
    json.dump(resultat, f, indent=4, ensure_ascii=False)

print(f"Fitxer creat: {filename}")
