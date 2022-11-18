import asyncio
import logging
import re
import threading


from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, ContextTypes, MessageHandler, filters

from main.common.business.IOsystem.command_queue import CommandQueue
from main.common.business.models.command_class import Command

API_KEY = '5717554569:AAEvqbY_n85M0zVNpkBd03dFD0PyhiO52BM'
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
handler_app = ApplicationBuilder().token(API_KEY).build()
bot = Bot(API_KEY)
command_queue = CommandQueue()

def set_command_queue(new_command_queue: CommandQueue)
    command_queue = new_command_queue


async def run_bot(response_queue):
    while True:
        response = response_queue.get_response()
        await bot.send_message(response.user_id, response.message)


def start_bot(response_queue):
    asyncio.run(run_bot(response_queue))


def start_bot_thread():
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()


def format_command_arguments(arguments=''):
    message = arguments.casefold()
    command_arguments = message.split()
    command_arguments.pop(0)
    return command_arguments


def format_command(command):
    prepared_command = command.casefold()
    prepared_command = prepared_command.split()
    prepared_command = prepared_command.pop(0)
    prepared_command = re.sub(r'\A/', '', prepared_command)
    return prepared_command


def send_command(user_id, command, command_arguments):
    command = format_command(command)
    command_args = format_command_arguments(command_arguments)
    asembled_command = Command(user_id=user_id, command=command, command_arguments=command_args)
    command_queue.add_command(asembled_command)


async def universal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    send_command(update.effective_user.id, update.message.text, update.message.text)


universal_handler = MessageHandler(filters.COMMAND, universal_command)
handler_app.add_handler(universal_handler)
