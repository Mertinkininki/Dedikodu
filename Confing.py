import os
import heroku3
from telethon import TelegramClient, events
#
# Buranı qurdalama
# Yalnız deploy buttonuyla botunu yarat
# 
api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
admin_qrup = int(os.environ.get("ADMIN_QRUP", "-1001704881102))
etiraf_qrup = int(os.environ.get("ETIRAF_QRUP", "-1001867212382"))
kanal = os.environ.get("kanal", "Kampus_itiraf")
log_qrup = int(os.environ.get("LOG_QRUP", "-1001704881102"))
botad = os.environ.get("BOT_AD")
etirafmsg = os.environ.get("etirafmsg")
startmesaj = os.environ.get("startmesaj")
etirafyaz = os.environ.get("etirafyaz")
qrupstart = os.environ.get("qrupstart")
gonderildi = os.environ.get("gonderildi")
support = os.environ.get("support", "Sohbet_kampus")
sahib = os.environ.get("sahib", "Yalnizkaranlik")