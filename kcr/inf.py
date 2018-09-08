import time
import discord
import psutil
import os
import sys
import asyncio
import aiohttp


from discord.ext import commands
from datetime import datetime
from ut import repo, default
from discord import Webhook, AsyncWebhookAdapter

class Information:
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("conf.json")
        self.process = psutil.Process(os.getpid())
        self.totalmembers = set({})



    def gettotalusers(self):
        for x in self.bot.guilds:
            for y in x.members:
                self.totalmembers.add(y.id)
        return len(self.totalmembers)


    def get_bot_uptime(self, *, brief=False):
        now = datetime.utcnow()
        delta = now - self.bot.uptime
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        if not brief:
            if days:
                fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds'
            else:
                fmt = '{h} hours, {m} minutes, and {s} seconds'
        else:
            fmt = '{h}h {m}m {s}s'
            if days:
                fmt = '{d}d ' + fmt

        return fmt.format(d=days, h=hours, m=minutes, s=seconds)

    @commands.command()
    async def owo(self, kit):
        await kit.send("Heres another great bot! > https://discordbots.org/bot/365255872181567489 ")

    @commands.command()
    async def bots(self, kit):
        """some great bots"""
        await kit.send("""some other great bots:
owopup
From a random furry comes owopup, the cutest furry bot you'll meet..!
https://discordbots.org/bot/365255872181567489
""")

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def ping(self, kit):
        """ Pong! """
        before = time.monotonic()
        message = await kit.send("<:theLook:483523876014260234>")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"""
<:pinglasses:483524563276398595>
The message round-trip took {int(ping)}ms 
The heartbeat ping {round(self.bot.latency * 1000)}ms 
""")

    @commands.command(aliases=['stats', 'status'])
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def botstats(self, kit):
        """ About the bot """
        ramUsage = self.process.memory_full_info().rss / 1024**2
        cpu_usage = round(self.process.cpu_percent() / psutil.cpu_count(), 2)
        embed = discord.Embed(colour=0xff0000)
        embed.set_thumbnail(url=kit.bot.user.avatar_url)
        embed.add_field(name="Commands", value=len([x.name for x in self.bot.commands]), inline=True)
        embed.add_field(name="Library", value="discord.py [rewrite]", inline=True)
        embed.add_field(name="Servers", value=len(kit.bot.guilds), inline=True)
        embed.add_field(name='Total Users', value=self.gettotalusers())
        embed.add_field(name="Platform", value='Linux Ubuntu 18.04 LTS', inline=True)
        embed.add_field(name="CPU Percentage", value=f"{cpu_usage}%", inline=True)
        embed.add_field(name="RAM Currently using",
                        value=f"{ramUsage:.2f} MB", inline=True)
        embed.add_field(name="Total RAM",
                        value=f"3.8 GB", inline=True)

        embed.add_field(name="Uptime", value=self.get_bot_uptime(), inline=False)

        await kit.send(embed=embed)

    @commands.command()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def about(self, kit, etitle: str, *, edescription: str):
        """info about the bot"""
        embed = discord.Embed(colour=0xff0000)
        embed.set_author()
        embed.set_thumbnail(url=kit.bot.user.avatar_url)
        embed.add_field(name="Dev[s]", value="wolfirik#4041", inline=False)
        embed.add_field(name="Admin[s]", value="""
wolfirik#4041
Syntax#0666
""", inline=True)
        embed.add_field(name="Helper[s]", value="""
wooosh_#7840
DankTanks#2608 aka Cuddles
""", inline=True)
        embed.set_footer(text='Kitsune#4041')
        await kit.send(embed=embed)

    @commands.command(aliases=['suggestions'])
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def suggest(self, kit):
        """Send me suggestions!"""
        embed = discord.Embed(title='Suggest somthing for Kitsune', description='''
Heres the form!
https://goo.gl/forms/FqrbhZwmo7KKtknf2''', color=0xff0000)
        embed.set_footer(text='Dont suggest things too crazy')
        await kit.send(embed=embed)

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def shard(self, kit):
        """Shard info."""
        shard = kit.message.guild.shard_id + 1
        em = discord.Embed(title="Your Guild is on shard:", description='{}/{}'.format(shard,self.bot.shard_count),color=discord.Color.blue())
        await kit.channel.send(embed=em)

    @commands.command(aliases=['RP'])
    @commands.cooldown(rate=1, per=15.0, type=commands.BucketType.user)
    async def report(self, kit, *, reason: str):
        """Reports a user"""
#yeet

    @commands.command(aliases=['contact'])
    @commands.cooldown(rate=1, per=8.0, type=commands.BucketType.user)
    async def feedback(self, kit, *, contact_text: str):#yeet
        """Contacts developers with a message."""





def setup(bot):
    bot.add_cog(Information(bot))
