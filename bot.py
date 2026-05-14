import random
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


# TODO 1: add token and name
TOKEN = ""
NAME = ""

# Add a user to the list of known users in the group chat
async def register_member(username: str, context: ContextTypes.DEFAULT_TYPE):
    # TODO 2: initialize an empty set of registered members in context if it doesn't exist yet
    if username != NAME:
        # TODO 3: add the username to the set in context
        pass

# Greet a random user in the group chat
async def send_to_random(chat_id: int, members: set):
    if len(members):
        username = random.choice(list(members))
        await app.bot.send_message(chat_id, f"@{username} How do you do, my fellow bot?")

# Handles the /start command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, my fellow bots!")
    await register_member(update.effective_user.username, context)

# Handles new members joining
async def handle_member_update(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for user in update.message.new_chat_members:
        await register_member(user.username, context)

# Responds to messages with a mention of the bot
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await register_member(update.effective_user.username, context)
    if NAME in update.message.text:
        # TODO 4: reply with a greeting message
        await asyncio.sleep(10)
        # TODO 5: greet a random other user (by calling send_to_random() with the chat ID and the set of users stored in context)
        pass

app = Application.builder().token(TOKEN).build()

# TODO 6: register the start_command() handler for the /start command
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, handle_member_update))
# TODO 7: register the handle_message() handler for all messages except commands
app.run_polling(allowed_updates=Update.ALL_TYPES)