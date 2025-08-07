# FileStore-Bot-on-Telegram-Cloud
# 📁 Telegram Permanent File Store Bot

This Telegram bot lets users upload multiple files and receive a permanent group download link. Files are stored in a private channel, and links generated via `/done` remain active for future use.

---

## 🚀 Features

- Upload multiple files (photos, documents, videos, etc.)
- Group them together
- Receive a **permanent download link**
- Files are stored securely in a private channel
- Simple and fast setup

---

## ⚙️ Setup Instructions

### 1. 🔐 Get your Bot Token

- Go to [@BotFather](https://t.me/BotFather) on Telegram.
- Send `/start`, then `/newbot`
- Follow the prompts to:
  - Set a name (e.g., **Nooba FileStore Bot**)
  - Set a username (e.g., **`noobayogesh_bot`**)  
- Copy the **HTTP API Token** provided — this is your `BOT_TOKEN`.

### 2. 📢 Create a Private Channel

- Open Telegram and tap **New Channel**
- Set a name (e.g., **NoobaStoreChannel**)
- Make sure it is **private**
- Add **your bot** (`@noobayogesh_bot`) as an **admin**
  - Enable: `Post Messages` permission

#### 🔍 Get Channel ID:

1. Add [@getidsbot](https://t.me/getidsbot) to your channel temporarily
2. Forward any message from your channel to @getidsbot
3. It will reply with the **channel ID** like `-1001837916554`

> ✅ Use this **channel ID** in your code (remove `-100` prefix if not required by your bot API method — in most cases it's required).

---

## 🛠️ Run the Bot

1. Clone the repo or copy the Python script
2. Install dependencies:
   ```bash
   pip install python-telegram-bot --upgrade
