from telethon import TelegramClient
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetShortName, DocumentAttributeCustomEmoji

API_ID = 23651528
API_HASH = 'ca42cf77a78ee409550aac24e179c87e'
SESSION = 'my_session'

# === SHU YERGA 10 TA PACK NOMINI YOZING ===
PACK_NAMES = [
    "tgiosicons",
    "DanatShopUz1",
    "Statusvideobytaraxd",
    "CenterOfPacks66572647",
    "EmojiCatalogbot0060",
    "emojisbyisakovkhusniddin",
    "ApplicationEmoji",
    "TgPremiumIcon",
    "NXDAMA_by_fStikBot",
    "TajalyanEmoji",
]
# ==========================================

OUTPUT_FILE = "emoji_ids.txt"

async def get_pack_emojis(client, pack_name):
    try:
        sticker_set = await client(GetStickerSetRequest(
            stickerset=InputStickerSetShortName(pack_name),
            hash=0
        ))
        print(f"[{pack_name}] - {len(sticker_set.documents)} ta emoji topildi")
        return sticker_set.documents
    except Exception as e:
        print(f"[{pack_name}] - XATO: {e}")
        return []

async def main():
    async with TelegramClient(SESSION, API_ID, API_HASH) as client:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            for pack_name in PACK_NAMES:
                documents = await get_pack_emojis(client, pack_name)
                
                f.write(f"\n=== {pack_name} ({len(documents)} ta) ===\n")
                
                for sticker in documents:
                    for attr in sticker.attributes:
                        if hasattr(attr, 'alt'):
                            f.write(f"{sticker.id}\n")
                            print(f"  Emoji: {attr.alt} | ID: {sticker.id}")

        print(f"\nBarcha ID lar '{OUTPUT_FILE}' fayliga yozildi!")

import asyncio
asyncio.run(main())
