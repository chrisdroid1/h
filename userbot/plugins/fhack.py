# Modified by @Hackintush
import asyncio

from telethon import events

from userbot import CMD_HELP
from userbot import bot as cipherx

SHUTDOWN = "https://filetolinktelegrambot.herokuapp.com/41750275203384/voice.ogg"
STARTUP = "https://filetolinktelegrambot.herokuapp.com/41767455072568/funny.gif.mp4"


@cipherx.on(events.NewMessage(pattern=r"\.fhack", outgoing=True))
async def _(event):
    await event.client.send_file(
        event.chat_id,
        STARTUP,
        caption="`You will be Hacked in a Moment by šš©šš šØ šš¦š¤š„š±š«š¦š«š¤ Bot.`",
        voice_note=True,
    ),
    await event.client.send_file(
        event.chat_id, SHUTDOWN, caption="`Hacking in progress...`", voice_note=True
    )
    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    animation_chars = [
        "`Connecting To šš©šš šØ šš¦š¤š„š±š«š¦š«š¤ Server...`",
        "`Target Selected.`",
        "`Hacking... 0%\nāāāāāāāāāāāāāāāāāāāāāāāāā `\n`Looking for Telegram Data...`\nETA: 0m, 20s",
        "`Hacking... 4%\nāāāāāāāāāāāāāāāāāāāāāāāāā `\n`Found SD Directory...`\n`Looking for Telegram Data : ā`\nETA: 0m, 10s",
        "`Hacking... 8%\nāāāāāāāāāāāāāāāāāāāāāāāāā `\n`Searching for Databases....`\n`Looking for Telegram Data : ā`\n`Found Telegram Database Directory : ā `\nETA: 0m, 15s",
        "`Hacking... 20%\nāāāāāāāāāāāāāāāāāāāāāāāāā`\n`Found msgstore.db.crypt12...`\n`Looking for Telegram Data : ā`\n`Found Telegram Database Directory : ā `\n`Searching for Databases : ā `\nETA: 0m, 09s",
        "`Hacking... 36%\nāāāāāāāāāāāāāāāāāāāāāāāāā `\n`Trying to Decrypt...`\n`Looking for Telegram Data : ā`\n`Found Telegram Database Directory : ā\n`Searching for Databases : ā`\n`Found msgstore.db.crypt12 :  ā`\n`ā ļø error occurred ..`\nETA: 0m, 25s",
        "`Hacking... 52%\nāāāāāāāāāāāāāāāāāāāāāāāāā `\n`Decryption successful!`\n`Looking for Telegram Data : ā`\n`ā ļø error occurred ..`\n`Found Telegram Database Directory : ā`\n`ā ļø Error Occurred ...`\n`Searching for Databases : ā`\n`Found msgstore.db.crypt12 :  ā`\nETA: 0m, 25s",
        "`Hacking... 84%\nāāāāāāāāāāāāāāāāāāāāāāāāā `\n`Scanning file...`\n`Looking for Telegram Data : ā`\n`ā ļø error occurred ..`\n`Found Telegram Database Directory : ā`\n`ā ļø Error Occurred ..`\n`ā ļø Error Occurred ...`\n`Searching for Databases : ā`\n`Found msgstore.db.crypt12 :  ā`\n`Scanning File :  ā`\nETA: 0m, 16s",
        "`Hacking... 100%\n` 98% HACKED`",
        "`Targeted Account Hacked By šš©šš šØ šš¦š¤š„š±š«š¦š«š¤`\n`_______________________`\n`result ... :)`\n\n`Chatlist : ā`\n`Calls : ā`\n`groups : ā`\n `Contacts : ā`\n`Channel : ā`\n`Deleted Messages : ā`\n`Edited Messages : ā`\n`All API Tokens : ā`",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 11])


CMD_HELP.update(
    {
        "fhack": "**Fhack**\
\n\n**Syntax : **`.fhack`\
\n**Usage :** Fun Hacking Plugin"
    }
)
