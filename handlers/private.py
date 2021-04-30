from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey,{BOT_NAME} ✨
I can play music in your group's voice call. Developed by [Agastya](https://t.me/smile_of_your_face).
Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "CREATOR", url="https://t.me/smile_of_your_face")
                  ],[
                    InlineKeyboardButton(
                        "🔰 GROUP🔰", url="https://t.me/worldwidebesties"
                    ),
                    InlineKeyboardButton(
                        "🎛️ COMMANDS 🎛️", url="https://telegra.ph/MusicBot-Robot-MusicBot-Robo-03-14"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "😎 ADD ME TO YOUR GROUP 😎", url="https://t.me/alone_music_robot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**✨{BOT_NAME} ✨ is on fire 🔥 ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "MOI CREATOR 🤙🏻", url="https://t.me/smile_of_your_face")
                ]
            ]
        )
   )

