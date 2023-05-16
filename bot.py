# @B11_demo_bot
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from kb4 import *
from aiogram.types import ReplyKeyboardRemove


bot = Bot(token='6288021917:AAHgqNbuWdQxZzXyph3LU36f3n5E-mGYl3w', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands='start')
async def menu_bot(message: types.Message):
    await message.answer('МЕНЮ', reply_markup=get_simple_kb())


@dp.message_handler(Text(equals='Назад'))
async def menu_bot(message: types.Message):
    await message.answer('МЕНЮ', reply_markup=get_simple_kb())


@dp.message_handler(Text(equals='Закрыть'))
async def menu_bot(message: types.Message):
    await message.answer('Меню закрыто', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals='Завтрак'))
async def menu_bot(message: types.Message):
    await message.answer('ЗАВТРАК:', reply_markup=get_simple_kb1())


@dp.message_handler(Text(equals='Обед'))
async def menu_bot(message: types.Message):
    await message.answer('ОБЕД', reply_markup=get_simple_kb2())


@dp.message_handler(Text(equals='Ужин'))
async def menu_bot(message: types.Message):
    await message.answer('УЖИН', reply_markup=get_simple_kb3())


@dp.message_handler(Text(equals='Назад😄'))
async def menu_bot(message: types.Message):
    await message.answer('Завтрак', reply_markup=get_simple_kb1())


@dp.message_handler(Text(equals='Назад😉'))
async def menu_bot(message: types.Message):
    await message.answer('Обед', reply_markup=get_simple_kb2())


@dp.message_handler(Text(equals='Назад😎'))
async def menu_bot(message: types.Message):
    await message.answer('Ужин', reply_markup=get_simple_kb3())


@dp.message_handler(Text(equals='Каша овсяная'))
async def menu_bot(message: types.Message):
    await message.answer('Цена', reply_markup=price_1())


@dp.message_handler(Text(equals='Чай с сахаром'))
async def menu_bot(message: types.Message):
    await message.answer('Цена', reply_markup=price_2())


@dp.message_handler(Text(equals='Батон'))
async def menu_bot(message: types.Message):
    await message.answer('Цена', reply_markup=price_3())


@dp.message_handler(Text(equals='Масло сливочное'))
async def menu_bot(message: types.Message):
    await message.answer('Цена', reply_markup=price_4())


@dp.message_handler(Text(equals='Винегрет овощной'))
async def menu_bot(message: types.Message):
    await message.answer('Цена', reply_markup=price_5())


@dp.message_handler(Text(equals='Рассольник домашний'))
async def menu_bot(message: types.Message):
    await message.answer('Цена', reply_markup=price_6())


@dp.message_handler(Text(equals='Рыба отварная'))
async def menu_bot(message: types.Message):
    await message.answer('Цена', reply_markup=price_7())


@dp.message_handler(Text(equals='Картофель отварной'))
async def menu_bot(message: types.Message):
    await message.answer('Цена', reply_markup=price_8())


@dp.message_handler(Text(equals='Сок персиковый'))
async def menu_bot(message: types.Message):
    await message.answer('Цена', reply_markup=price_9())


@dp.message_handler(Text(equals='Хлеб пшеничный'))
async def menu_bot(message: types.Message):
    await message.answer('Цена', reply_markup=price_10())


@dp.message_handler(Text(equals='Салат из свежей капусты'))
async def menu_bot(message: types.Message):
    await message.answer('Цена', reply_markup=price_11())


@dp.message_handler(Text(equals='Плов из свинины'))
async def menu_bot(message: types.Message):
    await message.answer('Цена', reply_markup=price_12())


@dp.message_handler(Text(equals='Чай'))
async def menu_bot(message: types.Message):
    await message.answer('Цена', reply_markup=price_13())


@dp.message_handler(Text(equals='Хлеб'))
async def menu_bot(message: types.Message):
    await message.answer('Цена', reply_markup=price_14())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
