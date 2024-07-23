from datetime import datetime, timedelta
from pyrogram import Client, filters

with open("userbot.info", "r") as file:
    lines = file.readlines()
    prefix_userbot = lines[2].strip()

afk_mode = False
afk_reason = ""
afk_start_time = 0
cinfo = f"😴`{prefix_userbot}afk`", f"🥱`{prefix_userbot}afkoff`"
ccomand = " включает AFK-режим.", " отключает AFK-режим."


def command_afk(app):
    @app.on_message(filters.me & filters.command("afk", prefixes=prefix_userbot))
    def set_afk_mode(_, message):
        global afk_mode, afk_reason, afk_start_time
        afk_mode = True
        afk_reason = " ".join(message.command[1:])
        afk_start_time = datetime.now()
        message.edit_text("**😴AFK-режим включён!**")

    @app.on_message(filters.mentioned)
    def check_afk(_, message):
        if afk_mode:
            current_time = datetime.now()
            time_diff = current_time - afk_start_time
            time_diff_str = str(time_diff).split('.')[0]
            message.reply_text(f"**💤Пользователь сейчас в AFK. \nВремя - {time_diff_str} \nПричина - {afk_reason}**")

    @app.on_message(filters.me & filters.command("afkoff", prefixes=prefix_userbot))
    def unset_afk_mode(_, message):
        global afk_mode
        afk_mode = False
        message.edit_text("**🥱AFK-режим выключен!**")

print(f"Модуль afk загружен!")
