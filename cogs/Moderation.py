import discord
from discord.ext import commands, tasks
import random

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moderation.py is ready!")

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, members: commands.Greedy[discord.Member]=None, *, reason=None):
        if not members:
            return await ctx.send("Kick ai mậy ?")
        if not reason:
            reason = "Xui thì chịu biết sao giờ"
        for member in members:
            await member.kick()
        conf_embed = discord.Embed(title="Thành công!", color=discord.Colour.green())
        conf_embed.add_field(
            name = "Kicked:",
            value = f"{members} đã cút khỏi server bởi {ctx.author.mention}.",
            inline = True
        )
        conf_embed.add_field(
            name = "Lí do:",
            value = reason,
            inline = False
        )
        await ctx.send(embed = conf_embed)
async def setup(client):
    await client.add_cog(Moderation(client))