from telethon import TelegramClient
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetShortName, DocumentAttributeCustomEmoji

API_ID = 23651528
API_HASH = 'ca42cf77a78ee409550aac24e179c87e'
SESSION = 'my_session'

# === SHU YERGA PACK NOMLARINI YOZING ===
PACK_NAMES = [
    "pixstars",
    "Reach_Emoji",
    "techbybirdanimatedemoji",
    "CenterOfPacks66572647",
    "EmojiCatalogbot0060",
    "emojisbyisakovkhusniddin",
    "ApplicationEmoji",
    "TgPremiumIcon",
    "NXDAMA_by_fStikBot",
    "IconsInTg",
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
                    emoji_char = ""
                    for attr in sticker.attributes:
                        # alt - bu emoji belgisi (ⓘ, 💎, ⭐ va h.k.)
                        if hasattr(attr, 'alt'):
                            emoji_char = attr.alt
                            break

                    # ID va emoji belgisini yonma-yon yozamiz
                    line = f"{sticker.id} | {emoji_char}\n"
                    f.write(line)
                    print(f"  ID: {sticker.id}  Emoji: {emoji_char}")

        print(f"\n✅ Barcha ID va emojilar '{OUTPUT_FILE}' fayliga yozildi!")


import asyncio
asyncio.run(main())
