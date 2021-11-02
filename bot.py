#!venv/bin/python
import os
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

# Объект бота
bot = Bot(token=API_TOKEN)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Хэндлер на команду /start
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Хэй, Бро!\nЧто у нас сегодня по тратам?")

# Хэндлер на команду /help
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь!")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)