import discord
from discord.ext import commands, tasks

class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Test.py is ready!")

    @commands.command()
    async def test(self, ctx):
        embed=discord.Embed()
        embed.add_field(name="undefined", value="undefined", inline=False)
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(Test(client))