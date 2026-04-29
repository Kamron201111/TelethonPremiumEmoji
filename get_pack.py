from telethon import TelegramClient
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetShortName, DocumentAttributeCustomEmoji

API_ID = 23651528
API_HASH = 'ca42cf77a78ee409550aac24e179c87e'
SESSION = 'my_session'

async def get_pack_emojis(pack_name):
    async with TelegramClient(SESSION, API_ID, API_HASH) as client:
        sticker_set = await client(GetStickerSetRequest(
            stickerset=InputStickerSetShortName(pack_name),
            hash=0
        ))
        
        print(f"Jami emoji soni: {len(sticker_set.documents)}\n")
        
        for sticker in sticker_set.documents:
            for attr in sticker.attributes:
                if hasattr(attr, 'alt'):  # emoji belgisi
                    print(f"Emoji: {attr.alt} | ID: {sticker.id}")

import asyncio
asyncio.run(get_pack_emojis("status_packuz"))
