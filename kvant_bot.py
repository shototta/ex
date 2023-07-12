from __future__ import annotations
from Config import token
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from kvant_button import choose_kat, choose_pay, fp2p_all, f2p_t, fp2p_t, p2p_t, info, sait, keyboard, kat_again


bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands='start', state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('Добро пожаловать в инфо-бот "Кванториума"! Что вас интересует?', reply_markup= choose_kat)
    await state.set_state('vb')


@dp.message_handler(state='vb')
async def kat_handler(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == "Общее":
        await state.set_state('ssil')
        await stil_handler(message, state)
    elif answer == "О программах":
        await state.set_state('prog')
        await prog_handler(message, state)
    elif answer == "Распределение":
        await state.set_state('check')
        await check(message, state)
    elif answer == "Поддержка":
        await state.set_state('check')
        await check(message, state)
    elif answer == "Оставить отзыв":
        await state.set_state('necheck')
        await check(message, state)
    else:
        await message.answer('Выберите интересующий Вас раздел', reply_markup= choose_kat)
        await state.set_state('vb')
        #асуждаю, но а что поделаешь


@dp.message_handler(state='ssil')
async def stil_handler(message: types.Message, state: FSMContext):
    await message.answer(info, reply_markup=kat_again)
    await state.set_state('kill')


@dp.message_handler(state='ssil')
async def kill_handler(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == "К каталогу":
        await state.set_state('vb')
        await kat_handler(message,state)
    else:
        await state.set_state('ssil')
        await kill_handler(message, state)


@dp.message_handler(state='check')
async def check(message: types.Message, state: FSMContext):
    await message.answer('Тип работает')
    await state.set_state('vb')

@dp.message_handler(state='necheck')
async def check(message: types.Message, state: FSMContext):
    await message.answer('Тип не работает')
    await state.set_state('vb')


@dp.message_handler(state='prog')
async def prog_handler(message: types.Message, state: FSMContext):
    await message.answer('Какие программы вас интересуют?',reply_markup= choose_pay)
    await state.set_state('pay')


@dp.message_handler(state='pay')
async def pay_handler(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == "Бесплатные программы":
        await state.set_state('f2p')
        await f2p(message,state)
    elif answer == "Платныее программы/оплачеваемые ПФДО":
        await state.set_state('fp2p')
        await fp2p(message, state)
    elif answer == "Платные программы":
        await state.set_state('p2p')
        await p2p(message, state)
    elif answer == "К каталогу":
        await state.set_state('vb')
        await kat_handler(message, state)
    else:
        await message.answer('Выберите интересующие Вас программы')
        await state.set_state('pay')
        #продолжаю кринж


@dp.message_handler(state='f2p')
async def f2p(message: types.Message, state: FSMContext):
    await message.answer(f2p_t, reply_markup=fp2p_all)
    await state.set_state('ppls')


@dp.message_handler(state='fp2p')
async def fp2p(message: types.Message, state: FSMContext):
    await message.answer(fp2p_t, reply_markup=fp2p_all)
    await state.set_state('ppls')


@dp.message_handler(state='p2p')
async def p2p(message: types.Message, state: FSMContext):
    await message.answer(p2p_t, reply_markup=fp2p_all)
    await state.set_state('ppls')


@dp.message_handler(state='ppls')
async def back_pay_pls(message: types.Message, state: FSMContext):
    await state.set_state('prog')
    await prog_handler(message, state)



















executor.start_polling(dp, skip_updates=True)