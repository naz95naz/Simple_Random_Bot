from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.fsm.state import default_state

import data
from keyboards.user_keyboards import start_markup, randomness_markup, back_markup


user_callback_router = Router()


@user_callback_router.callback_query(F.data == "randomness")
async def randomness(callback: CallbackQuery, state: FSMContext):
    await state.update_data(
        {"stored_data": data.user_datas[0]}
    )

    await callback.message.edit_text(
        text=data.randomness_SelectButton_text,
        reply_markup=randomness_markup
    )


@user_callback_router.callback_query(F.data == "back")
async def back(callback: CallbackQuery, state: FSMContext):
    stored_data = await state.get_data()

    if stored_data["stored_data"] == data.user_datas[0]:
        await callback.message.edit_text(
            text=data.start_text,
            reply_markup=start_markup
        )

    elif stored_data["stored_data"] == data.user_datas[1]:
        await state.update_data(
            {"stored_data": data.user_datas[0]}
        )
        await callback.message.edit_text(
            text=data.randomness_SelectButton_text,
            reply_markup=randomness_markup
        )

    await state.set_state(default_state)


@user_callback_router.callback_query(F.data == "random_number")
async def random_number_input(callback: CallbackQuery, state: FSMContext):
    await state.update_data(
        {"stored_data": data.user_datas[1]}
    )

    await callback.message.edit_text(
        text="Введіть діапазон у форматі:"
             "\n<pre>&lt;число1&gt; - &lt;число2&gt;</pre>",
        reply_markup=back_markup
    )