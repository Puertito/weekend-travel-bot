import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SERPAPI_KEY")

url = "https://serpapi.com/search.json"

params = {
    "engine": "google_flights",
    "departure_id": "TFN",
    "arrival_id": "BCN",
    "outbound_date": "2026-08-14",
    "return_date": "2026-08-16",
    "currency": "EUR",
    "hl": "en",
    "api_key": API_KEY,
}

response = requests.get(url, params=params)
data = response.json()

import json

with open("response.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Файл response.json сохранен")

print("========== РЕЗУЛЬТАТ ==========")

best_flights = data.get("best_flights", [])

if not best_flights:
    print("Билеты не найдены")
else:
    for flight in best_flights:
        print("----------------------------")
        print("Цена:", flight.get("price"))
        print("Всего пересадок:", flight.get("layovers"))
        print("Длительность:", flight.get("total_duration"))