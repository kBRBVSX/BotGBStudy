from aiogram import types, F, Router
from aiogram.filters.command import Command
from bot.keyboards.keyboards import kb1
from bot.utils.random_fox import fox

router = Router()


# Обработчик команды /start или текста "Старт"
@router.message(Command("start"))
@router.message(F.text == "Старт")
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Привет {name}! Я простой Telegram бот.", reply_markup=kb1)


# Обработчик команды /stop или текста "Стоп"
@router.message(Command("stop"))
@router.message(F.text == "Стоп")
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f"Пока, {name}!", reply_markup=kb1)


# Обработчик команды /fox или текста "Покажи лису"
@router.message(Command("fox"))
@router.message(Command("лиса"))
@router.message(F.text.lower() == "покажи лису")
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f"Держи лису, {name}!")
    await message.answer_photo(photo=img_fox)


# Обработчик текстовых сообщений (эхо)
@router.message()
async def echo(message: types.Message):
    name = message.chat.first_name
    text = message.text.lower()

    greetings = ["привет", "прива", "здарова", "hi", "ку", "здравствуй", "добрый день", "доброе утро", "добрый вечер",
                 "салют", "хай", "приветствую"]
    if text in greetings:
        await message.answer(f"Привет, {name}!")
        return

    exceptions = ["пока", "бб", "до свидания", "увидимся", "всего хорошего", "спокойной ночи", "до встречи", "прощай",
                  "до скорого", "до скорой встречи", "всего доброго", "всего наилучшего"]
    if text in exceptions:
        await message.answer(f"Пока, {name}!")
        return
    elif text == "стоп":
        await message.answer("Бот остановлен.", reply_markup=types.ReplyKeyboardRemove())
    elif text == "инфо":
        await message.answer("Это простой бот для демонстрации работы с клавиатурой.")
    elif text == "ты кто?" or text == "ты кто":
        await message.answer_dice(emoji="🎯")
    elif text == "закрыть":
        await message.answer("Клавиатура скрыта.", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer(f"Вы сказали: {message.text}")
