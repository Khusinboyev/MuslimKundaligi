from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
async def main_menu():
    Markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    Btn1 = KeyboardButton("📊 statistika")
    Btn2 = KeyboardButton("📌 Kanallar")
    Btn3 = KeyboardButton("✍️ Xabar yuborish")
    Btn6 = KeyboardButton("♻️ Tozalash")
    Markup.add(Btn1,Btn2)
    Markup.add(Btn3,Btn6)
    return Markup
async def send_message_btn():
    Markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    Btn1 = KeyboardButton("Bitta foydalanuvchiga yuborish")
    Btn3 = KeyboardButton("Barcha foydalanuchilarga yuborish")
    Btn4 = KeyboardButton("🔙 Orqaga qaytish")
    Markup.add(Btn1,Btn3)
    Markup.add(Btn4)
    return Markup

async def back_btn():
    Markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    Btn1 = KeyboardButton("🔙 Orqaga qaytish")
    Markup.add(Btn1)
    return Markup

async def channels_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    Btn1 = KeyboardButton("➕   Kanal qo`shish")
    Btn2 = KeyboardButton("🚫  Kanal olib tashlash")
    Btn3 = KeyboardButton("📜 Kanallar ro'yhati")
    markup.add(Btn1,Btn2)
    markup.add(Btn3)
    markup.add("🔙 Orqaga qaytish")
    return markup

async def connect_btn():
    Markup = ReplyKeyboardMarkup(resize_keyboard=True)
    Btn1 = KeyboardButton('ID qo\'shish')
    Btn2 = KeyboardButton('ID olib tashlash')
    Btn3 = KeyboardButton('ID lar ro\'yhati')
    Btn4 = KeyboardButton('🔙 Orqaga qaytish')
    Markup.add(Btn1,Btn2)
    Markup.add(Btn3)
    Markup.add(Btn4)
    return Markup

