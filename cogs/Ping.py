import discord
from discord.ext import commands, tasks

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping.py is ready!")

    @commands.command()
    async def checkping(self, ctx):
        bot_latency = round(self.client.latency * 1000)
        high_ping = 100
        if (bot_latency > high_ping):
            await ctx.send(f"Ping tao đang hơi cao, {bot_latency} ms.")
        else:
            await ctx.send(f"Ping đang ngon, {bot_latency} ms.")

async def setup(client):
    await client.add_cog(Ping(client))