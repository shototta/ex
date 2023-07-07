from Config import token
from aiogram import Bot, Dispatcher, executor, types

url = 'https://api.thecatapi.com/v1/images/search'

bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_mes(message: types.Message):
    await message.answer('добро пожаловать в тест эхо')


@dp.message_handler(commands=['getcat'])
async def cat_cat(message: types.Message):

    await message.answer('лови')
    await message.answer_photo(photo='https://cdn2.thecatapi.com/images/2es.jpg')






@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True)