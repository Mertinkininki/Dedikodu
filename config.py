import os
import heroku3
from telethon import TelegramClient, events
api_id = int(os.environ.get("APP_ID", "19764472"))
api_hash = os.environ.get("API_HASH", "1bb18890c8b4041cc66cb36ab796afca")
bot_token = os.environ.get("TOKEN", "5847695315:AAHwxw9EDcSI_khrdlC16cyCYpLnU4fRPK8")
# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
admin_qrup = int(os.environ.get("ADMIN_QRUP", "-1001704881102"))
etiraf_qrup = int(os.environ.get("ETIRAF_QRUP", "-1001867312382"))
kanal = os.environ.get("kanal")
log_qrup = int(os.environ.get("LOG_QRUP", "-1001704881102"))
botad = os.environ.get("BOT_AD", "İtirafBotu")
etirafmsg = os.environ.get("etirafmsg")
startmesaj = os.environ.get("startmesaj")
etirafyaz = os.environ.get("etirafyaz")
qrupstart = os.environ.get("qrupstart")
gonderildi = os.environ.get("gonderildi")
support = os.environ.get("support", "Sohbetkampus")
sahib = os.environ.get("sahib", "Yalnizkaranlik")
