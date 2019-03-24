# Modules

import discord, sys, asyncio, logging, traceback, MySQLdb, json
from discord.ext.commands import Bot
from discord.ext import commands
from config.cwd import cwdmain

# JSON handing

if sys.platform == "win32": 
    with open(f"{cwdmain}\\config\\config.json") as json_file: conf_json = json.load(json_file)
    with open(rf"{cwdmain}\\config\secretkeys.json") as json_file: keys = json.load(json_file)
else: 
    with open(f"{cwdmain}/config/config.json") as json_file: conf_json = json.load(json_file)
    with open(f"{cwdmain}/config/secretkeys.json") as json_file: keys = json.load(json_file)

# Defining Client & Bot

Client = discord.Client()
bot = commands.Bot(command_prefix = "~~")

# Mode Selection

print("======== Mode Selection ========")
print("Defaults to main bot")
print(" 1 | Main bot")
print(" 2 | Development bot")

modeselect = input('Select mode, or press enter to default: ')

if modeselect == "1":
    botkey = keys["keys"]["main"]
    mode = "Main bot"
elif modeselect == "2":
    botkey = keys["keys"]["dev"]
    mode = "Development Bot"
elif modeselect == "":
    botkey = keys["keys"]["main"]
    mode = "Main bot"
else:
    botkey = keys["keys"]["main"]
    print("Invalid Entry, defaulting to main bot")
    mode = "Main bot"

loaded_parts = [] # Loaded cogs decleration
logging.basicConfig(filename='output.log', filemode='w', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s') # Logging Config

# Build ID

if sys.platform == "linux":
    with open(f"{cwdmain}/buildid.txt", "r") as f:
        buildid=f.read()
        f.close()
if sys.platform == "win32":
    with open(f"{cwdmain}\\buildid.txt", "r") as f:
        buildid=f.read()
        f.close()

def setup(bot): pass