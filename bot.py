from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from config import BOT_TOKEN
from handlers import start, play, vote, leaderboard

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

start.register(dp)
play.register(dp)
vote.register(dp)
leaderboard.register(dp)

if __name__ == "__main__":
    executor.start_polling(dp)
