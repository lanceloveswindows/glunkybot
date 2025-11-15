import os
import discord
from discord.ext import commands

# Get the bot token from an environment variable (do NOT hardcode your token)
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise RuntimeError("Missing TOKEN environment variable. Set TOKEN in Railway variables.")

# Basic intents (message content intent not required for prefix commands unless you need it)
intents = discord.Intents.default()
intents.message_content = True

# Choose a command prefix (e.g. '!')
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (id: {bot.user.id})")
    print("------")

@bot.tree.command(name="glunky")
async def glunky(interaction: discord.Interaction):
    await ctx.send("I'm sorry 🥺")

if __name__ == "__main__":
    bot.run(TOKEN)
