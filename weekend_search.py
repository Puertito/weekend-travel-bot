import os
import asyncio
import requests
from dotenv import load_dotenv
from telegram import Bot
from dates import next_weekends

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

bot = Bot(BOT_TOKEN)


async def search(destination, outbound_date, return_date):
    params = {
        "engine": "google_flights",
        "departure_id": "TFN",
        "arrival_id": destination,
        "outbound_date": outbound_date,
        "return_date": return_date,
        "currency": "EUR",
        "hl": "en",
        "api_key": SERPAPI_KEY,
    }

    response = requests.get(
        "https://serpapi.com/search.json",
        params=params,
    )

    if response.status_code != 200:
        print("Ошибка запроса:", response.status_code)
        return None

    data = response.json()

    flights = data.get("best_flights", [])

    if len(flights) == 0:
        return None

    flight = flights[0]

    return {
        "destination": destination,
        "price": flight.get("price"),
        "airline": flight["flights"][0].get("airline"),
        "duration": flight.get("total_duration"),
        "outbound": outbound_date,
        "return": return_date,
    }


async def main():

    best_offer = None

    # Проверяем BCN и MAD
    for destination in ["BCN", "MAD"]:

        # Проверяем 12 ближайших выходных
        for outbound, inbound in next_weekends(12):

            print(f"Проверяю {destination} {outbound} -> {inbound}")

            flight = await search(
                destination,
                outbound,
                inbound,
            )

            if flight is None:
                continue

            if (
                best_offer is None
                or flight["price"] < best_offer["price"]
            ):
                best_offer = flight

    if best_offer is None:
        print("Ничего не найдено")
        return

    if best_offer["price"] > 50:
        print("Цена выше 50 €, сообщение не отправляется.")
        return

    message = f"""
🔥 Лучшее предложение

✈️ Маршрут:
TFN → {best_offer["destination"]}

📅 Вылет:
{best_offer["outbound"]}

📅 Возврат:
{best_offer["return"]}

💶 Цена:
{best_offer["price"]} €

✈️ Авиакомпания:
{best_offer["airline"]}

🕒 Время в пути:
{best_offer["duration"]} минут
"""

    await bot.send_message(
        chat_id=CHAT_ID,
        text=message,
    )

    print("Сообщение отправлено!")


if __name__ == "__main__":
    asyncio.run(main())