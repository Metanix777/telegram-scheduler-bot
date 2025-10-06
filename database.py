import aiosqlite
from datetime import datetime

DB_NAME = "schedule.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS schedule (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER,
                message TEXT,
                day TEXT,
                time TEXT
            )
        """)
        await db.commit()

async def add_schedule(chat_id, message, day, time):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("INSERT INTO schedule (chat_id, message, day, time) VALUES (?, ?, ?, ?)",
                         (chat_id, message, day, time))
        await db.commit()

async def get_all_schedules():
    async with aiosqlite.connect(DB_NAME) as db:
        now = datetime.now()
        day = now.strftime("%A")
        time = now.strftime("%H:%M")
        cursor = await db.execute("SELECT chat_id, message FROM schedule WHERE day = ? AND time = ?", (day, time))
        return await cursor.fetchall()
