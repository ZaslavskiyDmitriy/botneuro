from aiogram import types


button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='самокаты')
button3 = types.KeyboardButton(text='ты кто?')
button4 = types.KeyboardButton(text='Покажи котиков')
button5 = types.KeyboardButton(text='Закрыть')

keyboard1 = [
[button1, button2, button3],
[button4, button5],
]

keyboard2 = [
[ button4],
]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)