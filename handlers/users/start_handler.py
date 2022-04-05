from aiogram import types
from datetime import datetime
import pytz
import sqlite3
from key import dp, bot
from keyboards.inline.buttons import *
from sqlite3 import connect
from keyboards.buttons import *


class functions:
	@staticmethod
	async def check_on_start(user_id):
		with connect('./database/database.sqlite3') as db:
			cursor = db.cursor()
			rows = cursor.execute("SELECT id from channels ").fetchall()
			error_code = 0
			for row in rows:
				r = await bot.get_chat_member(chat_id=row[0], user_id=user_id)
				if r.status in ['member', 'creator', 'admin']:
					pass
				else:
					error_code = 1
		if error_code == 0:
			return True
		else:
			return False


@dp.message_handler(commands=['start'])
async def welcom(message:types.Message):
	connect = sqlite3.connect('./database/database.sqlite3')
	cursor = connect.cursor()
	cursor.execute(
		"""CREATE TABLE IF NOT EXISTS users ("key"  INTEGER,"user_id"  INTEGER,"date"  INTEGER);""")
	if cursor.execute(f"""SELECT user_id FROM users WHERE user_id = {message.chat.id}""").fetchone() == None:
		sana = datetime.now(pytz.timezone('Asia/Tashkent')).strftime('%d-%m-%Y %H:%M')
		cursor.execute(
			"INSERT INTO users (user_id, date) VALUES ('{user_id}', '{sana}')".format(user_id=message.chat.id,
			                                                                          sana=sana))
		connect.commit()

	db = sqlite3.connect('./database/choos.sqlite3')
	sql = db.cursor()
	sql.execute("""CREATE TABLE IF NOT EXISTS users ("user_id"  INTEGER,"region"  INTEGER);""")
	db.commit()

	if await functions.check_on_start(message.chat.id):
		audios = ["CQACAgIAAxkBAAIDi2JK_EbV_zl-ZA82dq0c6Gbzq2uvAAKNFAACab3ZSLZqQVPVHfD0IwQ", "CQACAgIAAxkBAAIC-mJK6PTghc05OcL9oxqR_pzk5pJXAAJ9EwACdj5xSu4PQ2Ub_T-uIwQ"]
		for audio in audios:
			await message.reply_audio(audio=audio, caption=f'Assalomu alaykum 👋 <b>{message.from_user.first_name}</b>\n\nBoshlanishidan Nashid bilan boshlamoqlikni niyyat qildik.\n\n\nAllohning o`zi hammamizdan rozi bo`lsin', reply_markup=main_btn)
	else:
		await message.reply(f'Assalomu alaykum {message.from_user.first_name}\nBotimizdan foydalanish uchun kanalimizga azo bo`ing👇👇', reply_markup=join_inline)

@dp.callback_query_handler(text='check')
async def check(call):
	if await functions.check_on_start(call.message.chat.id ):
		await call.message.reply_audio(audio="CQACAgIAAxkBAAIC-mJK6PTghc05OcL9oxqR_pzk5pJXAAJ9EwACdj5xSu4PQ2Ub_T-uIwQ", caption=f'Assalomu alaykum 👋 <b>{call.message.from_user.first_name}</b>\n\nBoshlanishidan Nashid bilan boshlamoqlikni niyyat qildik.\n\n\nAllohning o`zi hammamizdan rozi bo`lsin', reply_markup=main_btn)
	else:
		await call.message.reply(f'Assalomu alaykum {call.message.from_user.first_name}\nBotimizdan foydalanish uchun kanalimizga azo bo`ing👇👇', reply_markup = join_inline)


# @dp.message_handler(text='🔁 Tekshirish')
# async def welcom(message:types.Message):
# 	if await functions.check_on_start(message.chat.id):
# 		await bot.send_message(message.chat.id, 'Botimizdan foydalanishingiz mumkin👇', reply_markup=main_btn)
# 	else:
# 		await message.reply(f'Assalomu alaykum {message.from_user.first_name}\nRamazon taqvimi botimizga xush kelibsiz\nBotimizdan foydalanish uchun kanalimizga azo bo`ing👇👇\n\n<b>@Nurun_ala</b>', reply_markup=join_btn)
