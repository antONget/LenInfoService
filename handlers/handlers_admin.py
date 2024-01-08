from aiogram import types

@dp.message_handler(state=AddForm.add)
async def add_admins(message: types.Message, state: FSMContext):
    if message.text == "/start":
        await state.finish()
        return await start_message(message)
    elif message.text == "/menu":
        await state.finish()
        return await menu(message)
    telegram_id = message.text
    user = get_telegram_user(telegram_id, Tokens.bot_token)
    if 'result' in user:
        print(f'User with ID {telegram_id} exists.')
        conn = sqlite3.connect('mag.db')
        cursor = conn.cursor()

        # Добавление Telegram ID в базу данных
        cursor.execute('INSERT INTO admins (telegram_id) VALUES (?)', (telegram_id,))

        # Сохранение изменений и закрытие соединения
        conn.commit()
        conn.close()

        # Отправка сообщения об успешном добавлении
        await message.answer(f"Telegram ID {telegram_id} успешно добавлен в базу данных!")
        await state.finish()
    else:
        await message.answer(f"Telegram ID {telegram_id} не существует! Попробуйте еще раз!")
        await AddForm.add.set()