from dotenv import load_dotenv
from pathlib import Path
import os

import discord
from discord.ext import commands

import messages

# Load environment variables from the project's .env file.
load_dotenv(Path(__file__).resolve().parents[2] / "config" / ".env")

# Retrieve the Discord bot token from the environment.
TOKEN = os.getenv("DISCORD_API_KEY")
# Create the Discord intents configuration.
INTENTS = discord.Intents()

# Create the Discord bot instance.
bot = commands.Bot(command_prefix="!", intents=INTENTS)



@bot.tree.command(name="rules", description="Shows the server rules in current channel.")           ### REMOVE THE RESPONESE TO ONE WHO DOES COMMAND
async def Rules(interaction: discord.Interaction):
    """Display the server rules as a series of Discord embeds.

    Args:
        interaction: The Discord interaction generated when a user executes the /rules slash command.
    """
    await interaction.response.defer()
    await interaction.followup.send(embeds=[
        messages.Rules0,
        messages.Rules1,
        messages.Rules2,
        messages.Rules3,
        messages.Rules4,
        messages.Rules5
    ])

async def setup_roles(guild: discord.Guild):
    """Create required server roles if they do not already exist."""

    

    for role_name in ROLE_NAMES:
        role = discord.utils.get(guild.roles, name=role_name)

        if role is None:
            await guild.create_role(
                name=role_name,
                reason="Required bot role"
            )
            print(f"Created role: {role_name}")


@bot.event
async def on_ready():
    """Runs once the bot has successfully connected to Discord.
    """
    
    # Synchronize the bot's application commands with Discord.
    await bot.tree.sync()

    print(f"Logged in as {bot.user}")



# Start the bot.
bot.run(TOKEN)