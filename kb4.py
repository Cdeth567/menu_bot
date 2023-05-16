from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_simple_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text='Завтрак')
    btn2 = KeyboardButton(text='Обед')
    btn3 = KeyboardButton(text='Ужин')
    btn4 = KeyboardButton(text='Закрыть')
    kb.add(btn1)
    kb.add(btn2)
    kb.add(btn3)
    kb.add(btn4)
    return kb


def get_simple_kb1():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Каша овсяная'))\
        .add(KeyboardButton('Чай с сахаром')).add(KeyboardButton('Батон')).add(KeyboardButton('Масло сливочное')).add(KeyboardButton('Назад'))
    return kb


def get_simple_kb2():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Винегрет овощной'))\
        .add(KeyboardButton('Рассольник домашний')).add(KeyboardButton('Рыба отварная'))\
        .add(KeyboardButton('Картофель отварной')).add(KeyboardButton('Сок персиковый'))\
        .add(KeyboardButton('Хлеб пшеничный')).add(KeyboardButton('Назад'))
    return kb


def get_simple_kb3():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Салат из свежей капусты'))\
        .add(KeyboardButton('Плов из свинины')).add(KeyboardButton('Чай'))\
        .add(KeyboardButton('Хлеб')).add(KeyboardButton('Назад'))
    return kb


def price_1():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add('150 руб.').add('Назад😄')
    return kb


def price_2():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add('200 руб.').add('Назад😄')
    return kb


def price_3():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add('80 руб.').add('Назад😄')
    return kb


def price_4():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add('20 руб.').add('Назад😄')
    return kb


def price_5():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add('100 руб.').add('Назад😉')
    return kb


def price_6():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add('250 руб.').add('Назад😉')
    return kb


def price_7():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add('75 руб.').add('Назад😉')
    return kb


def price_8():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add('100 руб.').add('Назад😉')
    return kb


def price_9():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add('200 руб.').add('Назад😉')
    return kb


def price_10():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add('40 руб.').add('Назад😉')
    return kb


def price_11():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add('100 руб.').add('Назад😎')
    return kb


def price_12():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add('250 руб.').add('Назад😎')
    return kb


def price_13():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add('200 руб.').add('Назад😎')
    return kb


def price_14():
    kb = ReplyKeyboardMarkup(resize_keyboard=True).add('40 руб.').add('Назад😎')
    return kb
