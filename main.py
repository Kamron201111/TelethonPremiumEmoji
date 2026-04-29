from telethon import TelegramClient, events
from telethon.tl.types import MessageEntityCustomEmoji
from xtelethon import CustomParseMode

# ==========================================
# O'zingizning ma'lumotlaringizni kiriting:
API_ID = 23651528          # my.telegram.org
API_HASH = 'ca42cf77a78ee409550aac24e179c87e'     # my.telegram.org
SESSION = 'my_session'
# ==========================================

client = TelegramClient(SESSION, API_ID, API_HASH)
client.parse_mode = CustomParseMode('markdown')


# 1. Premium emoji yuborish
async def send_premium_emoji():
    # Emoji ID ni o'zgartiring (quyida ID olish yo'li bor)
    msg = 'Salom! Bu premium emoji: [❤️](emoji/5368324170671202286)'
    await client.send_message('me', msg)
    print("Xabar yuborildi!")


# 2. Emoji ID olish (Saved Messages ga premium emoji yuboring)
@client.on(events.NewMessage(from_users='me'))
async def get_emoji_id(event):
    if event.entities:
        for entity in event.entities:
            if isinstance(entity, MessageEntityCustomEmoji):
                emoji = event.message.message[entity.offset:entity.offset + entity.length]
                print(f"Emoji: {emoji}  |  ID: {entity.document_id}")


async def main():
    await send_premium_emoji()  # Yuborish
    # ID olish uchun quyidagi qatorni uncomment qiling:
    # await client.run_until_disconnected()


with client:
    client.loop.run_until_complete(main())
