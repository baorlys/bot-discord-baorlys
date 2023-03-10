#Library
import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
import os
from dotenv import load_dotenv
import asyncio
load_dotenv()



client = commands.Bot(command_prefix=">", intents=discord.Intents.all())
TOKEN = os.environ.get("TOKEN")
bot_status = cycle(["'>helpme for help'", "Hồng Phúc", "U70 trẻ đẹp"])

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))


@client.event
async def on_ready():
    print("Success: Bot is connected!")
    change_status.start()


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start(TOKEN)




asyncio.run(main())
