from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("AAMCAQADGQEAAQktfmBtezibMP9_oZV8zIp6SxncLhliAAJxAgAC84cJRaIKTccldi4Qmd6ZTBcAAwEAB20AAzRMAAIeBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [The Shashank](https://t.me/TheShashank).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://github.com/theshashankk/GroupMusicPlayerBot")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/WhiteDevil_Support"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/whitedevilot"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/The_ShashankMusicBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/whitedevilot")
                ]
            ]
        )
   )


