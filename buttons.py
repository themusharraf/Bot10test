from aiogram import types

kb = [
    [types.KeyboardButton(text="🗂 Categories"), types.KeyboardButton(text="📝 Ask questions")],
    [types.KeyboardButton(text="⚙️ Settings")],
]
keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

choise = [
    [types.KeyboardButton(text="Nordik-3"), types.KeyboardButton(text="Tonxeym")],
    [types.KeyboardButton(text="Oklend"), types.KeyboardButton(text="Klaum")],
    [types.KeyboardButton(text="Simona"), types.KeyboardButton(text="Stella")],
    [types.KeyboardButton(text="↩️ back")],

]
choises = types.ReplyKeyboardMarkup(keyboard=choise, resize_keyboard=True)
