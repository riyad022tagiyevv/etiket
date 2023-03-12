import os
import heroku3
from telethon import TelegramClient, events

from pyrogram import Client
from pyrogram import filters
import logging
#
# Burayı gurcalama
# 
# 
#api_id = 16102648
#api_hash = "378a73e340eb634cf67c8c42bafa9f37"
#bot_token = "6019015118:AAFLD0oIHeV47_7ceed-cWUVh17baqmfWPI"

# Telethon 
#client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
#USERNAME = "ModernTagBot"
group = -1001823689827
startmesaj = "**Men qrubunuzdaki üyeleri etiketleyebilen bir botum. Meni Qrubunuza alıf çalıştırabilirsiniz.**\n\n**Komutlar için /help yazın.**"
komutlar = "Komutlar:\n\n/utag -text- Kullanıcıları 5'li etiketlerim.\n/atag -text- Yöneticileri etiketlerim.\n/tektag Üyeleri tek tek etiketlerim.\n/etag - Üyeleri emoji ile etiketlerim.\n/soztag - Üyeleri sözler ile etiketlerim.\n/gisimtag - Üyeleri güzel isimlerle etiketlerim.\n/cancel - Etiket işlemini iptal ederim .\n\nYalnızca yöneticiler bu komutları kullanabilir."
qrupstart = "**Şu an aktif olarak çalışmaktayım.** 🕊🍃\n\n**Komutlar hakkında bilgi için /help yazın."
sahib = "RiyadAndMe"
support = "OldHumans"
sahib = "RiyadAndMe"
ozel_list = 5809546648
#
app = Client("GUNC",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token
             )
