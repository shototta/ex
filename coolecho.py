from __future__ import annotations
from Config import token
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

b1 = KeyboardButton('чат 1 на 1')
b2 = KeyboardButton('групповой чат')

choose_chat_type_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).insert(b1).insert(b2)


bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())

waiting_users: set[int] = set()
connected_pairs: dict[int, int] = {}

@dp.message_handler(commands='start', state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('Добро пожаловать в чат поддержки! Нажми /find чтобы написать')
    await state.set_state('ready')


@dp.message_handler(commands='find', state='ready')
async def find_handler(message: types.Message, state: FSMContext):
    await message.answer('Соединяем...')
    await state.set_state('ototot')
    await go(message, state)


@dp.message_handler(state='ototot')
async def go(message: types.Message, state: FSMContext):
    waiting_users.add(message.from_user.id)
    #print(message.from_user.username)
    for i in tuple(waiting_users):
        if i == 1717383692:
            user_ot = i
            await state.update_data(user_ot=user_ot)
            waiting_users.remove(i)
        else:
            await state.set_state('ototot')


    while len(waiting_users) >= 1:
        data = await state.get_data()
        user_ot = data['user_ot']
        user_1_id = user_ot
        user_2_id = waiting_users.pop()

        await dp.current_state(chat=user_1_id, user=user_1_id).set_state('chatting')
        await dp.current_state(chat=user_2_id, user=user_2_id).set_state('chatting')

        connected_pairs[user_1_id] = user_2_id
        connected_pairs[user_2_id] = user_1_id

        await bot.send_message(chat_id=user_1_id, text='Вы начали общаться')
        await bot.send_message(chat_id=user_2_id, text='Вы начали общаться')


@dp.message_handler(state='chatting')
async def chatting_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    chatmate_id = connected_pairs[user_id]
    await bot.send_message(chat_id=chatmate_id, text=message.text)


@dp.message_handler(state='*')
async def error_handler(message: types.Message, state: FSMContext):
    await message.reply(f'Неверный формат сообщения. Ваш текущий state: {await state.get_state()}')

executor.start_polling(dp, skip_updates=True)