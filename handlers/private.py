from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAALkRGEDxWKxliVZ67BDsFQpR4k55o3sAAKKCAACdynwUJdQxXu13P-bHgQ")
    await message.reply_text(
        f"""**Dear {message.from_user.first_name}!

😁 I am {BOT_NAME}. 

🥳 I can play music in your Telegram Group's Voice Chat😉


⚜️You can play music On voice chat group🔱


Developed by ⚡ @sokapgblg ⚡


My commands - type  /help to get commands, which work in grp

Thanks for using .

Regrards [Kyy](https://t.me/sokapgblg)
**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥 Owner ", url="https://t.me/sokapgblg")
                  ],[
                    InlineKeyboardButton(
                        "🔊 Channel Update", url="https://t.me/zeenmusicupdate"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/zeenplayerbot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ZEEN MUSIC PLAYER IS ALWAYS ACTIVE!!**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥 Owner", url="https://t.me/sokapgblg")
                ]
            ]
        )
   )
