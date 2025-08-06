import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message , CallbackQuery
import time
from googletrans import Translator
translator = Translator()
import app.inline as b
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


class Tarjima(StatesGroup):
    eng =State()
    rus = State()
    japan = State()



TOKEN = "6990681753:AAGKY2DjwI8hWyRX9s5l3L_8odPsEuA0MwQ"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer_photo(photo='https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Google_Translate_logo.svg/800px-Google_Translate_logo.svg.png',
                                    caption="🌐Google transga hush kelibsiz!‼️‼️ \n \n ADMIN: <B>@ahrorbeek007</b>🌐",
                                    reply_markup=b.inline_btns)
    
@dp.callback_query(F.data == 'rus')
async def rus(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('✔Matnni kiriting:')
    await state.set_state(Tarjima.rus)

@dp.message(Tarjima.rus)
async def rus1(messege: CallbackQuery, state: FSMContext):
    matn = translator.translate(messege.text, dest='ru',src='uz').text
    await messege.answer(f'<b>⚜️Tarjima</b>: <i>{matn}</i>')


@dp.callback_query(F.data == 'eng')
async def rus(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('✔Matnni kiriting:')
    await state.set_state(Tarjima.eng)

@dp.message(Tarjima.eng)
async def rus1(messege: CallbackQuery, state: FSMContext):
    matn = translator.translate(messege.text, dest='en',src='uz').text
    await messege.answer(f'<b>⚜️Tarjima</b>: <i>{matn}</i>')

@dp.callback_query(F.data == 'japan')
async def rus(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer('✔Matnni kiriting:')
    await state.set_state(Tarjima.japan)

@dp.message(Tarjima.japan)
async def rus1(messege: CallbackQuery, state: FSMContext):
    matn = translator.translate(messege.text, dest='ja',src='uz').text
    await messege.answer(f'<b>⚜️Tarjima</b>: <i>{matn}</i>')




async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


#pip install googletrans==3.1.0a0
