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
        print("synced" + len(synced) + "commands")
    except Exception as e:
        print(e)

@bot.tree.command(name="apology", description="Make Glunk apologise for his sins")
async def glunky(interaction: discord.Interaction):
    await interaction.response.send_message("I'm sorry 🥺")

@bot.tree.command(name="bald", description="Tell Glunk how bald Martin is")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Martin is not bald, he is baldING!")

@bot.tree.command(name="say", description="Make Glunk say something")
async def say(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message)


if __name__ == "__main__":
    bot.run(TOKEN)
