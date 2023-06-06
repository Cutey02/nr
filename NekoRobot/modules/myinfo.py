import asyncio
import datetime
import re
from datetime import datetime

from telethon import custom, events

from NekoRobot import tbot as bot
from NekoRobot import tbot as tgbot
from NekoRobot.events import register

edit_time = 5
""" =======================ᴘɪᴋᴀᴄʜᴏᴏ====================== """
file1 = "https://graph.org/file/8b464c9cb731a0fe73bcb.jpg"
file2 = "https://graph.org/file/8b464c9cb731a0fe73bcb.jpg"
file3 = "https://graph.org/file/8b464c9cb731a0fe73bcb.jpg"
file4 = "https://graph.org/file/8b464c9cb731a0fe73bcb.jpg"
file5 = "https://graph.org/file/8b464c9cb731a0fe73bcb.jpg"
""" =======================ᴘɪᴋᴀᴄʜᴏᴏ====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    betsy = event.sender.first_name
    button = [[custom.Button.inline("Click Here", data="information")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"♡ 𝙷𝚎𝚢 𝙳𝚞𝚍𝚎 {betsy}, I'ᴍ Pɪᴋᴀᴄʜᴏᴏ\n♡ I'ᴍ Cʀᴇᴀᴛᴇᴅ ʙʏ [ʙᴀᴅ ʙᴏʏ](http://t.me/badboybiographfia)\n♡ Click The Button Below To Get Your Info",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        NEKO = "ʏᴏᴜʀ ᴅᴇᴛᴀɪʟs ʙʏ ᴘɪᴋᴀᴄʜᴏᴏ \n\n"
        NEKO += f"ғɪʀsᴛ ɴᴀᴍᴇ : {PRO.first_name} \n"
        NEKO += f"ʟᴀsᴛ ɴᴀᴍᴇ : {PRO.last_name}\n"
        NEKO += f"ʏᴏᴜ ʙᴏᴛ : {PRO.bot} \n"
        NEKO += f"RESTRICTED : {PRO.restricted} \n"
        NEKO += f"ᴜsᴇʀ ɪᴅ : {boy}\n"
        NEKO += f"ᴜsᴇʀɴᴀᴍᴇ : {PRO.username}\n"
        await event.answer(NEKO, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__help__ = """
/myinfo: shows your info in inline button
"""

__mod_name__ = "myinfo"
__command_list__ = ["myinfo"]
