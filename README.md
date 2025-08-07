# FileStore-Bot-on-Telegram-Cloud
# 📁 Telegram Permanent File Store Bot

This Telegram bot lets users upload multiple files and receive a **permanent batch download link**. Files are stored in a private channel and grouped under a single shareable link.

---

## 🚀 Features

- ✅ Upload **multiple files** in a batch (photo, document, video, etc.)
- 🔗 Receive a **single permanent download link** for the whole group
- 🔒 Files stored securely in a **private Telegram channel**
- 📤 All Telegram-supported media types supported (photo, video, audio, document)
- 🧠 Grouped files are saved with a unique ID in `file_groups.json`
- ♻️ Can retrieve the same group anytime using the generated link

---

## ⚙️ Setup Instructions

### 1. 🔐 Get your Bot Token

- Go to [@BotFather](https://t.me/BotFather)
- Run `/start` → `/newbot`
- Set a name and username (e.g., `noobayogesh_bot`)
- Copy the **API Token** — this is your `BOT_TOKEN`

### 2. 📢 Create a Private Channel

- Open Telegram → Create a **new channel**
- Make it **Private**
- Add your bot (`@noobayogesh_bot`) as **Admin**
  - Ensure **Post Messages** permission is enabled

### 3. 📋 Get the Channel ID

1. Add [@getidsbot](https://t.me/getidsbot) to your private channel
2. Forward any message to @getidsbot
3. Copy the ID shown (e.g., `-1001837916554`) and set this as `CHANNEL_ID` in your code

---

## 🛠️ Run the Bot

1. Install dependencies:
   ```bash
   pip install python-telegram-bot --upgrade
