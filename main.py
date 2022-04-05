from aiogram import *
from handlers.users.start_handler import *
from handlers.admin.admin_handlers import *
from key import bot, dp
from keyboards.buttons import *
from aiogram.types import *
import requests
from bs4 import BeautifulSoup
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import datetime
db = sqlite3.connect('./database/choos.sqlite3')
sql = db.cursor()
regions = {'Andijon':1, 'Fargona':37, 'Namangan' : 15, 'Toshkent' : 27, 'Sirdaryo' : 5, 'Samarqand' : 18, 'Qashqadaryo' : 25, 'Surxondaryo' : 74, 'Navoiy' : 14, 'Buxoro' : 4, 'Jizzax' : 9, 'Xorazm' : 78, 'Qoroqolpoq' : 16}


@dp.message_handler(text = "📖Quron, to'liq holda")
async def quran(msg: types.Message):
	audios = ["CQACAgIAAxkBAAIGuWJMSICXi-xeY5GMZzZKPId1dy3IAAJHFgACo6wISraX5pRUzC4lIwQ", "CQACAgIAAxkBAAIGumJMSICtVkFk2A2RIrGcgRF7r_SEAAJyGAACLcAoSo-FWc3RSEJ6IwQ"]
	for audio in audios:
		await msg.reply_audio(audio=audio, caption="Assalomu alaykum va roxmatullohi va barakatixi.\n\nQuronni to'liq holda tinglashingiz mumkin\n\n\nBotni Hudo hohlasa tez orada mukammalroq qilib yasaymiz")


@dp.message_handler(text = "Adminga murojaat")
async def quran(msg: types.Message):
	await msg.reply("Admin bilan bog'lanish uchun : @coder_dmin")

@dp.message_handler(text='↩️ Orqaga qaytish')
async def back(message: types.Message):
	await message.reply('Orqaga qaytdingiz', reply_markup=main_btn)

@dp.message_handler(text='🔙️ Orqaga qaytish')
async def back(message: types.Message):
	await message.reply('Orqaga qaytdingiz', reply_markup=calendars)

@dp.message_handler(text = '📆 Taqvimlar')
async def province(message: types.Message):
	await message.reply('Tanlang', reply_markup=calendars)

"""""###################### Ramazon taqvimi"""""

@dp.message_handler(text = '📆 Ramazon taqvimi')
async def ramadan(message: types.Message):
	await message.reply('Tanlang', reply_markup=RaTimes)

@dp.message_handler(text = '⏰ Vaqtni bilish')
async def ramadan(message: types.Message):
	send = await message.answer('⏳')
	user_id = message.from_user.id
	check = sql.execute("SELECT region FROM users WHERE user_id = ?", (user_id,)).fetchone()
	reg = sql.execute("SELECT region FROM users WHERE user_id = ?", (user_id,)).fetchone()[0]
	reg1 = regions[reg]
	html_text = requests.get(f'https://islom.uz/region/{reg1}').text
	soup = BeautifulSoup(html_text, 'lxml')
	times = soup.find('div', class_='in_header_p')
	bomdod = times.find('div', id = 'tc1').text
	shom = times.find('div', id='tc5').text
	reg = sql.execute("SELECT region FROM users WHERE user_id = ?", (user_id,)).fetchone()[0]
	img = Image.open('pic/img.png')
	id = message.from_user.id
	day = datetime.datetime.today().day
	myFont = ImageFont.truetype('mono.ttf', 48)
	I1 = ImageDraw.Draw(img)
	I1.text((50, 50), f"{day - 1}-Ramazon", font=myFont, fill=(255, 0, 0))
	I1.text((50, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
	I1.text((10, 200), f"Saxarlik : {bomdod}", font=myFont, fill=(255, 0, 0))
	I1.text((10, 300), f"Iftorlik    : {shom}", font=myFont, fill=(255, 0, 0))
	I1.text((280, 380), f"{reg} vaqti", font=ImageFont.truetype('mono.ttf', 26), fill=(255, 0, 0))
	I1.text((180, 450), "@Muslim_kundaligi_robot", font=ImageFont.truetype('mono.ttf', 20), fill=(255, 0, 0))
	img.save(f"pic/{id}.png")
	if not check:
		await message.reply('Viloyatingizni tanlang', reply_markup=provinces)
	else:
		await message.reply_photo(photo=open(f'pic/{id}.png', 'rb'), caption=f"<b>{reg} vaqti</b>\n\nSaxarlik > {bomdod}\nIftorlik > {shom}", reply_markup=RaTimes)
	await bot.delete_message(chat_id=message.chat.id, message_id=send.message_id)

@dp.message_handler(text = '⏳ Oylik taqvim')
async def ramadan(message: types.Message):
	await message.reply("Bu yerdan oylik taqvimlarni ko`rib olishiz mumkin:  https://islom.uz/vaqtlar/27/4", reply_markup=RaTimes)

@dp.message_handler(text = "📿 O'qiadigan duolar")
async def ramadan(message: types.Message):
	await message.reply(""" 🤲САҲАРЛИК (ОҒИЗ ЁПИШ) ДУОСИ
- - - - - - - - - - - - - - - - - -
  Навайту ан асума совма шаҳри Рамазона минал фажри илал мағриби, холисан лиллаҳи таъалаа. Аллоҳу акбар.
- - - - - - - - - - - - - - - - - -
  Маъноси: Рамазон ойининг рўзасини субҳдан то кун ботгунича холис Аллоҳ таоло учун тутишни ният қилдим. Аллоҳу акбар.\n\n\n🤲ИФТОРЛИК (ОҒИЗ ОЧИШ) ДУОСИ
- - - - - - - - - - - - - - - - - -
 Аллоҳумма лака сумту ва бика ааманту ва ъалайка таваккалту ва ъалаа ризқика афтарту, фағфирли зунубий йаа Ғоффару маа қоддамту ва маа аххорту. 
- - - - - - - - - - - - - - - - - -
Маъноси: Ё Аллоҳ! Сенга имон келтириб, Сенга таваккал қилиб, Сен учун рўза тутдим. Сен берган ризқинг билан ифтор қилдим. Эй гуноҳларни кечиргувчи Зот! Менинг олдинги ва кейинги гуноҳларимни кечир. Омин!""", reply_markup=RaTimes)

"""""####################### Namoz taqvimi"""""

@dp.message_handler(text = '🧎 Namoz taqvimi')
async def ramadan(message: types.Message):
	await message.reply('Tanlang', reply_markup=PrTimes)

@dp.message_handler(text='⌛️Vaqtni bilish')
async def ramadan(message: types.Message):
	send = await message.answer('⏳')
	user_id = message.from_user.id
	reg = sql.execute("SELECT region FROM users WHERE user_id = ?", (user_id,)).fetchone()[0]
	reg1 = regions[reg]
	html_text = requests.get(f'https://islom.uz/region/{reg1}').text
	soup = BeautifulSoup(html_text, 'lxml')
	times = soup.find('div', class_='in_header_p')
	bomdod = times.find('div', id = 'tc1').text
	quyosh = times.find('div', id='tc2').text
	peshin = times.find('div', id='tc3').text
	asr = times.find('div', id='tc4').text
	shom = times.find('div', id='tc5').text
	xufton = times.find('div', id='tc6').text
	img = Image.open('pic/pic.png')
	day = datetime.datetime.today().day
	myFont = ImageFont.truetype('mono.ttf', 55)
	I1 = ImageDraw.Draw(img)
	I1.text((340, 30), f"{day - 1}-Ramazon", font=myFont, fill=(255, 0, 0))
	I1.text((340, 100), f"{day}-Aprel", font=myFont, fill=(255, 0, 0))
	I1.text((30, 200), f"Bomdod : {bomdod}", font=myFont, fill=(255, 0, 0))
	I1.text((30, 300), f"Quyosh    : {quyosh}", font=myFont, fill=(255, 0, 0))
	I1.text((30, 400), f"Peshin    : {peshin}", font=myFont, fill=(255, 0, 0))
	I1.text((30, 500), f"Asr    : {asr}", font=myFont, fill=(255, 0, 0))
	I1.text((30, 600), f"Shom    : {shom}", font=myFont, fill=(255, 0, 0))
	I1.text((30, 700), f"Xufton    : {xufton}", font=myFont, fill=(255, 0, 0))
	I1.text((380, 800), f"{reg} vaqti", font=ImageFont.truetype('mono.ttf', 32), fill=(255, 0, 0))
	I1.text((330, 900), "@Muslim_kundaligi_robot", font=ImageFont.truetype('mono.ttf', 26), fill=(255, 0, 0))
	img.save(f"pic/{user_id}.png")
	if not check:
		await message.reply('Viloyatingizni tanlang', reply_markup=provinces)
	else:
		await message.reply_photo(photo=open(f'pic/{user_id}.png', 'rb'), caption=f"<b>{reg} namoz vaqtlari</b>\n\nBomdod > {bomdod}\nQuyosh > {quyosh}\nPeshin > {peshin}\nAsr > {asr}\nShom > {shom}\nXufton > {xufton}", reply_markup=PrTimes)
	await bot.delete_message(chat_id=message.chat.id, message_id=send.message_id)

@dp.message_handler(text='🎛 Oylik taqvm')
async def ramadan(message: types.Message):
	await message.reply('"Bu yerdan oylik taqvimlarni ko`rib olishiz mumkin:  https://islom.uz/vaqtlar/27/4"', reply_markup=PrTimes)

"""""          Viloyatni tanlash  """""

@dp.message_handler(text = 'Viloyatlar')
async def province(message: types.Message):
	await message.reply('O`z viloyatingizni tanlang', reply_markup=provinces)

@dp.callback_query_handler()
async def call(call: CallbackQuery):
	user_id = call.from_user.id
	region = call.data
	db = sqlite3.connect('./database/choos.sqlite3')
	sql = db.cursor()
	sql.execute("""CREATE TABLE IF NOT EXISTS users ("user_id"  INTEGER,"region"  INTEGER);""")
	check = sql.execute("SELECT region FROM users WHERE user_id = ?", (user_id,)).fetchone()
	if not check:
		sql.execute("""INSERT INTO users VALUES(?, ?)""", (user_id, region))
	else:
		sql.execute("""UPDATE users SET region = ? WHERE user_id = ?""", (region, user_id))
	db.commit()
	await call.answer()
	await call.message.answer(f'<b>{region}</b> tanlandi', reply_markup=main_btn)

""""""""""""""""""" 1- ustun"""""""
@dp.message_handler(text = '📿Iymon haqida')
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("🎧Audio maruza", "🎬Video maruza", "↩️ Orqaga qaytish")
	await message.answer("Allohumma solli a'la sayyidina Muhammad\n\nTanlang👇", reply_markup=markup)

@dp.message_handler(text = "🎧Audio maruza")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("🎧Audio maruza", "🎬Video maruza", "↩️ Orqaga qaytish")
	await message.answer_audio(audio="CQACAgIAAxkBAAIBkGJKvYdn56OASoIO2p3tgdGVPVW8AAJ8GgACVzzYSmgbRkVvNoNfIwQ",caption="Ya robbiy, o'zing iymonimizdan ayirmagaysan", reply_markup=markup)

@dp.message_handler(content_types='audio')
async def sdsd(message: types.Message):
	await message.reply(text = message.audio.file_id)

@dp.message_handler(text = "🎬Video maruza")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("🎧Audio maruza", "🎬Video maruza", "↩️ Orqaga qaytish")
	await message.answer_video(video="BAACAgIAAxkBAAEPHR1iSqqxzpy89GUffrA56q6lfM4_QgACMRQAApYX-Eg93VW2PYDvhCME", caption="Ya robbiy, o'zing iymonimizdan ayirmagaysan\n\n\n@Muslim_kundaligi_robot", reply_markup=markup)

"""""""""""""""""""""""""""""""        2  -  ustun   """""""

@dp.message_handler(text = "🧎Namoz haqida")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("Shayx Muhammad Sodiq", "Abdulloh domla,", "↩️ Orqaga qaytish")
	await message.answer("Innal illahi va inna ilayxi roji'un\n\nTanlang👇", reply_markup=markup)

@dp.message_handler(text = "Shayx Muhammad Sodiq")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("Shayx Muhammad Sodiq", "Abdulloh domla,", "↩️ Orqaga qaytish")
	audios = ["CQACAgIAAxkBAAIDVWJK9Shyd32qYeHEC8gWTAxq89xIAAJLFQACZmTQS2c0bzzO9CByIwQ", "CQACAgIAAxkBAAIDVmJK9Shjn5W2eyFu2l5YAAHyoKXsbgAC8Q0AAtlZwUpa55hVp4GSUSME"]
	for audio in audios:
		await message.answer_audio(audio=audio, caption="Shayx Muhammad Sodiq Muhammad Yusufning namoz haqidagi maruzasi\n\n\n@Muslim_kundaligi_robot", reply_markup=markup)

@dp.message_handler(text = "Abdulloh domla,")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("Shayx Muhammad Sodiq", "Abdulloh domla,", "↩️ Orqaga qaytish")
	audios = ["CQACAgIAAxkBAAIDWWJK9ViNUepgvZ65KRt3pfuQ3psSAAItFAACFEPYSkotMuAg6JhrIwQ", "CQACAgIAAxkBAAIDW2JK9YJWT-nhkOlzMKM7b_ipaoVyAAL8FAACSPmhS7BETf90h7zwIwQ"]
	for audio in audios:
		await message.answer_audio(audio=audio, caption="Abdulloh domlaning namoz haqidagi maruzasi\n\n\n@Muslim_kundaligi_robot", reply_markup=markup)


"""""""""""   3- ustun """""

@dp.message_handler(text = "☺️Ro'za haqida")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("🎧Audio maruzalar", "📖Ro'za tutish tartibi", "↩️ Orqaga qaytish")
	await message.answer("Innal illahi va inna ilayxi roji'un\n\nTanlang👇", reply_markup=markup)


@dp.message_handler(text = "🎧Audio maruzalar")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("Shayx Muhammad Sodiq", "Abdulloh domla", "↩️ Orqaga qaytish")
	await message.answer("Suhanollohi va bihamdi - Subhanollohil A'zim\n\nTanlang👇", reply_markup=markup)

@dp.message_handler(text = "Shayx Muhammad Sodiq")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("Shayx Muhammad Sodiq", "Abdulloh domla", "↩️ Orqaga qaytish")
	await message.answer_audio(audio="CQACAgIAAxkBAAIBo2JKwkRY8QUTS3S9Jr8c1nKZB49OAAL4HAACImoBSYz3fzDgiUN4IwQ", caption="Ramazon oyida tutiladigan ro'za va Ramazonning fazilatlari haqida Shayx Muhammad Sodiq Muhammad Yusufning maruzasi\n\n\n@Muslim_kundaligi_robot",reply_markup=markup)

@dp.message_handler(text = "Abdulloh domla")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("Shayx Muhammad Sodiq", "Abdulloh domla", "↩️ Orqaga qaytish")
	await message.answer_audio(audio="CQACAgIAAxkBAAIBpWJKwnLXCxmVvkG9vWuXpY_ihzDDAAIcEwACxhKpSNGN3haSV2CVIwQ", caption="Ramazon oyida tutiladigan ro'za va Ramazonning fazilatlari haqida Abdulloh domlaning marvizasi\n\n\n@Muslim_kundaligi_robot",reply_markup=markup)

@dp.message_handler(text = "📖Ro'za tutish tartibi")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("🎧Audio maruzalar", "📖Ro'za tutish tartibi", "↩️ Orqaga qaytish")
	await message.answer_audio(audio="CQACAgIAAxkBAAIBp2JKwydnhUOztGtJ96LtP_ZrIVhfAAIpFwAC0jhwSVjq2hR9rXj8IwQ", caption="MashaAlloh\n\n\n@Muslim_kundaligi_robot",reply_markup=markup)

"""""""""""""""""""""    4   -   ustun    """""""""


@dp.message_handler(text = "⚖️Zakot haqida")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("Shayx Muhammad Sodiq", "Abdulloh domla", "↩️ Orqaga qaytish")
	await message.answer("Marvizalarni tinglab hammasini bilib olasiz InshaAlloh\n\nTanlang👇", reply_markup=markup)

@dp.message_handler(text = "Shayx Muhammad Sodiq.")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("Shayx Muhammad Sodiq.", "Abdulloh domla.", "↩️ Orqaga qaytish")
	await message.answer_audio(audio="CQACAgIAAxkBAAIB92JK2RUUzkKzAjTBweZOuV5SfAWvAAJtFAACXtawSAmQaWChwxCwIwQ", caption="Ramazon oyida tutiladigan ro'za va Ramazonning fazilatlari haqida Shayx Muhammad Sodiq Muhammad Yusufning maruzasi\n\n\n@Muslim_kundaligi_robot",reply_markup=markup)

@dp.message_handler(text = "Abdulloh domla.")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("Shayx Muhammad Sodiq.", "Abdulloh domla.", "↩️ Orqaga qaytish")
	await message.answer_audio(audio="CQACAgIAAxkBAAIB-GJK2RWTPvuqcv5h9FOEw0d__5VoAALOHAAC2MMxSimwAuDRI68QIwQ", caption="Ramazon oyida tutiladigan ro'za va Ramazonning fazilatlari haqida Abdulloh domlaning marvizasi\n\n\n@Muslim_kundaligi_robot",reply_markup=markup)

"""""""""""""""""""""""""""""""""   5  -  ustun  """""""""""""""""""""""""""""""""""


@dp.message_handler(text = "🕋Haj haqida")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("Shayx Muhammad Sodiq..", "Abdulloh domla..", "📚Kitoblar","↩️ Orqaga qaytish")
	await message.answer("Marvizalarni tinglab hammasini bilib olasiz InshaAlloh\n\nTanlang👇", reply_markup=markup)

@dp.message_handler(text = "Shayx Muhammad Sodiq..")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("Shayx Muhammad Sodiq..", "Abdulloh domla..", "📚Kitoblar","↩️ Orqaga qaytish")
	await message.answer_audio(audio="CQACAgIAAxkBAAICVWJK4RVM46y2qibL0VQ3a06D9RyVAAJ1FwAC_1MBSlA4gWznnrUQIwQ", caption="Ramazon oyida tutiladigan ro'za va Ramazonning fazilatlari haqida Shayx Muhammad Sodiq Muhammad Yusufning maruzasi\n\n\n@Muslim_kundaligi_robot",reply_markup=markup)

@dp.message_handler(text = "Abdulloh domla..")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("Shayx Muhammad Sodiq..", "Abdulloh domla..", "📚Kitoblar","↩️ Orqaga qaytish")
	await message.answer_audio(audio="CQACAgIAAxkBAAICU2JK4KH3QhXqEqZZxNi0NCrIPrIuAAIIEQACkGMYS6aSCtlMWf1pIwQ", caption="Ramazon oyida tutiladigan ro'za va Ramazonning fazilatlari haqida Abdulloh domlaning marvizasi\n\n\n@Muslim_kundaligi_robot",reply_markup=markup)

@dp.message_handler(text = "📚Kitoblar")
async def sdsd(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("Shayx Muhammad Sodiq..", "Abdulloh domla..", "📚Kitoblar", "↩️ Orqaga qaytish")
	idFile = ["BQACAgIAAxkBAAICWGJK5pgapo3qI-t-aby-dLjHofVpAAIiFgACjAFZSqLRx9qO7WuCIwQ", "BQACAgIAAxkBAAICWWJK5pjK74EdpJfQ4amHhF88CqLJAAIjFgACjAFZStsmPxkftIckIwQ"]
	for id in idFile:
		await message.reply_document(document=id,caption="\nHaj va umra ibodatlari haqidagi kitob va programma\n\n@Muslim_kundaligi_robot",reply_markup=markup)


"""""""""""""""""""""""""""""""""""""""""""       QURON BO'LIMI     tez kunda         """""""




"""""""""""""""""""""""""   nashidlar   """""""

@dp.message_handler(text = "🔊Nashidlar")
async def nashid(msg: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("1 - 10", "11 - 20", "21 - 30", "↩️ Orqaga qaytish")
	await msg.reply("Tanlang👇", reply_markup=markup)

@dp.message_handler(text = "1 - 10")
async def num(msg: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("1 - 10", "11 - 20", "21 - 30", "↩️ Orqaga qaytish")
	nasheds = ["CQACAgIAAxkBAAICn2JK6EVpI8WPo53t9yXCqznU-Xb9AAJUGAACNbopSh-fA4q3-T0FIwQ", "CQACAgIAAxkBAAICt2JK6EWULtrPDcsIvICU-4tfwS-UAAJ6GAAC2YlASn2a325o_elJIwQ",
	           "CQACAgIAAxkBAAICjmJK6EU_TQKQ6IG07uhMKEe7LdngAAKvFQACqRZZSWzdIBgqrhJdIwQ", "CQACAgEAAxkBAAICq2JK6EWJeN1ekkU5rZ8vVD1nAyJFAAJeAQACKsvQRoHQIHTABXKjIwQ", "CQACAgIAAxkBAAICp2JK6EW-76LSV4BllLmkWDAidtzcAALCBAACTsLhSz7rL6acl9GmIwQ", "CQACAgIAAxkBAAICm2JK6EUKy7yyHHGI1EhAPPbsvNzJAAL_EwACfMUwSn9uhjM2JMrjIwQ",
	           "CQACAgIAAxkBAAICtmJK6EXAfSBwIERhDGJqZO3VcfgcAAIsFwACNko5SsyRjEK0EluYIwQ", "CQACAgIAAxkBAAICpmJK6EVyNIUzpE2W2ZPvCe9ffy7GAAKoCwACKSTRS5UV0d1vP96PIwQ", "CQACAgIAAxkBAAICsGJK6EXp6KKR8CX-dAKoHt2MuxTdAALQFQACZ3WZSAfSI4dMtLPZIwQ", "CQACAgEAAxkBAAICrGJK6EUkT2_WgRyP1fgzx7dt7gToAAJeAQACKsvQRoHQIHTABXKjIwQ"]
	for nashed in nasheds:
		await msg.reply_audio(audio=nashed, caption="Assalomu alaykum.\n\nAllohumma solli a'la sayyidina Muhammad\n\n\n@Muslim_kundaligi_robot", reply_markup=markup)

@dp.message_handler(text = "11 - 20")
async def num(msg: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("1 - 10", "11 - 20", "21 - 30", "↩️ Orqaga qaytish")
	nasheds = ["CQACAgIAAxkBAAICuGJK6EVLL-k9yiVoRBGq7hPl_1HcAALJEAAC7_5pSPwd4EhaO-JUIwQ", "CQACAgIAAxkBAAICqWJK6EXdX84JV_INvCF8vjW93y60AAJ9FQAC6MuxSKB6yX3OG-PqIwQ",
	           "CQACAgIAAxkBAAICtGJK6EWUQgZH5r5l2TS8UTAEt1zmAAKoCwACKSTRS5UV0d1vP96PIwQ", "CQACAgIAAxkBAAICqGJK6EWmjW25ZoXseKz9aAABrGG1kQACoBMAAh67OEjfsNxhAUacHiME", "CQACAgQAAxkBAAICsmJK6EXRVZASB4PIn38oEhti-86bAAK0bgACsXzJUmYi25kvYp8PIwQ", "CQACAgIAAxkBAAICtWJK6EUe13LHMm9qWKZXOPp6PfmHAAIFDAACkvT4SGAOspZDIQZvIwQ",
	           "CQACAgIAAxkBAAIComJK6EXPd0cSFnVGKyYYFCITv9owAALCBAACTsLhSz7rL6acl9GmIwQ", "CQACAgIAAxkBAAICrWJK6EUXYZf9V3C5M8as2AMKROv3AAIYEwACuswISyUtPAXQkUuAIwQ", "CQACAgIAAxkBAAICi2JK6EWGP1ZA2Pdh2PtCkTYhEy5cAAJxFgACMJL4SfZOlVmguTr4IwQ", "CQACAgIAAxkBAAIChGJK6EXga3JxK1L4MLrSbSuAH9vbAALQAgACbzWwSq_rOD-yHMFaIwQ"]
	for nashed in nasheds:
		await msg.reply_audio(audio=nashed, caption="Assalomu alaykum.\n\nAllohumma solli a'la sayyidina Muhammad\n\n\n@Muslim_kundaligi_robot", reply_markup=markup)

@dp.message_handler(text = "21 - 30")
async def num(msg: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
	markup.add("1 - 10", "11 - 20", "21 - 30", "↩️ Orqaga qaytish")
	nasheds = ["CQACAgIAAxkBAAICpWJK6EXF4tx5zFyeoSVt3GMn8L5vAALQAgACbzWwSq_rOD-yHMFaIwQ", "CQACAgIAAxkBAAICsWJK6EXg8QtW3P5D_wKQTL9rHgABJwAC5goAArWUcEguwPdbeslELiME",
	           "CQACAgIAAxkBAAICo2JK6EWDsk25L6njwdzm1XrZFToiAAJ9FQAC6MuxSKB6yX3OG-PqIwQ", "CQACAgIAAxkBAAICmGJK6EVd3IlDisXdgTqBvbYPS7VtAAJSIwACg_4ISQABhxoVUtfqByME", "CQACAgIAAxkBAAIClGJK6EX6J6WowOZXSJswnC1G6b_5AAL5FQACoTsZSklcfgfflCNuIwQ", "CQACAgIAAxkBAAICr2JK6EXfl2i9RcRY1Rjo9FgyDitoAAKeDQACq_QxSfF-PlacngqDIwQ",
	           "CQACAgIAAxkBAAICnmJK6EXKzlqNJVfL1EGOBvKfGBKXAAL7EwAC2YlISiviJp88yppeIwQ", "CQACAgIAAxkBAAICqmJK6EUPYpxXX0eVEJGD97Untyo0AALADwACqnaoSVZbdQzj6fPyIwQ", "CQACAgIAAxkBAAICf2JK6EX1bb6Lq4nZUnTC4H7_Bl5CAAIFDAACkvT4SGAOspZDIQZvIwQ", "CQACAgIAAxkBAAICkmJK6EU7TsY1yceDpaHoAsuEUrDQAAKmEwACSCUJShT9T3jpRt2gIwQ"]
	for nashed in nasheds:
		await msg.reply_audio(audio=nashed, caption="Assalomu alaykum.\n\nAllohumma solli a'la sayyidina Muhammad\n\n\n@Muslim_kundaligi_robot", reply_markup=markup)


if __name__=='__main__':
	executor.start_polling(dispatcher=dp)