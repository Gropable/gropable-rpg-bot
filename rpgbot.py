import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
bot = commands.Bot(command_prefix="&")
@bot.event
async def on_ready():
    print("I'm running on " + bot.user.name + " with the ID " + bot.user.id)
    

bot.run("NDQ5NjczOTIyNTY5NTY4MjU3.Deo5gg.HUnK9LHFpH7V9r76HB-dUIlPomA")