from aiogram import Bot, Dispatcher, types
import asyncio
import logging
import config
from handlers import common
from bot.handlers import career_choice

# Функция для установки команд в левом меню
async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command="/start", description="Начать работу с ботом"),
        types.BotCommand(command="/fox", description="Показать лису"),
        # Добавьте другие команды по необходимости
    ]
    await bot.set_my_commands(commands)

# Функция запуска бота
async def main():
    # Включаем логирование
    logging.basicConfig(level=logging.INFO)

    # Создаем объекты бота и диспетчера
    bot = Bot(token=config.token)
    dp = Dispatcher()

    dp.include_routers(career_choice.router, common.router)

    # Устанавливаем команды для меню
    await set_commands(bot)

    # Запуск polling
    await dp.start_polling(bot)

# Функция для обработки ошибок
async def error_handler(update: types.Update, exception: Exception):
    logging.error(f"Произошла ошибка: {exception}")
    if update.message:
        await update.message.answer("Извините, произошла ошибка.")

if __name__ == "__main__":
    asyncio.run(main())
