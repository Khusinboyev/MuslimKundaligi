from aiogram.dispatcher import FSMContext
from aiogram import types
import datetime
from aiogram.types import ContentType
from aiogram.utils.exceptions import *
from sqlite3 import connect
import asyncio
from aiogram.utils import exceptions
import sqlite3
from key import bot, dp
from keyboards.default.admin_keyfunctions import *
from database.From import *

boshAdmin = '1918760732'

class functions:

	@staticmethod
	async def channel_adder(id):
		with connect('./database/database.sqlite3') as db:
			cursor = db.cursor()
			cursor.execute("""CREATE TABLE IF NOT EXISTS channels(id)""")
			db.commit()

			cursor.execute("INSERT INTO channels VALUES(?);", id)
			db.commit()

	@staticmethod
	async def channel_remover(id):
		with connect('./database/database.sqlite3') as db:
			cursor  = db.cursor()
			cursor.execute(f'DELETE FROM channels WHERE id = "{id}"')
			db.commit()

	@staticmethod
	async def channel_generator():
		with connect('./database/database.sqlite3')as db:
			cursor = db.cursor()
			cursor.execute("SELECT id from channels ")
			str = ''
			for row in cursor.fetchall():
				id = row[0]
				all_details = await bot.get_chat(id)
				title = all_details["title"]
				channel_id = all_details["id"]
				info = all_details["description"]
				str += f"-----------------------------------------\nKanal useri:   {id} \nKanal nomi:   {title} \nKanal id si:   {channel_id} \nKanal haqida:   {info} \n -----------------------------------------"
			return str


async def send_message_chats(chat_id: int, from_chat_id: int, message_id: int, reply_markup) -> bool:
	try:
		await dp.bot.copy_message(chat_id=chat_id, from_chat_id=from_chat_id, message_id=message_id, reply_markup=reply_markup)
	except exceptions.BotBlocked:
		pass
	except exceptions.ChatNotFound:
		pass
	except exceptions.UserDeactivated:
		pass
	except exceptions.TelegramAPIError:
		pass
	else:
		return True
	return False

@dp.message_handler(commands='panel', user_id=boshAdmin)
async def panel(message: types.Message):
	Markup = await main_menu()
	await message.answer('salom admin', reply_markup=Markup)


@dp.message_handler(lambda message: message.text == '🔙 Orqaga qaytish', state=Form.all_states, user_id=boshAdmin)
async def back_state(message: types.Message, state: FSMContext):
	Markup = await main_menu()
	await message.answer('Orqaga qaytdingiz', reply_markup=Markup)
	await state.finish()


@dp.message_handler(lambda message: message.text == '🔙 Orqaga qaytish', user_id=boshAdmin)
async def back(message: types.Message, state: FSMContext):
	Markup = await main_menu()
	await message.answer('Orqaga qaytdingiz', reply_markup=Markup)
	await state.finish()


@dp.message_handler(text="📊 statistika", user_id=boshAdmin)
async def statistics(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
	markup.add("📊 statistika")
	markup.add('🔙 Orqaga qaytish')
	date = datetime.date.today()
	connect = sqlite3.connect('./database/database.sqlite3')
	cursor = connect.cursor()
	cursor.execute("SELECT COUNT(*) FROM users")
	followers = cursor.fetchone()[0]
	cursor.execute(f"SELECT COUNT(*) FROM users WHERE date='{date}' ")
	today_joined = cursor.fetchone()[0]
	cursor.execute(f"SELECT COUNT(*) FROM users WHERE date='{date - datetime.timedelta(days=1)}' ")
	yesterday_joined = cursor.fetchone()[0]

	await message.answer(f"📊 Statistika\n"
						 "\n"
						 f"🗓  Botga bugun qo'shilganlar soni: {today_joined}\n"
						 f"🌙  Botga kecha qo'shilganlar soni: {yesterday_joined}\n"


						 f"🫂 Botdagi jami foydalanuvchilar soni:  {followers}\n"
						 '\n')


@dp.message_handler(lambda message: message.text == "📌 Kanallar", user_id=boshAdmin)
async def channels(message: types.Message):
	markup = await channels_btn()
	await message.answer(text='Menyudan tanlang', reply_markup=markup)
	await Form.channel.set()


@dp.message_handler(lambda message: message.text == "➕   Kanal qo`shish", state=Form.channel, user_id=boshAdmin)
async def channel_add1(message: types.Message):
	markup = await back_btn()
	await message.answer('Kanal Userini @chanel_id formatida kiritng', reply_markup=markup)
	await Form.channel_add2.set()


@dp.message_handler(state=Form.channel_add2, user_id=boshAdmin)
async def channel_add2(message: types.Message, state: FSMContext):
	with sqlite3.connect('./database/database.sqlite3') as db:
		cursor = db.cursor()
		channel_id = [message.text.upper()]
		data = cursor.execute(f"SELECT id FROM channels WHERE id = '{message.text.upper()}'").fetchone()
		if data is None:
			if message.text[0] == '@':
				await functions.channel_adder(channel_id)
				await state.finish()
				await message.answer("kanal muvvafaqiyatli qo`shildi")
			else:
				await message.answer('Channel ID xato kiritildi \n'
									 'Iltimos to`g`ri Channel ID kiriting')
		else:
			await message.answer('Bu kanal avvaldan kannallar  ro`yhatiga qo`shilgan')


@dp.message_handler(lambda message: message.text == "🚫  Kanal olib tashlash", user_id=boshAdmin)
async def channel_remove1(message: types.Message):
	markup = await back_btn()
	await message.answer('Kanal Userini @chanel_id formatida kiritng', reply_markup=markup)
	await Form.ChannelRemove.set()

@dp.message_handler(state=Form.ChannelRemove, user_id=boshAdmin)
async def channel_remove2(message: types.Message):
	markup = await back_btn()
	with sqlite3.connect('./database/database.sqlite3') as db:
		cursor = db.cursor()
		data = cursor.execute(f"SELECT id FROM channels WHERE id = '{message.text.upper()}'").fetchone()
		if data != None:
			await functions.channel_remover(message.text.upper())
			await message.answer('o`chirildi', reply_markup=markup)
		else:
			await message.answer("Bunday kanal yo`q")


@dp.message_handler(lambda message: message.text == "📜 Kanallar ro'yhati", state=Form.channel, user_id=boshAdmin)
async def channels_list(message: types.Message, state: FSMContext):
	if len(await functions.channel_generator())>9:
		await state.finish()
		await message.answer(await functions.channel_generator())
	else:
		await message.answer('kanallar yo`q')


@dp.message_handler(lambda message: message.text == '✍️ Xabar yuborish', user_id=boshAdmin)
async def send_message(message: types.Message):
	Markup = await send_message_btn()
	await message.answer("Menyudan tanlang", reply_markup=Markup)


@dp.message_handler(lambda message: message.text == 'Bitta foydalanuvchiga yuborish', user_id=boshAdmin)
async def one_user(message: types.Message):
	await message.answer("Yuborilishi kerak bo'lgan odamning ID sini yuboring")
	await Form.OneUser.set()


@dp.message_handler(state=Form.OneUser, user_id=boshAdmin)
async def one_user(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['OneUser'] = message.text
	await message.answer("Yuborilishi kerak bo'lgan xabarni yuboring")
	await Form.OneUser2.set()


@dp.message_handler(state=Form.OneUser2, content_types=ContentType.ANY, user_id=boshAdmin)
async def one_user(message: types.Message, state: FSMContext):
	Markup = await main_menu()
	async with state.proxy() as data:
		id = data['OneUser']
	await bot.copy_message(from_chat_id=message.chat.id, chat_id=id, message_id=message.message_id)
	await message.answer("Xabar yuborildi", reply_markup=Markup)
	await state.finish()


@dp.message_handler(lambda message: message.text == 'Birnechta foydalanuchilarga yuborish', user_id=boshAdmin)
async def send_many(message: types.Message):
	markup = await back_btn()
	await message.answer("Qancha odamga yuborilishi kerak ekanligini kiriting", reply_markup=markup)
	await Form.ManyUser.set()


@dp.message_handler(state=Form.ManyUser, user_id=boshAdmin)
async def send_many2(message: types.Message, state: FSMContext):
	markup = await back_btn()
	async with state.proxy() as data:
		data['ManyUser'] = message.text
	await message.answer("Yuborilishi kerak bo'lgan xabarni kiriting", reply_markup=markup)
	await Form.ManyUser2.set()


@dp.message_handler(state=Form.ManyUser2, content_types=ContentType.ANY, user_id=boshAdmin)
async def send_many2(message: types.Message, state: FSMContext):
	await state.finish()
	async with state.proxy() as data:
		amount = data['ManyUser']
	connect = sqlite3.connect('./database/database.sqlite3')
	cursor = connect.cursor()
	rows = cursor.execute(f"SELECT user_id FROM users ").fetchall()
	list = []
	for row in rows:
		list.append(row[0])
	for i in range(int(amount)):
		await send_message_chats(chat_id=list[i], from_chat_id=message.chat.id, message_id=message.message_id,
								 reply_markup=message.reply_markup)
	await message.answer("Xabar yuborish yakunlandi")


@dp.message_handler(lambda message: message.text == "Barcha foydalanuchilarga yuborish", user_id=boshAdmin)
async def all_users(message: types.Message, state: FSMContext):
	markup = await back_btn()
	await message.answer("Yuborilishi kerak bo'lgan xabarni yuboring", reply_markup=markup)
	await Form.AllUsers.set()


@dp.message_handler(state=Form.AllUsers, content_types=ContentType.ANY, user_id=boshAdmin)
async def all_users2(message: types.Message, state: FSMContext):
	await state.finish()
	Markup = await main_menu()
	connect = sqlite3.connect('./database/database.sqlite3')
	cursor = connect.cursor()
	rows = cursor.execute(f"SELECT user_id FROM users ").fetchall()
	for row in rows:
		id = row[0]
		await send_message_chats(from_chat_id=message.chat.id, message_id=message.message_id, chat_id=id,
								 reply_markup=message.reply_markup)

	await message.answer("Xabar yuborish yakunlandi", reply_markup=Markup)


@dp.message_handler(lambda message: message.text == '♻️ Tozalash', user_id=boshAdmin)
async def clear(message: types.Message):
	try:

		Markup = await back_btn()
		await message.answer("Tozalash uchun xavfizlik kodini kiriting 🔑", reply_markup=Markup)
		await Form.ClearState.set()
	except:
		pass


@dp.message_handler(state=Form.ClearState, user_id=boshAdmin)
async def clear2(message: types.Message, state: FSMContext):
	if message.text == '0000':

		markup = await main_menu()
		connect = sqlite3.connect('./database/database.sqlite3')
		cursor = connect.cursor()
		cursor.execute("SELECT COUNT(*) FROM users")
		followers = cursor.fetchone()[0]
		check_time = followers / 60 / 10
		text = 'Tozalash boshlandi\nTozalash tozalash {:.2f} daqiqa vaqt oladi va {} ta foydalanuvchi tekshiriladi\n❗️ Tozalash yakunlanmagunicha iltimos botning adminpanelidan foydalanmang '
		text = text.format(check_time, followers)
		await message.answer(text)
		rows = cursor.execute(f"SELECT user_id FROM users ").fetchall()
		for row in rows:
			id = row[0]
			try:
				await bot.send_message(chat_id=id, text="Biz bilan qolganingiz uchun rahmat 🎉")
			except BotBlocked:
				cursor.execute(f"DELETE FROM users WHERE user_id = '{id}'")
				connect.commit()
			except ChatNotFound:
				cursor.execute(f"DELETE FROM users WHERE user_id = '{id}'")
				connect.commit()
			except RetryAfter as e:
				await asyncio.sleep(e.timeout)
			except UserDeactivated:
				cursor.execute(f"DELETE FROM users WHERE user_id = '{id}'")
				connect.commit()
			except MigrateToChat:
				cursor.execute(f"DELETE FROM users WHERE user_id = '{id}'")
				connect.commit()
			except TelegramAPIError:
				cursor.execute(f"DELETE FROM users WHERE user_id = '{id}'")
				connect.commit()
		await message.answer("Tozalash yakunlandi  ✅", reply_markup=markup)
		await state.finish()
	else:
		Markup = await back_btn()
		await message.answer("Xavfsizlik kodi noto'g'ri. Qaytadan urunub ko'ring", reply_markup=Markup)



@dp.message_handler(is_reply=True, user_id=boshAdmin)
async def connect_repl(message: types.Message, state: FSMContext):
	try:
		await bot.copy_message(from_chat_id=message.chat.id, chat_id=message.reply_to_message.forward_from.id,
							   message_id=message.message_id)
	except UserDeactivated:
		pass
	except BotBlocked:
		pass
	except ChatNotFound:
		pass
