import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

HOME_AIRPORT = os.getenv("HOME_AIRPORT", "TFN")
DESTINATIONS = os.getenv("DESTINATIONS", "BCN,MAD").split(",")

MAX_PRICE_BCN = int(os.getenv("MAX_PRICE_BCN", "50"))
MAX_PRICE_MAD = int(os.getenv("MAX_PRICE_MAD", "50"))