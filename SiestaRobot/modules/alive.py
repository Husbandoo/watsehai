import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/a53d70bd26de174b8f1a2.mp4"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Kon'nichiwa!! [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Kaguya Shinomiya.** \n\n"
  TEXT += "◈ **I'm Working Properly Baka!!** \n\n"
  TEXT += f"◈ **My President : [Husbando をに](https://t.me/Husbandoo)** \n\n"
  TEXT += f"◈ **Library Version :** `{telever}` \n\n"
  TEXT += f"◈ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"◈ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here**"
  BUTTON = [[Button.url("ᴜᴘᴅᴀᴛᴇs", "https://t.me/Shinomiyaupdates"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/Shinomiyasupport"), 
                       Button.url("ᴘʀᴇꜱɪᴅᴇɴᴛ", "https://t.me/Husbandoo")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
