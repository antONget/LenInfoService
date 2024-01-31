import sqlite3
from aiogram.types import Message


# можно использовать memory: вместо названия файла, чтобы хранить данные в оперативной памяти
db = sqlite3.connect('mag.db', check_same_thread=False)
sql = db.cursor()


def create_table_admins():
    sql.execute("""CREATE TABLE IF NOT EXISTS admins(
        id INTEGER PRIMARY KEY,
        telegram_id INTEGER
    )""")
    db.commit()


def create_table_sales():
    sql.execute("""CREATE TABLE IF NOT EXISTS admins(
        id INTEGER PRIMARY KEY,
        desc TEXT,
        imj BLOB,
        shdesc TEXT
    )""")
    db.commit()


def table_auto():
    sql.execute("""CREATE TABLE IF NOT EXISTS order_auto(
        id INTEGER PRIMARY KEY,
        user_id TEXT,
        username TEXT,
        phone TEXT,
        vin TEXT,
        car TEXT,
        list_tools TEXT
    )""")
    db.commit()


def table_tools():
    sql.execute("""CREATE TABLE IF NOT EXISTS order_tools(
        id INTEGER PRIMARY KEY,
        user_id TEXT,
        username TEXT,
        phone TEXT,
        type_tool TEXT,
        model_tool TEXT,
        list_tools TEXT
    )""")
    db.commit()


def add_id_auto(message: Message):
    # sql.execute("SELECT id FROM order_auto WHERE id = ?", (message.chat.id,))
    sql.execute(f"INSERT INTO order_auto (user_id, username, phone, vin, car, list_tools)"
                f" VALUES({message.chat.id}, 'name', 'phone', 'vin', 'car', 'list_tools')")
    db.commit()


def add_id_tool(message: Message):
    # sql.execute("SELECT id FROM order_tools WHERE id = ?", (message.chat.id,))
    sql.execute(f"INSERT INTO order_tools (user_id, username, phone, type_tool, model_tool, list_tools)"
                f" VALUES({message.chat.id}, 'name', 'phone', 'type_tool', 'model_tool', 'list_tools')")
    db.commit()


def update_table_field(message: Message, table, field, set_field):
    sql.execute(f"UPDATE {table} SET {field} = ? WHERE user_id = ? AND id=(SELECT MAX(id) FROM {table})",
                (set_field, message.chat.id,))
    db.commit()


# def update_table(message: Message, table, field, set_field):
#     sql.execute(f"UPDATE {table} SET {field} = ? WHERE {message.chat.id} = ? AND id=(SELECT MAX(id) FROM {table})",
#                 (message.text.replace('\n', ' '),
#                  message.chat.id))
#     db.commit()





def update_phone(message: Message, table):
    print(type(message.text))
    if message.contact is not None:
        phone = message.contact.phone_number
    else:
        phone = message.text
    sql.execute(f"UPDATE {table} SET phone = ? WHERE user_id = ? AND id=(SELECT MAX(id) FROM {table})",
                (phone,
                 message.chat.id))
    db.commit()


chat_id = 5443784834


def select_row(message, table):
    return sql.execute(f"SELECT * FROM {table} WHERE user_id = ?",
                        (message.chat.id,)).fetchall()[-1]


if __name__ == '__main__':
    db = sqlite3.connect('/Users/antonponomarev/PycharmProjects/LenService/mag.db', check_same_thread=False)
    sql = db.cursor()
    sql.execute('DROP TABLE order_auto')
