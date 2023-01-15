import discord
from discord.ext import commands, tasks
import random

class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("HelpCommand.py is ready!")

    @commands.command()
    async def helpme(self, ctx):
        embed = discord.Embed(
            title="Bot commands",
            description="Welcome to help section. Here are all the commands !",
            color=discord.Colour.green()
        )
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/682/682055.png")
        embed.add_field(
            name=">help",
            value="List all of the commands",
            inline=True
        )
        embed.add_field(
            name=">quote",
            value="Quote of TAFI",
            inline=True
        )
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(HelpCommand(client))