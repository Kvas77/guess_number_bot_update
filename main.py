import asyncio

from aiogram import Bot, Dispatcher

from handlers.user_handlers import play_handlers, settings_handlers, statistics_handlers 
from config_data.config import load_config


async def main():
    config = load_config()

    bot = Bot(config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(play_handlers.router)
    dp.include_router(statistics_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
