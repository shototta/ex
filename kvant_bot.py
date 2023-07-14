from __future__ import annotations
from Config import token
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from kvant_button import choose_kat, choose_pay, fp2p_all, f2p_t, fp2p_t, p2p_t, kat_again, tip_info, adap, pay, choose
from aiogram.types import ReplyKeyboardRemove
import kvant_button
from kvant_button import ways_of_differentiation, ways_of_differentiation_hud_b, ways_of_differentiation_IT_bp, ways_of_differentiation_IT_p, ways_of_differentiation_IT_b, ways_of_differentiation_hud_bp, ways_of_differentiation_hud_p

bot = Bot(token)
dp = Dispatcher(bot, storage=MemoryStorage())

info = {"text": "хотите перейти на официальный сайт?",
        "reply_markup": kvant_button.go_keyboard}

active_users: set[int] = set()


@dp.message_handler(commands='start', state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('Добро пожаловать в инфо-бот "Кванториума"! Что вас интересует?', reply_markup=choose_kat)
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
        await state.set_state('bespredrl')
        await bes_handler(message, state)
    #elif answer == "Поддержка":
        #await state.set_state('pip')
        #await start_handlerrr(message, state)
    #elif answer == "Оставить отзыв":
        #await state.set_state('necheck')
        #await check(message, state)
    else:
        await message.answer('Выберите интересующий Вас раздел', reply_markup=choose_kat)
        await state.set_state('vb')
        # асуждаю, но а что поделаешь


waiting_users: set[int] = set()
connected_pairs: dict[int, int] = {}


@dp.message_handler(state='pip')
async def start_handlerrr(message: types.Message, state: FSMContext):
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
    # print(message.from_user.username)
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

        await bot.send_message(chat_id=user_1_id, text='Вы начали общаться', reply_markup= kat_again)
        await state.set_state('kill')
        await kill_handler(message, state)
        await bot.send_message(chat_id=user_2_id, text='Вы начали общаться', reply_markup= kat_again)
        await state.set_state('kill')
        await kill_handler(message, state)


@dp.message_handler(state='chatting')
async def chatting_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    chatmate_id = connected_pairs[user_id]
    await bot.send_message(chat_id=chatmate_id, text=message.text)



@dp.message_handler(state='bespredrl')
async def bes_handler(message: types.Message, state: FSMContext):
    await message.answer('Сколько лет Вам/Вашему ребенку?', reply_markup=ReplyKeyboardRemove())
    await state.set_state('an1')


@dp.message_handler(state='an1')
async def an1(message: types.Message, state: FSMContext):
    age = message.text
    try:
        age = int(age)
    except:
        await state.set_state('bespredrl')
        await bes_handler(message, state)
    else:
        await state.update_data(age=age)
        if (age > 2) and (age < 19):
            await message.answer('Вас интересуют адаптированные направления?', reply_markup=adap)
            await state.set_state('an2')
        else:
            await message.answer('К сожалению, для Вас нет подходящей группы', reply_markup=kat_again)
            await state.set_state('kill')


@dp.message_handler(state='an2')
async def an2(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == "Адаптированная программа":
        await state.set_state('prosto')
        await p(message, state)
    elif answer == "Стандартная программа":
        await state.set_state('prosto_pi')
        await pp(message, state)
    else:
        await state.set_state('an2')
        await message.answer('loh')


@dp.message_handler(state='prosto_pi')
async def pp(message: types.Message, state: FSMContext):
    await message.answer('Какое направление Вам подходит?', reply_markup= pay)
    await state.set_state('hru')


@dp.message_handler(state='hru')
async def hru_handler(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == "Техническое":
        await state.set_state('gg')
        await gg(message, state)
    elif answer == "Художественное":
        await state.set_state('vp')
        await vp(message, state)
    else:
        await state.set_state('prosto_pi')


@dp.message_handler(state='prosto')
async def p(message: types.Message, state: FSMContext):
    data = await state.get_data()
    age = data['age']
    if (age >= 5) and (age <= 17):
        await message.answer('Вот направления, которые мы можем Вам предложить:', reply_markup=kat_again)
        for way in ways_of_differentiation:
            if (age >= way.min_age) and (age <= way.max_age):
                await message.answer(f'{way.name} : \n\n{way.description}')
                await state.set_state('kill')
                # помогите
    else:
        await message.answer('К сожалению, для Вас нет подходящей группы', reply_markup=kat_again)
        await state.set_state('kill')


@dp.message_handler(state='gg')
async def gg(message: types.Message, state: FSMContext):
    await message.answer('Какие программы Вас интересуют?', reply_markup= choose)
    await state.set_state('ggg')


@dp.message_handler(state='ggg')
async def heg(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == "Бесплатные программы":
        await state.set_state('f2pp')
        await f2pp(message, state)
    elif answer == "Платныее программы/оплачеваемые ПФДО":
        await state.set_state('fp2pp')
        await fp2pp(message, state)
    elif answer == "Платные программы":
        await state.set_state('p2pp')
        await p2pp(message, state)
    else:
        await message.answer('Выберите интересующие Вас программы')
        await state.set_state('ggg')


@dp.message_handler(state='f2pp')
async def f2pp(message: types.Message, state: FSMContext):
    data = await state.get_data()
    age = data['age']
    if (age >= 7) and (age <= 17):
        await message.answer('Вот направления, которые мы можем Вам предложить:', reply_markup=kat_again)
        for way in ways_of_differentiation_IT_b:
            if (age >= way.min_age) and (age <= way.max_age):
                await message.answer(f'{way.name} : \n\n{way.description}')
                await state.set_state('kill')
    else:
        await message.answer('К сожалению, для Вас нет подходящей группы', reply_markup=kat_again)
        await state.set_state('kill')


@dp.message_handler(state='fp2pp')
async def fp2pp(message: types.Message, state: FSMContext):
    data = await state.get_data()
    age = data['age']
    if (age >= 5) and (age <= 17):
        await message.answer('Вот направления, которые мы можем Вам предложить:', reply_markup=kat_again)
        for way in ways_of_differentiation_IT_bp:
            if (age >= way.min_age) and (age <= way.max_age):
                await message.answer(f'{way.name} : \n\n{way.description}')
                await state.set_state('kill')
    else:
        await message.answer('К сожалению, для Вас нет подходящей группы', reply_markup=kat_again)
        await state.set_state('kill')


@dp.message_handler(state='p2pp')
async def p2pp(message: types.Message, state: FSMContext):
    data = await state.get_data()
    age = data['age']
    if (age >= 3) and (age <= 5):
        await message.answer('Вот направления, которые мы можем Вам предложить:', reply_markup=kat_again)
        for way in ways_of_differentiation_IT_p:
            if (age >= way.min_age) and (age <= way.max_age):
                await message.answer(f'{way.name} : \n\n{way.description}')
                await state.set_state('kill')
    else:
        await message.answer('К сожалению, для Вас нет подходящей группы', reply_markup=kat_again)
        await state.set_state('kill')


@dp.message_handler(state='vp')
async def vp(message: types.Message, state: FSMContext):
    await message.answer('Какие программы Вас интересуют?', reply_markup= choose)
    await state.set_state('vvp')


@dp.message_handler(state='vvp')
async def hegg(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == "Бесплатные программы":
        await state.set_state('f2pppp')
        await f2pppp(message, state)
    elif answer == "Платныее программы/оплачеваемые ПФДО":
        await state.set_state('fp2pppp')
        await fp2pppp(message, state)
    elif answer == "Платные программы":
        await state.set_state('p2pppp')
        await p2pppp(message, state)
    else:
        await message.answer('Выберите интересующие Вас программы')
        await state.set_state('vvp')


@dp.message_handler(state='f2pppp')
async def f2pppp(message: types.Message, state: FSMContext):
    data = await state.get_data()
    age = data['age']
    if (age >= 5) and (age <= 18):
        await message.answer('Вот направления, которые мы можем Вам предложить:', reply_markup=kat_again)
        for way in ways_of_differentiation_hud_b:
            if (age >= way.min_age) and (age <= way.max_age):
                await message.answer(f'{way.name} : \n\n{way.description}')
                await state.set_state('kill')
    else:
        await message.answer('К сожалению, для Вас нет подходящей группы', reply_markup=kat_again)
        await state.set_state('kill')


@dp.message_handler(state='fp2pppp')
async def fp2pppp(message: types.Message, state: FSMContext):
    data = await state.get_data()
    age = data['age']
    if (age >= 5) and (age <= 18):
        await message.answer('Вот направления, которые мы можем Вам предложить:', reply_markup=kat_again)
        for way in ways_of_differentiation_hud_bp:
            if (age >= way.min_age) and (age <= way.max_age):
                await message.answer(f'{way.name} : \n\n{way.description}')
                await state.set_state('kill')
    else:
        await message.answer('К сожалению, для Вас нет подходящей группы', reply_markup=kat_again)
        await state.set_state('kill')


@dp.message_handler(state='p2pppp')
async def p2pppp(message: types.Message, state: FSMContext):
    data = await state.get_data()
    age = data['age']
    if (age >= 3) and (age <= 5):
        await message.answer('Вот направления, которые мы можем Вам предложить:', reply_markup=kat_again)
        for way in ways_of_differentiation_hud_p:
            if (age >= way.min_age) and (age <= way.max_age):
                await message.answer(f'{way.name} : \n\n{way.description}')
                await state.set_state('kill')
    else:
        await message.answer('К сожалению, для Вас нет подходящей группы', reply_markup=kat_again)
        await state.set_state('kill')


@dp.message_handler(state='ssil')
async def stil_handler(message: types.Message, state: FSMContext):
    await message.answer(tip_info, reply_markup=kat_again)
    await message.answer(**info)
    await state.set_state('kill')


@dp.message_handler(state='kill')
async def kill_handler(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == "К каталогу":
        await state.set_state('vb')
        await kat_handler(message, state)
    else:
        await state.set_state('kill')
        await kill_handler(message, state)


@dp.message_handler(state='prog')
async def prog_handler(message: types.Message, state: FSMContext):
    await message.answer('Какие программы вас интересуют?', reply_markup=choose_pay)
    await state.set_state('pay')


@dp.message_handler(state='pay')
async def pay_handler(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == "Бесплатные программы":
        await state.set_state('f2p')
        await f2p(message, state)
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
        # продолжаю кринж


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
