from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey,β¨
I can play music in your group's voice call. Developed by @grootmini
Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "CREATOR", url="https://t.me/grootmini")
                  ],[
                    InlineKeyboardButton(
                        "π° GROUPπ°", url="https://t.me/"
                    ),
                    InlineKeyboardButton(
                        "ποΈ COMMANDS ποΈ", url="https://telegra.ph/MusicBot-Robot-MusicBot-Robo-03-14"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "π ADD ME TO YOUR GROUP π", url="https://t.me/Mini_musicRoBoT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Hey I'm Alive and ready To Play music π₯ β**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "MOI CREATOR π€π»", url="https://t.me/grootmini")
                ]
            ]
        )
   )

