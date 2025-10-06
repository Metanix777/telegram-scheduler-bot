from apscheduler.schedulers.asyncio import AsyncIOScheduler
from database import get_all_schedules
from aiogram import Bot
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
scheduler = AsyncIOScheduler()

async def scheduled_job():
    tasks = await get_all_schedules()
    for chat_id, message in tasks:
        await bot.send_message(chat_id, message)

def setup_scheduler():
    scheduler.add_job(scheduled_job, "cron", minute="*")
    scheduler.start()
