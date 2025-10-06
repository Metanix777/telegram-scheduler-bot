# Telegram Scheduler Bot

Бот для отправки сообщений в заданное время определённым пользователям.

## Команды

- `/start` — приветствие
- `/add` — добавить сообщение в формате `chat_id|текст|день недели|время`

## Развёртывание на Render

1. Залей проект на GitHub
2. Создай Web Service на [Render.com](https://render.com)
3. Укажи:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python bot.py`
   - Environment variables:
     - `BOT_TOKEN`: токен от BotFather
     - `ADMIN_IDS`: список ID админов через запятую
