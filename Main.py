import messages
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)

#sync the commands
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="rules")
async def rules_command(interaction: discord.Interaction):
    await interaction.response.defer()
    channel = interaction.channel
    await channel.send(embeds=[
        messages.Rules0,
        messages.Rules1,
        messages.Rules2,
        messages.Rules3,
        messages.Rules4,
        messages.Rules5
    ])

bot.run(token, log_handler=handler, log_level=logging.DEBUG)