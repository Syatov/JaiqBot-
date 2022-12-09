from aiogram.types import ReplyKeyboardMarkup , KeyboardButton


# Главное меню
btnInfo = KeyboardButton("📚Информация")
btnSs = KeyboardButton("🔮Другие соц.сети")
btnKurs = KeyboardButton("🔥Курсы")
mainMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnInfo,btnSs,btnKurs)


#другое меню
btnNazat = KeyboardButton("🔗Главное меню")
btnMoney = KeyboardButton("💰Цены")
btnK = KeyboardButton("💡Информация про курсы")
otherMenu = ReplyKeyboardMarkup(resize_keyboard= True).add(btnMoney,btnNazat,btnK)