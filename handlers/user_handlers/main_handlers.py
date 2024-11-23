from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from lexicon.lexicon import lexicon
from keyboards.keyboard_reply import main_keyboard 


router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    global user_language
    user_language = message.from_user.language_code
    await message.answer(text=lexicon[user_language]['/start'].format(message.from_user.full_name),
                         reply_markup=main_keyboard)
    

@router.message(F.text == 'Cancel ❌')
async def process_play_command(message: Message):
    await message.answer(text=lexicon[user_language]['/cancel'])


@router.message(F.text == 'PLAY! 🎮')
async def process_play_command(message: Message):
    await message.answer(text=lexicon[user_language]['/play'])
