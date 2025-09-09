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
