import discord

from discord import utils

@bot.command(pass_content = True)
async def ping():
    await bot.say('Pong!')