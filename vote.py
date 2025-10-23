from aiogram import Dispatcher, types
from services.sheets import record_vote

def register(dp: Dispatcher):
    @dp.callback_query_handler(lambda c: c.data.startswith("vote_"))
    async def handle_vote(callback_query: types.CallbackQuery):
        vote = int(callback_query.data.split("_")[1])
        user = callback_query.from_user

        # Записываем голос в таблицу
        record_vote(user.id, vote)

        await callback_query.answer("Голос засчитан! ✅")
      
