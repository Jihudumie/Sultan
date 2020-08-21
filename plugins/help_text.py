#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Ribbiyyuwna

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase


@pyrogram.Client.on_message(pyrogram.Filters.command(["help", "about"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/start")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["hamis", "jihaad"]))
async def upgrade(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/hamis")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HAMIS_MAJIBU,
        parse_mode="html",
        reply_to_message_id=update.message_id,
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["wakweli", "almuhajir"]))
async def wakweli(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "wakweli")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.WAKWELI,
        parse_mode="html",
        reply_to_message_id=update.message_id,
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["aliswod"]))
async def aliswod(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "aliswod")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ALISWOD,
        reply_to_message_id=update.message_id
    )

