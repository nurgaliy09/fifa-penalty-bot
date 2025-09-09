import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Tokenni ENV orqali olish
TOKEN = os.getenv("BOT_TOKEN")

# /start komandasi (async)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Bot muvaffaqiyatli ishlayapti ✅")

def main():
    if not TOKEN:
        print("❌ BOT_TOKEN o‘rnatilmagan!")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
import random

# Misol uchun oddiy prognoz generator
def generate_coupon():
    # 4 ta o'yin kombinatsiyasi
    matches = [
        "Team A vs Team B",
        "Team C vs Team D",
        "Team E vs Team F",
        "Team G vs Team H"
    ]

    # Har bir o'yin uchun random natija: goal/miss
    coupon = []
    for match in matches:
        prediction = random.choice(["goal", "miss"])
        coupon.append({"match": match, "prediction": prediction})

    return coupon
