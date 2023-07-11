from __future__ import annotations
from Config import token
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


#bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())


b_n = KeyboardButton('нет')
b_d = KeyboardButton('да')

b1 = KeyboardButton('нет')
b2 = KeyboardButton('да')

b3 = KeyboardButton('нет')
b4 = KeyboardButton('да')

b5 = KeyboardButton('нет')
b6 = KeyboardButton('да')

choose_chat_type_keyboard_true = ReplyKeyboardMarkup(resize_keyboard=True).insert(b_n).insert(b_d)
choose_chat_type_keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True).insert(b1).insert(b2)
choose_chat_type_keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True).insert(b3).insert(b4)
choose_chat_type_keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True).insert(b5).insert(b6)



a = []


@dp.message_handler(commands='start', state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('Привет! Готов к викторине?', reply_markup=choose_chat_type_keyboard_true)
    await state.set_state('true')

@dp.message_handler(state='true')
async def per1_handler(message: types.Message, state: FSMContext):
    per = message.text
    if per == "да":
        await message.answer('Отлично, начнем')
        await state.set_state('per1')
    else:
        await message.answer('Ну а что поделаешь. Жизнь такая, нужно проходить...')
        await state.set_state('per1')

@dp.message_handler(state='per1')
async def per2_handler(message: types.Message, state: FSMContext):
    await message.answer('Тебе нравится учеба?', reply_markup=choose_chat_type_keyboard1)
    per1 = message.text
    if per1 == "да":
        await message.answer('Отлично, идем дальше')
        a.append(1)
        await state.set_state('per2')
    else:
        await message.answer('Хорошо, идем дальше')
        a.append(0)
        await state.set_state('per2')

@dp.message_handler(state='per2')
async def per3_handler(message: types.Message, state: FSMContext):
    await message.answer('Тебе нравится лагерь?', reply_markup=choose_chat_type_keyboard2)
    per2 = message.text
    if per2 == "да":
        await message.answer('Отлично, идем дальше')
        a.append(1)
        await state.set_state('per3')
    else:
        await message.answer('Хорошо, идем дальше')
        a.append(0)
        await state.set_state('per3')

@dp.message_handler(state='per3')
async def per2_handler(message: types.Message, state: FSMContext):
    await message.answer('Тебе нравится Иннополис?', reply_markup=choose_chat_type_keyboard3)
    per3 = message.text
    if per3 == "да":
        await message.answer('Отлично, идем дальше')
        a.append(1)
        await state.set_state('pod')
    else:
        await message.answer('Хорошо, идем дальше')
        a.append(0)
        await state.set_state('pod')

@dp.message_handler(state='pod')
async def pod_handler(message: types.Message, state: FSMContext):
    await message.answer('Итак, твой результат...')
    b = 0
    for element in a:
        b = b + element
    if b == 0:
        await message.answer('0/3: а с у ж д а ю')
    elif b == 1:
        await message.answer('1/3: неплохо')
    elif b == 2:
        await message.answer('2/3: хорошо')
    else:
        await message.answer('3/3: отлично!')


executor.start_polling(dp, skip_updates=True)