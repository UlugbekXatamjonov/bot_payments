import logging

from aiogram import Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    # for admin in ADMINS:
    #     try:
            await dp.bot.send_message(1012480055, "Bot ishga tushdi")

        # except Exception as err:
        #     logging.exception(err)
