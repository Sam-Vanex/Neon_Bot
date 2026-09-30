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
    await interaction.response.send_message(embeds=[
        messages.Rules0,
        messages.Rules1,
        messages.Rules2,
        messages.Rules3,
        messages.Rules4,
        messages.Rules5])

@bot.tree.command(name="stream_notification", description="Sends a notification that the livestream has started", guild=discord.Object(id=1496509654270873681)) ### GUILD REMOVE AFTER TEST
async def Stream_notification(interaction: discord.Interaction):
    """Send the livestream notification embed and notify everyone.
    
    Args:
        interaction: The Discord interaction generated when a user executes the /rules slash command.
    """

    await interaction.response.send_message(content="@everyone", embed=Stream_notification)

async def setup_roles(guild: discord.Guild):
    """Create required server roles if they do not already exist.
    
    Args:
        guild: The guild where you want the roles set up.
    """

    #Twitch sub role.
    if discord.utils.get(guild.roles, name="Twitch_Subscriber") is None:
        await guild.create_role(name="Twitch_Subscriber", color=discord.Colour.from_str("#9146FF"), permissions=discord.Permissions.none())

    #Youtube member role.
    if discord.utils.get(guild.roles, name="Youtube_Member") is None:
        await guild.create_role(name="Youtube_Member", color=discord.Colour.from_str("#FF0000"), permissions=discord.Permissions.none())


@bot.event
async def on_ready():
    """Runs once the bot has successfully connected to Discord.
    """
    
    # Synchronize the bot's application commands with Discord.
    synced = await bot.tree.sync(guild=discord.Object(id=1496509654270873681)) ### REMOVE GUILD AFTER TESTING

    for command in synced:
        print(f"- /{command.name}")

    # Check if all the roles exist.
    await setup_roles(bot.guilds[0])

    print(f"Logged in as {bot.user}")



# Start the bot.
bot.run(TOKEN)