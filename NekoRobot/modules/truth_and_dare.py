import asyncio
import datetime
import re
from datetime import datetime

from telethon import custom, events

from NekoRobot import tbot as bot
from NekoRobot import tbot as tgbot
from NekoRobot.events import register

@register(pattern="^/truth ?(.*)")

def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))

@register(pattern="^/dare ?(.*)")

def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth, run_async=True)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare, run_async=True)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
