# Importing Modules
import discord, sys, asyncio, logging, traceback, time
from config.config import conf_json, cwdmain, Client, bot, mode, botkey, loaded_parts, buildid, logging

class help_switch_class():
    @staticmethod
    def none(): 
        embed = discord.Embed(title="Help For 5YR Bot", description="List of commands\n(part) | Required argument\n[part] | Optional argument\nDon't include the brackets which are used in the examples", color=conf_json["colors"]["embedcolordark"])
        embed.set_author(name="Stiindox & Nukelar", icon_url="")
        return embed
    #Addhere
    
        
help_switch_cases = {
    None : help_switch_class.none
    #Addhere
}

def switch( case, switch_cases, self): return switch_cases[a]

# TODO
