from aiogram import Dispatcher, types
from services.sheets import get_leaderboard

def register(dp: Dispatcher):
    @dp.message_handler(commands=["leaderboard"])
    async def leaderboard_cmd(message: types.Message):
        leaderboard = get_leaderboard()
        text = "🏆 Топ игроков:\n\n"
        for i, (user_id, score) in enumerate(leaderboard, 1):
            text += f"{i}. ID {user_id}: {score} очков\n"
        await message.answer(text)
