from Config import token
from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_mes(message: types.Message):
    await message.answer('Привет, как тебя зовут?')

