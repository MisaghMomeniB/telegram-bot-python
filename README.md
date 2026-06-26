# 🤖 Telegram Bot Python

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![python-telegram-bot](https://img.shields.io/badge/python--telegram--bot-22.8-blue?style=for-the-badge&logo=telegram&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

A clean, minimal, and production-ready **Telegram Bot** built with Python — powered by [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot) v22.8 and async/await architecture. 🚀

[✨ Features](#-features) · [📦 Installation](#-installation) · [⚙️ Configuration](#%EF%B8%8F-configuration) · [🚀 Usage](#-usage) · [📁 Project Structure](#-project-structure) · [🛠️ Tech Stack](#%EF%B8%8F-tech-stack) · [🤝 Contributing](#-contributing) · [📄 License](#-license)

</div>

---

## ✨ Features

- 💬 **Echo Bot** — Replies to every message with what the user said
- 👋 **`/start` Command** — Greets the user by their first name
- 🛡️ **Global Error Handler** — Catches and logs all runtime errors gracefully
- 🔐 **Environment-based Config** — API token loaded securely via `.env` (never hardcoded)
- ⚡ **Fully Async** — Built on Python's `asyncio` for non-blocking, high-performance handling
- 📋 **Structured Logging** — Timestamped logs with levels for easy debugging
- 🧹 **Clean Architecture** — Minimal, readable, and easily extendable codebase

---

## 📦 Installation

### Prerequisites

Make sure you have the following installed:

- 🐍 **Python 3.10+**
- 📦 **pip**
- 🤖 A **Telegram Bot Token** from [@BotFather](https://t.me/BotFather)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/MisaghMomeniB/telegram-bot-python.git
cd telegram-bot-python
```

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Linux/macOS
venv\Scripts\activate           # On Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Create a `.env` file in the root directory:

```bash
cp .env.example .env   # if provided, otherwise create manually
```

Add your Telegram Bot Token:

```env
TOKEN=your_telegram_bot_token_here
```

> 💡 **Tip:** Get your token by messaging [@BotFather](https://t.me/BotFather) on Telegram and using the `/newbot` command.

> 🔒 **Security:** Never commit your `.env` file to version control. It's already included in `.gitignore`.

---

## 🚀 Usage

Start the bot with:

```bash
python bot.py
```

You should see output like:

```
2026-06-26 12:00:00,000 - __main__ - INFO - Bot started!
```

Now open Telegram, find your bot, and try:

| Command / Input | Response |
|---|---|
| `/start` | `Hello, [YourName]!` |
| Any text message | `You said: [your message]` |

---

## 📁 Project Structure

```
telegram-bot-python/
│
├── bot.py               # 🤖 Main bot logic (handlers, app setup)
├── requirements.txt     # 📦 Python dependencies
├── .env                 # 🔐 Environment variables (not committed)
├── .gitignore           # 🚫 Files excluded from Git
├── LICENSE              # 📄 MIT License
└── README.md            # 📖 You are here
```

---

## 🛠️ Tech Stack

| Library | Version | Purpose |
|---|---|---|
| `python-telegram-bot` | 22.8 | Telegram Bot API wrapper |
| `python-dotenv` | 1.2.2 | `.env` file loader |
| `httpx` | 0.28.1 | Async HTTP client |
| `anyio` | 4.14.0 | Async I/O backend |

---

## 🧩 How It Works

```
User sends message
       │
       ▼
  Telegram API
       │
       ▼
python-telegram-bot (polling)
       │
       ├── /start command ──► start() handler ──► "Hello, {name}!"
       │
       ├── text message ────► echo() handler  ──► "You said: {text}"
       │
       └── any error ───────► error_handler() ──► logs to console
```

The bot uses **long polling** to continuously check for new updates from Telegram's servers — no webhook setup required, making it perfect for local development and simple deployments.

---

## 🔧 Extending the Bot

Adding new commands is straightforward:

```python
# Add a new /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Available commands:\n/start - Greet the bot\n/help - Show this message")

# Register it in main()
app.add_handler(CommandHandler("help", help_command))
```

Some ideas to build on top of this template:

- 🗓️ Reminder / scheduler bot
- 🌤️ Weather info bot
- 📊 Poll / survey bot
- 🤖 AI-powered chatbot (integrate with an LLM API)
- 🛒 E-commerce notification bot

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 🙌

1. Fork the project
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add some amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

Please make sure your code is clean, well-commented, and follows existing conventions.

---

## 🐛 Reporting Issues

Found a bug? Have a suggestion? [Open an issue](https://github.com/MisaghMomeniB/telegram-bot-python/issues) and describe:

- What you expected to happen
- What actually happened
- Steps to reproduce

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

```
MIT License — free to use, modify, and distribute with attribution.
```

---

## 👤 Author

**Misagh Momeni**

- GitHub: [@MisaghMomeniB](https://github.com/MisaghMomeniB)

---

<div align="center">

⭐ **If you found this project helpful, please give it a star!** ⭐

Made with ❤️ and Python 🐍

</div>
