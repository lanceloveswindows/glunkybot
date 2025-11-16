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
intents.message_content = True

# Choose a command prefix (e.g. '!')
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print("synced" + len(synced) + "commands")
    except Exception as e:
        print(e)

@bot.tree.command(name="say", description="Make Glunk say something")
async def say(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()

    # Trigger 1
    if "glunk" in content or "glunky" in content:
        await message.channel.send("I'm sorry 🥺")

    # Trigger 2
    if "martin" in content or "bald" in content:
        await message.channel.send("Martin is not bald, he is baldING!")

    if "nadine" in content or "food" in content:
        await message.channel.send("Luckily, Nadine has fed me in the last week.")

    if "1502" in content or  "get up" in content:
        await message.channel.send("Cameron, get up: https://www.youtube.com/watch?v=l47q2EY8Jjs")

    # Allows slash commands & prefix commands to keep working
    await bot.process_commands(message)

if __name__ == "__main__":
    bot.run(TOKEN)
