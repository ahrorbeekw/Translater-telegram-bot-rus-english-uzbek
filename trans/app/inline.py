from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

inline_btns = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Rus',callback_data='rus'), InlineKeyboardButton(text='Eng',callback_data='eng'), InlineKeyboardButton(text='Japan',callback_data='japan') ]
])



btns = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Rus tili')],
    [KeyboardButton(text='/start')]
],resize_keyboard=True,
input_field_placeholder='See')