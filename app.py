import os
import json
import uuid
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)

# 🔧 Your credentials
BOT_TOKEN = 'bottoken'
CHANNEL_ID = 'channelid'  # Your private channel ID (not @username)
BOT_USERNAME = 'botname'  # without @
GROUP_DB_FILE = 'file_groups.json'
# ================

# Load or initialize group storage
if os.path.exists(GROUP_DB_FILE):
    with open(GROUP_DB_FILE, 'r') as f:
        file_groups = json.load(f)
else:
    file_groups = {}

def save_groups():
    with open(GROUP_DB_FILE, 'w') as f:
        json.dump(file_groups, f)

# Temporary per-user group collector
user_temp_files = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args

    if args and args[0].startswith("get_"):
        group_id = args[0][4:]

        if group_id not in file_groups:
            await update.message.reply_text("❌ Group not found or expired.")
            return

        for msg_id in file_groups[group_id]:
            try:
                await context.bot.copy_message(
                    chat_id=update.effective_chat.id,
                    from_chat_id=CHANNEL_ID,
                    message_id=msg_id
                )
            except Exception as e:
                await update.message.reply_text(f"❌ Failed to send file ID {msg_id}")
    else:
        await update.message.reply_text(
            "👋 Send multiple files one by one.\nThen send /done to get a download link for the group."
        )

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    message = update.message

    try:
        sent = await message.forward(chat_id=CHANNEL_ID)
        file_id = sent.message_id

        # Store in user's temporary group
        user_temp_files.setdefault(user_id, []).append(file_id)

        await message.reply_text("✅ File received. Send more or use /done to finish.")
    except Exception as e:
        await update.message.reply_text(f"❌ Error saving file:\n`{e}`", parse_mode='Markdown')

async def done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    if user_id not in user_temp_files or not user_temp_files[user_id]:
        await update.message.reply_text("❗You haven't sent any files.")
        return

    group_id = str(uuid.uuid4())[:8]  # short group ID
    file_groups[group_id] = user_temp_files[user_id]
    save_groups()

    del user_temp_files[user_id]  # Clear temp store

    link = f"https://t.me/{BOT_USERNAME}?start=get_{group_id}"
    await update.message.reply_text(
        f"✅ Group saved!\n\n📎 [Download all files]({link})",
        parse_mode='Markdown',
        disable_web_page_preview=True
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("done", done))
    app.add_handler(MessageHandler(
        filters.Document.ALL | filters.VIDEO | filters.AUDIO | filters.PHOTO,
        handle_file
    ))

    print("🤖 Bot is running...")

    app.run_polling()
