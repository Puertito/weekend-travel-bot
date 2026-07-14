import asyncio
from telegram import Bot
from config import BOT_TOKEN, CHAT_ID


async def main():
    bot = Bot(token=BOT_TOKEN)

    await bot.send_message(
        chat_id=CHAT_ID,
        text="🎉 Поздравляю! Твой Telegram-бот работает!"
    )


if __name__ == "__main__":
    asyncio.run(main())