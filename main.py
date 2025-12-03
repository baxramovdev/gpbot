from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils import executor

# 🔑 BotFather'dan olgan tokeningni yoz
TOKEN = "8444313843:AAG_7dMIvKGNTajB2svz058y-Iie9bU08Ds"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# /start handler
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Web App tugma yaratish
    webapp_info = WebAppInfo(url="https://grapher-eight.vercel.app/")
    button = InlineKeyboardButton(text="Open Grapher App", web_app=webapp_info)
    keyboard = InlineKeyboardMarkup().add(button)

    # Foydalanuvchiga xabar yuborish
    await message.answer(
        "Hello! Click the button to open Grapher Web App:",
        reply_markup=keyboard
    )

if __name__ == "__main__":
    print("Bot is running...")
    executor.start_polling(dp, skip_updates=True)
