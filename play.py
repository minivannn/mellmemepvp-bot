handlers/play.py
from aiogram import Dispatcher, types
from services.meme_generator import generate_meme_pair
from aiogram.types import InputFile, InlineKeyboardMarkup, InlineKeyboardButton
from io import BytesIO

def register(dp: Dispatcher):
    @dp.message_handler(commands=["play"])
    async def play_cmd(message: types.Message):
        meme1, meme2 = generate_meme_pair()

        # Преобразуем изображения в BytesIO
        bio1 = BytesIO()
        meme1.save(bio1, format="JPEG")
        bio1.seek(0)

        bio2 = BytesIO()
        meme2.save(bio2, format="JPEG")
        bio2.seek(0)

        keyboard = InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            InlineKeyboardButton("⬅️", callback_data="vote_0"),
            InlineKeyboardButton("➡️", callback_data="vote_1")
        )

        await message.answer_photo(InputFile(bio1, filename="meme1.jpg"), caption="Мем 1")
        await message.answer_photo(InputFile(bio2, filename="meme2.jpg"), caption="Мем 2", reply_markup=keyboard)
