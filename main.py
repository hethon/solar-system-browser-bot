import os
import logging
from html import escape
from uuid import uuid4

from telegram import (
    InlineQueryResultCachedPhoto, 
    InlineQueryResultsButton, 
    WebAppInfo, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton, 
    Update
)
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, InlineQueryHandler, filters


from planets import planets, caption_template
from helpers import formatstr
from error_handler import report_error
import config

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text("Hi!")


async def photo_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_id = update.message.photo[-1].file_id
    await update.message.reply_text(f"FileId: <code>\"{file_id}\"</code>", quote=True, parse_mode=ParseMode.HTML)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the inline query. This is run when you type: @botusername <query>"""
    query = update.inline_query.query
    query = query.lower() if query else query

    results = []
    if query in planets:
        planets__local = {query: planets[query]} 
    else:
        planets__local = planets

    for planet_name in planets__local:
        planet = planets[planet_name]

        results.append(
            InlineQueryResultCachedPhoto(
                id=str(uuid4()),
                photo_file_id=planet["photo_file_id"],
                title=planet["name"],
                description=planet["description"],
                caption=formatstr(caption_template, **planet),
                parse_mode=ParseMode.HTML,
                reply_markup=InlineKeyboardMarkup.from_button(
                    InlineKeyboardButton(
                        text="Let's go!", 
                        url=f"{config.web_app_direct_link}?startapp={planet['name']}"
                    )
                )
            )
        )

    await update.inline_query.answer(
        results=results, 
        button=InlineQueryResultsButton(
            "Open Miniapp", 
            web_app=WebAppInfo(url=config.web_app_url)
        )
    )


def main() -> None:
    TOKEN = os.getenv("BOT_TOKEN")

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # application.add_handler(MessageHandler(filters.PHOTO, photo_file_id))

    application.add_handler(InlineQueryHandler(inline_query))

    application.add_error_handler(report_error)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
