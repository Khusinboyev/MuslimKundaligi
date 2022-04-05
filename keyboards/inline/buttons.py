import sqlite3
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

db = sqlite3.connect('D://update/Muslim kundaligi/database/database.sqlite3')
sql = db.cursor()
checks = sql.execute("SELECT id FROM channels ").fetchall()
sql.execute(f"SELECT id FROM  channels")
check = sql.fetchall()
join_inline = InlineKeyboardMarkup(row_width=2)
join_inline.add(InlineKeyboardButton("Kanalga o`tish", url=f"https://t.me/{check[0][0][1::]}"))
join_inline.add(InlineKeyboardButton("🔁 Tekshirish", callback_data='check'))

# join_inline = InlineKeyboardMarkup(row_width=2)
# join_inline.add(InlineKeyboardButton("Kanalga o`tish", url=f"https://t.me/{check}"))
# join_inline.add(InlineKeyboardButton("🔁 Tekshirish", callback_data='check'))
