import logging
from aiogram import Bot , Dispatcher ,executor , types
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
import random
import markups as nav
import datetime
from datetime import date
x = datetime.datetime.now()
x1 = x.strftime("%u")
m = x.strftime("%M")
h = x.strftime("%H")
print(x)
print(x1)

TOKEN = ""

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}'.format(message.from_user), reply_markup= nav.mainMenu)

@dp.message_handler()
async def command_start(message: types.Message):
    if message.text == "🔗Главное меню":
        await bot.send_message(message.from_user.id,"🔗Главное меню" ,reply_markup= nav.mainMenu)
    elif message.text == "🔮Другие соц.сети":
        await bot.send_message(message.from_user.id, "instagram - https://www.instagram.com/jaiqschool/\ntiktok - https://www.tiktok.com/@jaiq.school?lang=ru-RU\n telegram - https://t.me/jaiqschool")
    elif message.text == "📚Информация":
        await bot.send_message(message.from_user.id, "JaiqSchool - это школа програмирования и роботатехники")
    elif message.text == "🔥Курсы":
        await bot.send_message(message.from_user.id,reply_markup= nav.otherMenu)
    elif message.text == "💰Цены":
        await bot.send_message(message.from_user.id, "Курс работатехники - цена\nКурс програмирования - цена\nКурс веб дизайна - цена")
    elif message.text == "SyatovAmir11":
        await bot.send_message(message.from_user.id, "")
    elif x1 == 5 and h == 15 and m == 30:
         await bot.send_message(message.from_user.id, "через 2 с половиной часа муви тайм")
    else :
        await message.reply("Неизвестная команда")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
