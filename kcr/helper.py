import time
import aiohttp
import discord
import asyncio

from asyncio.subprocess import PIPE
from discord.ext import commands
from io import BytesIO
from ut import repo, default, http, dataIO


class Helper:
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("conf.json")
        self._last_result = None



    @commands.group()
    @commands.check(repo.is_helper)
    async def helper(self, kit):
        if kit.invoked_subcommand is None:
            _help = await kit.bot.formatter.format_help_for(kit, kit.command)

            for page in _help:
                await kit.send(page)

    @helper.command(name="guild")
    @commands.check(repo.is_helper)
    async def guilds(self, kit):
        """Sends guilds"""
        await kit.send('some weird dev shit with guids')
        await kit.send(kit.bot.guilds)


    @helper.command(name="status")
    @commands.check(repo.is_helper)
    async def changestats(self, kit, status: str):
        '''there was german shit here ;-;'''
        status = status.lower()
        if status == 'offline' or status == 'off' or status == 'invisible':
            discordStatus = discord.Status.invisible
        elif status == 'idle':
            discordStatus = discord.Status.idle
        elif status == 'dnd' or status == 'disturb':
            discordStatus = discord.Status.dnd
        elif status == 'online' or status == 'on':
            discordStatus = discord.Status.online
        await self.bot.change_presence(status=discordStatus)
        await kit.send(f'**:ok:** Changed status to: **{discordStatus}**')


    @helper.command(name="dm")
    @commands.check(repo.is_helper)
    async def DM(self, kit, id: int, message: str):
        """Dm somebody"""
        user = self.bot.get_user(id)
        if user is not None:
            await user.send(message)
            await kit.send("message sent (i think?)")

def setup(bot):
    bot.add_cog(Helper(bot))
