"""Executes when bot package runs."""
from os import getenv
from discord import Intents
from dotenv import load_dotenv

from bot import Bot
from log import setup_logger

load_dotenv()

# Setups logger
setup_logger(LOG_LEVEL)


# Starts the bot
TOKEN = getenv("TOKEN")

bot = Bot(
    command_prefix=".",
    intents=Intents.all(),
    
)
bot.run(TOKEN)
