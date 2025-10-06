from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
import asyncio
from config import BOT_TOKEN, ADMIN_IDS
from database import init_db, add_schedule
from scheduler import setup_scheduler

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command(start))
async def start(msg types.Message)
    await msg.answer(Привет! Я бот-напоминалка. Используй add чтобы добавить сообщение.)

@dp.message(Command(add))
async def add(msg types.Message)
    if msg.from_user.id not in ADMIN_IDS
        await msg.answer(У тебя нет прав для добавления сообщений.)
        return
    await msg.answer(Отправь сообщение в форматеnn`chat_idтекстдень неделивремя (HHMM)`, parse_mode=Markdown)

@dp.message(F.text.regexp(r^d+.+.+d{2}d{2}$))
async def handle_schedule(msg types.Message)
    try
        chat_id, text, day, time = msg.text.split()
        await add_schedule(int(chat_id), text.strip(), day.strip(), time.strip())
        await msg.answer(Сообщение добавлено в расписание.)
    except Exception as e
        await msg.answer(fОшибка {e})

async def main()
    await init_db()
    setup_scheduler()
    await dp.start_polling(bot)

if __name__ == __main__
    asyncio.run(main())
