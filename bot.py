import random
from time import sleep
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# TODO: add token and name
TOKEN = ""
NAME = ""

async def register_member(username: str, context: ContextTypes.DEFAULT_TYPE):
    # TODO: initialize an empty set of registered members in context if it doesn't exist yet
    if username != NAME:
        # TODO: add username to the set in context
        pass

async def send_to_random(chat_id: int, members: set):
    if len(members):
        username = random.choice(list(members))
        await app.bot.send_message(chat_id, f"@{username} How do you do, my fellow bot?")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # TODO: reply with a greeting message
    await register_member(update.effective_user.username, context)
    await send_to_random(update.effective_chat.id, context.chat_data["members"])

async def handle_member_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("I saw the bot")
    for user in update.message.new_chat_members:
        await register_member(user.username, context)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await register_member(update.effective_user.username, context)
    sleep(10)
    if NAME in update.message.text:
        # TODO: reply with a greeting message (quoting the original message)
        # TODO: retrieve the set of members from context and pass it to send_to_random
        pass

app = Application.builder().token(TOKEN).build()

# TODO: register the start_command handler for the /start command
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, handle_member_update))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling(allowed_updates=Update.ALL_TYPES)