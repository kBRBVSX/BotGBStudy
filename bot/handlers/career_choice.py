from aiogram import types, Router, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from bot.keyboards.prof_keyboards import make_row_keyboard, EXIT_BUTTON

router = Router()


available_jobs = [
    "Программист",
    "Дизайнер",
    "Маркетолог"
]

available_grades = ['Junior', 'Middle', 'Senior']

class ChoiceProfile(StatesGroup):
    job = State()
    grade = State()

@router.message(Command("prof"))
@router.message(F.text == "Профессии")
async def command_prof(message: types.Message, state: FSMContext):
    await message.answer(
        text="Выберите профессию",
        reply_markup=make_row_keyboard(available_jobs))
    await state.set_state(ChoiceProfile.job)


@router.message(ChoiceProfile.job)
async def prof_choice(message: types.Message, state: FSMContext):
    if message.text == EXIT_BUTTON:
        await state.clear()
        await message.answer("Вы вышли из процесса выбора. До свидания!", reply_markup=types.ReplyKeyboardRemove())
        return

    if message.text not in available_jobs:
        await message.answer("Пожалуйста, выберите профессию из предложенных вариантов или нажмите 'Выйти'.")
        return

    await state.update_data(chosen_job=message.text)
    await state.set_state(ChoiceProfile.grade)
    await message.answer("Теперь выберите грейд", reply_markup=make_row_keyboard(available_grades))


@router.message(ChoiceProfile.grade)
async def grade_choice(message: types.Message, state: FSMContext):
    if message.text == EXIT_BUTTON:
        await state.clear()
        await message.answer("Вы вышли из процесса выбора. До свидания!", reply_markup=types.ReplyKeyboardRemove())
        return

    if message.text not in available_grades:
        await message.answer("Пожалуйста, выберите грейд из предложенных вариантов или нажмите 'Выйти'.")
        return

    user_data = await state.get_data()
    chosen_job = user_data.get("chosen_job")
    chosen_grade = message.text

    await message.answer(
        f"Ваша профессия: {chosen_job}\nВаш грейд: {chosen_grade}",
        reply_markup=types.ReplyKeyboardRemove()
    )
    await state.clear()


@router.message(ChoiceProfile.job)
async def initial_prof_choice(message: types.Message):
    await message.answer(
        text="Выберите профессию",
        reply_markup=make_row_keyboard(available_jobs)
    )