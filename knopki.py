from __future__ import annotations

from Config import token
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import klikerer

bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())

main_menu = {"text": "не кликай", "reply_markup": klikerer.help_keyboard}

i = 0

@dp.message_handler(commands=['start'], state='*')
async def process_start(message: types.Message, state: FSMContext):
    await message.answer(**main_menu)


@dp.callback_query_handler(lambda c: c.data == 'one', state='k')
async def one(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.edit_text(f'хватит кликать ({i})', reply_markup=klikerer.back_keyboard)
    await state.update_data({'i': i})


@dp.callback_query_handler(lambda c: c.data == 'two', state='l')
async def two(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.edit_text(f'хватит кликать ({i})', reply_markup=klikerer.back_keyboard)
    await state.update_data({'i': i})
    await state.set_state('*')


executor.start_polling(dp, skip_updates=True)
