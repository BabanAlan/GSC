import discord
from discord import app_commands
from discord.ext import commands
from discord_slash import SlashCommand
from config import settings

import discord                     
from discord.ext import commands
import discord_slash    


bot = commands.Bot(command_prefix='!')

slash = discord_slash.SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print("Bot is online")

@slash.slash(name="test", description="Those burgers look tasty",
             options=[discord_slash.manage_commands.create_option(name="first_option", description="Please enter what you want on your burger", option_type=3, required=False)])
async def test(ctx: discord_slash.SlashContext, first_option): 
    await ctx.send(f'I am now gonna get you a burger with {first_option}')

bot.run("ODE0MzIyMTU5Mzc5MjgzOTY4.GQFR7O.nNaEzoBm76pI_LOqaGmM6vtJ4gGvRh2BjPoFAM")