import time
import aiohttp
import discord
import asyncio
import re
import subprocess
import os
import asyncio


from discord import Webhook, AsyncWebhookAdapter
from io import BytesIO
from ut import permissions, default
from discord.ext import commands
from io import BytesIO
from ut import repo, default, http, dataIO


class breaking:
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("conf.json")
#webhook for bans # yeet yeet 
#webhook for kicks Y E E T
    @commands.command(aliases=['bant'])
    @commands.check(repo.is_owner)
    @commands.guild_only()
    async def banmessage(self, kit, userid: int, *, reason: str):
        """testing ban thingy"""
        # taking this out

    @commands.command(aliases=['kickt'])
    @commands.check(repo.is_owner)
    @commands.guild_only()
    async def kickmessage(self, kit, userid: int, *, reason: str):
        """testing kick thingy"""
        # and this

    @commands.command()
    @commands.check(repo.is_owner)
    async def st(self, kit):
        """Speedtest.net results"""
        rb = "```rb\n{0}\n```"
        await kit.channel.trigger_typing()
        await asyncio.sleep(3)
        await kit.send("This may take a while...")
        msg = "speedtest-cli --share --simple"
        input = os.popen(msg)
        output = input.read()
        await kit.send(rb.format(output))
        #you can keep this shitty thing


    @commands.command()
    @commands.check(repo.is_owner)
    async def cmc(self, kit, *, alice: str):
        """do some CMD stuffs"""
        #cant have this one tho




def setup(bot):
    bot.add_cog(breaking(bot))
