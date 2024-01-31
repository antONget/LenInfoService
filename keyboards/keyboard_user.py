from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def menu_button():
    menu_btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    menu_btn.add(KeyboardButton("🚘 Заказ автозапчастей"), KeyboardButton("Заказ з/ч мото/вело/инструменты 🛠"))
    menu_btn.add(KeyboardButton("📞 Контакты"), KeyboardButton("Акции и скидки 🎁🔥"))
    return menu_btn


def get_base_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton('Назад'))
    return keyboard


def btn_from_vin():
    keybtn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keybtn.add(KeyboardButton('Да 👍'))
    keybtn.add(KeyboardButton('Нет 👎'))
    keybtn.add(KeyboardButton('Назад'))
    return keybtn


def keyboard_reply():
    button1 = InlineKeyboardButton(
        text='Все верно!',
        callback_data='done'
    )
    button2 = InlineKeyboardButton(
        text='Изменить',
        callback_data='change'
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[button1], [button2]]
    )
    return keyboard


def keyboard_reply_tools():
    button1 = InlineKeyboardButton(
        text='Все верно!',
        callback_data='done_tools'
    )
    button2 = InlineKeyboardButton(
        text='Изменить',
        callback_data='change_tools'
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[button1], [button2]]
    )
    return keyboard