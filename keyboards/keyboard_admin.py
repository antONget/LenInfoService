from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def adminBtn():
    admin_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    admin_button.add(KeyboardButton('Добавить'))
    admin_button.add(KeyboardButton('Удалить'))
    admin_button.add(KeyboardButton('Удалить все акции и скидки'))
    return admin_button


def adminBtn_plus():
    admin_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    admin_button.add(KeyboardButton('Добавить'))
    admin_button.add(KeyboardButton('Удалить'))
    admin_button.add(KeyboardButton('Удалить все акции и скидки'))
    admin_button.add(KeyboardButton('Добавить админа'))
    return admin_button

def confirm_keyboard(promo_id):
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("Да, удалить", callback_data=f"confirm_delete:{promo_id}"),
        InlineKeyboardButton("Отмена", callback_data="cancel_delete")
    )