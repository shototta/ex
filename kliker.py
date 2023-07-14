from __future__ import annotations

from Config import token
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import klikerer


bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())


main = {"text": "не кликай", "reply_markup": klikerer.help_keyboard}

@dp.message_handler(commands=['start'], state='*')
async def process_start(message: types.Message, state: FSMContext):
    await message.answer(**main)

i = 0

@dp.callback_query_handler(lambda c: c.data == 'KLIK', state='k')
async def k(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.edit_text(f'хватит кликать ({i})')
    await state.update_data({'i': i+1})
    await state.set_state('l')


@dp.callback_query_handler(lambda c: c.data == 'KLIK', state='l')
async def l(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await state.update_data({'i': i + 1})
    await callback_query.message.edit_text(f'хватит кликать ({i})')
    await state.set_state('k')



executor.start_polling(dp, skip_updates=True)