from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
                          InlineKeyboardButton, InlineKeyboardMarkup


help = InlineKeyboardButton("клик", callback_data='one')
help_keyboard = InlineKeyboardMarkup().insert(help)

back = InlineKeyboardButton("килк", callback_data='two')
back_keyboard = InlineKeyboardMarkup().add(back)