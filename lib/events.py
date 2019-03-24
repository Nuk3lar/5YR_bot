# Modules

import discord, sys, asyncio, logging, traceback, os, sys, aiohttp
from discord.ext.commands import Bot
from discord.ext import commands
from config.config import Client, bot, conf_json, buildid, cwdmain

# Changing the Status Message

async def status_task():
    while True:
        await bot.change_presence(activity=discord.Activity(name='~~help', type=0))
        await asyncio.sleep(20)
        await bot.change_presence(activity=discord.Activity(name="ARMA", type=0))
        guild = bot.get_guild(453626984128446512)
        await asyncio.sleep(20)
        await bot.change_presence(activity=discord.Activity(name=f'with {len(guild.members)} soldiers', type=0))
        await asyncio.sleep(20)

class on_ready:
    # Setup INIT
    def __init__(self, bot): self.bot = bot
    def __unload(self): pass
    @Client.event
    async def on_ready(self):
        print(f'[Bot user] {bot.user.name}\n[Bot ID] {bot.user.id}')
        logging.info("[MAIN] 5YR Bot #"+buildid+" STARTED")
        bot.loop.create_task(status_task())
        print(f'== 5YR build #{buildid} Started ==')

# For Loading Module

def setup(bot):
    bot.add_cog(on_ready(bot))