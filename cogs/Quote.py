import discord
from discord.ext import commands, tasks
import random

class Quote(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Quote.py is ready!")

    @commands.command()
    async def quote(self, ctx):
        with open("quote_tafi.txt", "r", encoding="utf8") as f:
            random_res = f.readlines()
            res = random.choice(random_res)
        embed_message = discord.Embed(title="Những câu nói hay", description=res, color=discord.Color.random())
        embed_message.set_thumbnail(url="https://iili.io/HY6CIC7.jpg")
        await ctx.send(embed = embed_message)

async def setup(client):
    await client.add_cog(Quote(client))