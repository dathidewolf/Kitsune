import discord
import traceback
import psutil
import os
import random
import asyncio

from datetime import datetime
from discord.ext.commands import errors
from ut import default, permissions


async def send_cmd_help(kit):
    if kit.invoked_subcommand:
        _help = await kit.bot.formatter.format_help_for(kit, kit.invoked_subcommand)
    else:
        _help = await kit.bot.formatter.format_help_for(kit, kit.command)

    for page in _help:
        await kit.send(page)


class Events:
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






    async def on_command_error(self, kit, err):
        if isinstance(err, errors.MissingRequiredArgument) or isinstance(err, errors.BadArgument):
            await send_cmd_help(kit)

        elif isinstance(err, errors.CommandInvokeError):
            err = err.original

            _traceback = traceback.format_tb(err.__traceback__)
            _traceback = ''.join(_traceback)
            error = ('```py\n{2}{0}: {3}\n```').format(type(err).__name__, kit.message.content, _traceback, err)

            await kit.send(f"Error:\n{error}")

        elif isinstance(err, errors.CheckFailure):
            pass

        elif isinstance(err, errors.CommandOnCooldown):
            embed = discord.Embed(
                title="Ratelimit <:Harold1:483523859178323979>",
            description=f"you can use this command in {err.retry_after:.0f} seconds.",
            color=0xff0000
             )
            embed.set_footer(text='Kitsune#0602'.format(kit.author))
            await kit.send(embed=embed)

        elif isinstance(err, errors.CommandNotFound):
            pass

    async def on_guild_join(self, guild): # stolenedndndn sorry dad
        members = set(guild.members)
        bots = filter(lambda m: m.bot, members)
        bots = set(bots)
        members = len(members) - len(bots)
        try:
            to_send = sorted([chan for chan in guild.channels if chan.permissions_for(guild.me).send_messages and isinstance(chan, discord.TextChannel)], key=lambda x: x.position)[0]
            try:
                invite_chan = sorted([chan for chan in guild.channels if chan.permissions_for(guild.me).create_instant_invite and isinstance(chan, discord.TextChannel)], key=lambda x: x.position)[0]
                invite = await invite_chan.create_invite(reason="Don't mind me :eyes:")
            except:
                invite_msg = "**Invite Unavailable**"
        except IndexError:
            pass
        else:
            await to_send.send("Hello! my prefix is Kit- or you can mention me! *If you want to use the beta just use K-*")
            invite_msg = f"[**Guild Invite**]({invite})"
        if len(bots) > members:
            sketchy_msg = "\n<:blobdoggothink:444122378260185088> **More Bots than users**"
        else:
            sketchy_msg = ""

        channel = self.bot.get_channel(474290279994884096) # channel ID goes here
        join = discord.Embed(title="Added to Guild ", description=f"» Name: {guild.name}\n» ID: {guild.id}\n» Reigion: {guild.region}\n» Members/Bots: `{members}:{len(bots)}`\n» Owner: {guild.owner}{sketchy_msg}\n» {invite_msg}", color=0xff00da)
        join.set_thumbnail(url=guild.icon_url)
        join.set_footer(text=f"Total Guilds: {len(self.bot.guilds)}")
        await channel.send(embed=join)

    async def on_guild_remove(self, guild):
        channel = self.bot.get_channel(474290279994884096) # channel ID goes here
        members = set(guild.members)
        bots = filter(lambda m: m.bot, members)
        bots = set(bots)
        members = len(members) - len(bots)
        leave = discord.Embed(title="Removed from Guild", description=f"» Name: {guild.name}\n» ID: {guild.id}\n» Region: {guild.region}\n» Members/Bots: `{members}:{len(bots)}`\n» Owner: {guild.owner}", color=0x9905ac)
        leave.set_thumbnail(url=guild.icon_url)
        leave.set_footer(text=f"Total Guilds: {len(self.bot.guilds)}")
        await channel.send(embed=leave)


    async def on_message_edit(self, before, after): # dont kill me daddy skull
        if not self.bot.is_ready() or after.author.bot or not permissions.can_send(after):
            return


        await self.bot.process_commands(after)

    async def on_ready(self):
        if not hasattr(self.bot, 'uptime'):
            self.bot.uptime = datetime.utcnow()

        print("Magic almost fully charged...")
        await asyncio.sleep(3)
        print("Magic charged!")
        print(
            "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f'Ready: {self.bot.user} | Servers: {len(self.bot.guilds)} | Users: {len(set(self.bot.get_all_members()))}')
        print(f'\nCogs Loaded: {", ".join(list(self.bot.cogs))}')
        await self.bot.change_presence(activity=discord.Game(type=0, name=f"with {self.gettotalusers()} users  | Kit-help"), status=discord.Status.online)


def setup(bot):
    bot.add_cog(Events(bot))
