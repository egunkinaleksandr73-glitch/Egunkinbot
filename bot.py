import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я Egunkinbot.\n\n"
        "Выбери раздел:\n\n"
        "/news — 📰 Новости дня\n"
        "/games — 🎮 Игры\n"
        "/tech — 💻 Технологии\n"
        "/movie — 🎬 Кино"
    )


async def news(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📰 Новости дня\n\n"
        "Раздел пока настраивается. Скоро здесь будут свежие новости."
    )


async def games(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 Игры\n\n"
        "Раздел пока настраивается. Скоро здесь будут новости игровой индустрии."
    )


async def tech(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💻 Технологии\n\n"
        "Раздел пока настраивается. Скоро здесь будут новости технологий."
    )


async def movie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 Кино\n\n"
        "Раздел пока настраивается. Скоро здесь будут новости кино."
    )


def main():
    token = os.environ["BOT_TOKEN"]

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", news))
    app.add_handler(CommandHandler("games", games))
    app.add_handler(CommandHandler("tech", tech))
    app.add_handler(CommandHandler("movie", movie))

    app.run_polling()


if __name__ == "__main__":
    main()
