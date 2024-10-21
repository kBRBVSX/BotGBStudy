from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

EXIT_BUTTON = "Выйти"

def make_row_keyboard(buttons: list[str], add_exit: bool = True) -> ReplyKeyboardMarkup:
    row = [KeyboardButton(text=button) for button in buttons]
    if add_exit:
        row.append(KeyboardButton(text=EXIT_BUTTON))
    return ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)