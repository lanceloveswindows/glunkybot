import os
import discord
from discord.ext import commands
from discord import app_commands

# Get the bot token from an environment variable (do NOT hardcode your token)
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise RuntimeError("Missing TOKEN environment variable. Set TOKEN in Railway variables.")

# Basic intents (message_content not needed for slash commands)
intents = discord.Intents.default()

# Choose a command prefix (e.g. '!')
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()

@bot.tree.command(name="glunky")
async def glunky(interaction: discord.Interaction):
    await interaction.response.send_message("I'm sorry 🥺")

if __name__ == "__main__":
    bot.run(TOKEN)
