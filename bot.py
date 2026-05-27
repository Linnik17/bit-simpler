
import os
import random
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

history = [1.2, 1.1, 1.4, 1.3, 5.7, 1.1, 1.0]

def generate_signal(data):
    low_rounds = sum(1 for x in data[-5:] if x < 2)

    if low_rounds >= 4:
        return "🚀 Возможен высокий множитель в следующем раунде"
    elif data[-1] > 5:
        return "⚠️ После большого икса лучше пропустить 1-2 раунда"
    else:
        return random.choice([
            "🎯 Осторожная игра x1.5-x2",
            "💤 Явного сигнала нет",
            "🔥 Возможен импульс x3+"
        ])

async def send_message():
    bot = Bot(token=TOKEN)
    signal = generate_signal(history)
    await bot.send_message(chat_id=CHAT_ID, text=signal)

if __name__ == "__main__":
    import asyncio
    asyncio.run(send_message())
