import random
import discord
import json

from io import BytesIO
from discord.ext import commands
from ut import lists, permissions, http, default
from ut import repo


class embeds:
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("conf.json")



    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def embed(self, kit, etitle: str, *, edescription: str):
        """makes you a embed"""
        embed = discord.Embed(title=etitle, description=edescription, color=0xff0000)
        embed.set_footer(text='Requested by:\n{0}'.format(kit.author))
        await kit.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def embed1(self, kit, etitle: str, *, edescription: str):
        """makes you a embed then deleted the command that invoked it"""
        embed = discord.Embed(title=etitle, description=edescription, color=0xff0000)
        embed.set_footer(text='Requested by:\n{0}'.format(kit.author))
        await kit.send(embed=embed)
        await kit.message.delete()

    @commands.command(hidden=True)
    @commands.check(repo.is_owner)
    async def ki1(self, kit, etitle: str, *, edescription: str):
###################################################################

def setup(bot):
    bot.add_cog(embeds(bot))
