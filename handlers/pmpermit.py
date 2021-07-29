from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hlo dear 🥰, This is a music assistant service .\n\n 🙃 Rules:\n   - No chatting allowed\n  - You will get non reply beacause it is a bot\n  - No spam allowed \n\n 👉 **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN'T JOIN YOUR GROUP.**\n\n This Is very easy and comfortablein ise with 0% risk!!\n    - If you have any issue and doubt 🧐 just contact @sokapgblg\n   - Thanks For Using ZEEN MUSIC\n\n")
  return
