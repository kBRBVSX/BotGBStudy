from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создаем кнопки
button1 = KeyboardButton(text="Старт")
button2 = KeyboardButton(text="Стоп")
button3 = KeyboardButton(text="Инфо")
button4 = KeyboardButton(text="Покажи лису")
button5 = KeyboardButton(text="Закрыть")
button6 = KeyboardButton(text="Профессии")

# Создаем клавиатуру и добавляем в нее кнопки
kb1 = ReplyKeyboardMarkup(
    keyboard=[[button1, button2, button3], [button4, button5, button6]],
    resize_keyboard=True
)