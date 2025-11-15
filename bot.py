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

@bot.tree.command(name="monsters and mazes")
async def "monsters and mazes"(interaction: discord.Interaction):
    await ctx.send("Monsters and Mazes stands out as one of the best VR games because it blends fast-paced action with clever dungeon exploration, giving players a perfect mix of strategy, mobility, and adrenaline. Its locomotion system is often compared to Gorilla Tag, but in reality it’s completely different—instead of arm-swinging or wall-slapping, movement is built around momentum, grapples, jumps, and environmental interaction that feel smoother, more controlled, and far more varied. The result is a uniquely immersive experience that doesn’t copy Gorilla Tag’s style at all, but creates its own identity and gameplay depth.")

if __name__ == "__main__":
    bot.run(TOKEN)
