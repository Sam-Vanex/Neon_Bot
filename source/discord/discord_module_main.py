import discord
from discord.ext import commands

from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path(__file__).resolve().parents[2] / "config" / ".env")

TOKEN = os.getenv("DISCORD_API_KEY")
INTENTS = discord.Intents()

bot = commands.bot(intents=INTENTS)

