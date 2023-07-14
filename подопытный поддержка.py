from __future__ import annotations
from Config import token
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())

waiting_users: set[int] = set()
connected_pairs: dict[int, int] = {}

@dp.message_handler(commands='start', state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('Привет! Добро пожаловать в чат-рулетку! Как тебя зовут?')
    await state.set_state('name')

@dp.message_handler(state='name')
async def name_handler(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({'name': name})
    await message.reply(f'Приятно познакомитья, {name}! Нажми /find чтобы начать')
    await state.set_state('ready')


@dp.message_handler(commands='find', state='ready')
async def find_handler(message: types.Message, state: FSMContext):
    await message.answer('Ищем собеседника...')


@dp.message_handler(state='set')
async def find_handler(message: types.Message, state: FSMContext):
    waiting_users.add(message.from_user.id)

    for el in waiting_users:
        if el == 1717383692:
            user_ot = el

            #print(message.from_user.username)
            while len(waiting_users) >= 1:
                user_1_id = waiting_users.pop()
                user_2_id = user_ot

                if user_1_id != 1717383692:
                    await dp.current_state(chat=user_1_id, user=user_1_id).set_state('chatting')
                    await dp.current_state(chat=user_2_id, user=user_2_id).set_state('chatting')

                    connected_pairs[user_1_id] = user_2_id
                    connected_pairs[user_2_id] = user_1_id

                    await bot.send_message(chat_id=user_1_id, text='Вы начали общаться')
                    await bot.send_message(chat_id=user_2_id, text='Вы начали общаться')

                else:
                    await state.set_state('set')


@dp.message_handler(state='chatting')
async def chatting_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    chatmate_id = connected_pairs[user_id]
    await bot.send_message(chat_id=chatmate_id, text=message.text)


@dp.message_handler(state='*')
async def error_handler(message: types.Message, state: FSMContext):
    await message.reply(f'Неверный формат сообщения. Ваш текущий state: {await state.get_state()}')

executor.start_polling(dp, skip_updates=True)