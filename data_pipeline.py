import requests, pandas as pd  
url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"  
data = requests.get(url).json()  
df = pd.DataFrame(data["hourly"])  
df.to_csv("weather.csv", index=False)  
