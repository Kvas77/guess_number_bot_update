from aiogram import F, Router
from aiogram.types import Message

from lexicon.lexicon import lexicon
from keyboards.keyboard_reply import main_keyboard, statistics_keyboard

router = Router()


@router.message(F.text == 'Statictics 🏆')
async def process_statistics_command(message: Message):
    global user_language
    user_language = message.from_user.language_code
    await message.answer(text=lexicon[user_language]['/statistics'],
                         reply_markup=statistics_keyboard)


@router.message(F.text == 'Reload Statistics 🔄')
async def process_reload_stat_command(message: Message):
    await message.answer(text=lexicon[user_language]['/reload_stat'],
                         reply_markup=main_keyboard)


@router.message(F.text == 'Back ↩️')
async def process_back_command(message: Message):
    await message.answer(text=lexicon[user_language]['/back'],
                         reply_markup=main_keyboard)

