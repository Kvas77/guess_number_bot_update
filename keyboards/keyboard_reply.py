from aiogram.types import KeyboardButton, ReplyKeyboardMarkup 


# main
play_button = KeyboardButton(text='PLAY! 🎮')
statistic_button = KeyboardButton(text='Statictics 🏆')
settings_button = KeyboardButton(text='Settings ⚙️')
cancel_button = KeyboardButton(text='Cancel ❌')

main_keyboard = ReplyKeyboardMarkup(keyboard=[[play_button, statistic_button, settings_button, cancel_button]],
                                    resize_keyboard=True,
                                    input_field_placeholder='Ничего не пишите, просто нажимайте на кнопки',
                                    one_time_keyboard=True)

# statistics 
reload_stat_button = KeyboardButton(text='Reload Statistics 🔄')
back_button = KeyboardButton(text='Back ↩️')

statistics_keyboard = ReplyKeyboardMarkup(keyboard=[[reload_stat_button, back_button]],
                                    resize_keyboard=True,
                                    input_field_placeholder='Ничего не пишите, просто нажимайте на кнопки',
                                    one_time_keyboard=True)

