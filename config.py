import os

BOT_TOKEN = os.getenv("8383759148:AAGJzPUVxiROwGtPI2daOAK_yXdHugAjKn0")
ADMIN_IDS = [int(i) for i in os.getenv("@MultyNet", "").split(",") if i]
