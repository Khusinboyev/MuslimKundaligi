from aiogram.types import ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
main_btn.add("📖Quron, to'liq holda")
main_btn.add('📆 Taqvimlar', "📿Iymon haqida")
main_btn.add('🧎Namoz haqida', "☺️Ro'za haqida", "⚖️Zakot haqida")
main_btn.add("🕋Haj haqida", '🔊Nashidlar',)
main_btn.add('Viloyatlar', "Adminga murojaat")

calendars = ReplyKeyboardMarkup(resize_keyboard=True)
calendars.add('📆 Ramazon taqvimi', "🧎 Namoz taqvimi")
calendars.add('↩️ Orqaga qaytish')

RaTimes = ReplyKeyboardMarkup(resize_keyboard=True)
RaTimes.add('⏰ Vaqtni bilish', '⏳ Oylik taqvim')
RaTimes.add("📿 O'qiadigan duolar", '🔙️ Orqaga qaytish')

PrTimes = ReplyKeyboardMarkup(resize_keyboard=True)
PrTimes.add('⌛️Vaqtni bilish', '🎛 Oylik taqvm')
PrTimes.add('🔙️ Orqaga qaytish')

provinces = InlineKeyboardMarkup(row_width=2)
provinces.add(InlineKeyboardButton(text='Andijon', callback_data='Andijon'))
provinces.insert(InlineKeyboardButton(text='Fargona', callback_data='Fargona'))
provinces.insert(InlineKeyboardButton(text='Namangan', callback_data='Namangan'))
provinces.insert(InlineKeyboardButton(text='Toshkent', callback_data='Toshkent'))
provinces.insert(InlineKeyboardButton(text='Sirdaryo', callback_data='Sirdaryo'))
provinces.insert(InlineKeyboardButton(text='Samarqand', callback_data='Samarqand'))
provinces.insert(InlineKeyboardButton(text='Qashqadaro', callback_data='Qashqadaro'))
provinces.insert(InlineKeyboardButton(text='Surxondaryo', callback_data='Surxondaryo'))
provinces.insert(InlineKeyboardButton(text='Navoiy', callback_data='Navoiy'))
provinces.insert(InlineKeyboardButton(text='Buxoro', callback_data='Buxoro'))
provinces.insert(InlineKeyboardButton(text='Jizzax', callback_data='Jizzax'))
provinces.insert(InlineKeyboardButton(text='Xorazm', callback_data='Xorazm'))
provinces.insert(InlineKeyboardButton(text='Qoroqolpoqiston', callback_data='Qoroqolpoq'))
