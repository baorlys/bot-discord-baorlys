import discord
from discord.ext import commands, tasks

class Hi(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Hi.py is ready!")

    @commands.command()
    async def hi(self, ctx):
        await ctx.author.send("hi hi cái bầu đuồi!")

async def setup(client):
    await client.add_cog(Hi(client))