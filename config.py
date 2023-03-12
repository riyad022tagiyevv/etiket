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
#api_id = 24647583
#api_hash = "f41a6516ad6fba3b43d9cccd1f2c551c"
#bot_token = "6116997441:AAFF9bqrIam6UzGCi6BHoGV6U4gax0KtSRE"

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
