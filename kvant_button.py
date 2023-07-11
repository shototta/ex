from __future__ import annotations
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, \
                          InlineKeyboardButton, InlineKeyboardMarkup


b1_1 = KeyboardButton('Общее')
b1_2 = KeyboardButton('О программах')
b1_3 = KeyboardButton('Распределение')
b1_4 = KeyboardButton('Поддержка')
b1_5 = KeyboardButton('Оставить отзыв')

choose_kat = ReplyKeyboardMarkup(resize_keyboard=True).insert(b1_1).insert(b1_2).add(b1_3).insert(b1_4).add(b1_5)


b2_1 = KeyboardButton('Бесплатные программы')
b2_2 = KeyboardButton('Платныее программы/оплачеваемые ПФДО')
b2_3 = KeyboardButton('Платные программы')

kat = KeyboardButton('К каталогу')

choose_pay = ReplyKeyboardMarkup(resize_keyboard=True).insert(b2_1).add(b2_2).add(b2_3).add(kat)

back = KeyboardButton('Вернуться')
fp2p_all = ReplyKeyboardMarkup(resize_keyboard=True).insert(back)

f2p_t = "чета про:" \
        "робототехнику" \
        "адаптивка робототехника" \
        "поколение it" \
        "адптивка it" \
        "vr/ar" \
        "адаптивка vr/ar" \
        "пром диз" \
        "челодой инженер" \
        "песни" \
        "адаптитвка песни" \
        "пляски" \
        "матеша" \
        "шахматы" \
        "тех инглиш" \
        "аддативные техги" \
        "ии" \
        "чета про данные" \
        "медийники" \
            #нифигасе, а меня на ии не позвали :'(

fp2p_t = "чета про:" \
         "робототехника" \
         "песни" \
         "смешанные пляски" \
         "несмешанные пляски" \
         "шахматы" \
         "развитие" \
         "граф диз" \
         "3д ручки" \
         "смешанные пляски постарше" \
         "мультимедия" \
         "помощь в развитии" \
         "инглиш" \
         "дизайн"
p2p_t = "чета про:" \
        "пляски" \
        "робототехника"


sait = InlineKeyboardButton("перейти на сайт", callback_data='sait')
keyboard = InlineKeyboardMarkup().insert(sait)

info = {"я хороший я хороший", keyboard}
