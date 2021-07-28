from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CUJU0dgACAppgyWsRKZJ0W4hbRKdVMYuxwb50wwACgxcAAtqjlSw9sWir1m6CTx8E")
    await message.reply_text(
        f"""**Hallo👋🏻 {message.from_user.first_name}!

🔥 I am Zeen Music Player. 

🔥 I can play music in your Telegram Group's Voice Chat😉

Developed by ⚡ @sokapgblg ⚡


My commands - type  /help to get commands, which work in group

Thanks for using {BOT_NAME}

**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👑 Owner", url="https://t.me/sokapgblg
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/Kingbot_Music_Bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🔥ZEEN MUSIC PLAYER IS ALWAYS ACTIVE!!**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Tanya-Tanya klik disini", url="https://t.me/sokapgblg")
                ]
            ]
        )
   )
