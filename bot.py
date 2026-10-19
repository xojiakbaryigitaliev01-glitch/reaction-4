import os
import random
from telegram import Update, ReactionTypeEmoji
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]
BASE_URL = os.environ["RENDER_EXTERNAL_URL"]  # Render buni o'zi beradi
PORT = int(os.environ.get("PORT", 10000))
EMOJIS = ["👍", "❤️", "🔥", "😍"]

async def react_to_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    post = update.channel_post
    await context.bot.set_message_reaction(
        chat_id=post.chat_id,
        message_id=post.message_id,
        reaction=[ReactionTypeEmoji(random.choice(EMOJIS))],
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.UpdateType.CHANNEL_POST, react_to_post))

app.run_webhook(
    listen="0.0.0.0",
    port=PORT,
    url_path=BOT_TOKEN,
    webhook_url=f"{BASE_URL}/{BOT_TOKEN}",
    allowed_updates=["channel_post"],
)
