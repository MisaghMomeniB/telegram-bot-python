import os
from telegram import Update
from dotenv import load_dotenv
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

load_dotenv()


TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    print("Recived :", user_text)

    await update.message.reply_text(f"and You : {user_text}")


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Bot Started!")

app.run_polling()
