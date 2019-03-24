# 5YR Bot by Stiindox  & Nuk3lar
# This bot is designed to only work on the 5YR Discord Server (https://discord.gg/gQ6N7qf)

# Main imports

import discord, sys, asyncio, logging, traceback, time
from config.config import conf_json, cwdmain, Client, bot, mode, botkey, loaded_parts, buildid, logging

# Startup function

def _startup():
    logging.info("[MAIN] BOT STARTING")
    print('==== 5YR bot booting ====')
    print(f'[Bot] {mode}')
    print(f'[Platform] {sys.platform}\n[CWD] {cwdmain}\n[Build] #{buildid}')
    if sys.platform == "linux":
        discord.opus.load_opus(f'{cwdmain}/_bin/libopus.so')
        if discord.opus.is_loaded() == True: print('[Library] Opus Loaded')
    else: print('[Library] Opus not needed on Win32')

def _load_part(part, succ, fail):
    try:
        bot.load_extension(part)
        logging.info("[COGS] LOADING "+part)
        succ += 1
        loaded_parts.append(part)
    except Exception as e:
        logging.error('[COGS] FAILED TO LOAD: '+part)
        logging.error(f'[COGS] ERROR:\n{e}')
        fail += 1
    return succ, fail
    
def _load_parts(parts):
    logging.info("[MAIN] LOADING COGS")
    print('[Cogs] Loading Cogs as defined in config/config.json')
    succ = 0
    fail = 0
    for part in parts: succ, fail = _load_part(part, succ, fail)
    print(f"[Cogs] {succ} Loaded : {fail} Failed to load.")
    
if __name__ == "__main__":
    _startup()
    _load_parts(conf_json["parts"])
    
bot.run(botkey, bot=True, reconnect=True)