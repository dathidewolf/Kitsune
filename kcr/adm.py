import time
import aiohttp
import discord
import asyncio

from asyncio.subprocess import PIPE
from discord.ext import commands
from io import BytesIO
from ut import repo, default, http, dataIO
from ut.chat_formatting import pagify, box


class Admin:
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("conf.json")
        self._last_result = None

    @commands.command(hidden=True)
    @commands.check(repo.is_owner)
    async def id(self, kit, user: discord.Member):
        """shows a user id cause im lazy"""
        # f in chat im removing this

    @commands.command(hidden=True)
    @commands.check(repo.is_owner)
    async def DM(self, kit, id: int, message: str):
        """Dm somebody"""
        user = self.bot.get_user(id)
        if user is not None:
            await user.send(message)
            #unf
            #dm that user nicely

    @commands.command(hidden=True)
    @commands.check(repo.is_owner)
    async def cogs(self, kit):
        mod = ", ".join(list(self.bot.cogs))
        await kit.send(f"The current modules I can see are:\n{mod}")
        # oof 

    @commands.command(hidden=True)
    @commands.check(repo.is_owner)
    async def servers(self, kit):
        """Lists servers"""
        owner = kit.author
        guilds = sorted(list(self.bot.guilds),
                        key=lambda s: s.name.lower())
        msg = ""
        for i, guild in enumerate(guilds, 1):
            members = set(guild.members)
            bots = filter(lambda m: m.bot, members)
            bots = set(bots)
            members = len(members) - len(bots)
            msg += "`{}:` {} `{} members, {} bots` \n".format(i, guild.name, members, len(bots))

        for page in pagify(msg, ['\n']):
            await kit.send(page)
            # oof oof not mine


    @commands.command(hidden=True)
    @commands.check(repo.is_owner)
    async def changestats(self, kit, status: str):
        '''Changes status'''
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
        #yeet yeet

    @commands.command(hidden=True)
    @commands.check(repo.is_owner)
    async def leaves(self, kit, guild: int):
        """leaves a server, thanks to wooosh for the help"""
        # yeet yeet taking this out too

    @commands.command(hidden=True)
    @commands.check(repo.is_owner)
    async def guilds(self, kit):
        """Sends guilds"""
        await kit.send('some weird dev shit with guids')
        await kit.send(kit.bot.guilds)

    @commands.command(hidden=True)
    @commands.check(repo.is_owner)
    async def guildsl(self, kit):
        """prints servers"""
        print('Servers connected to:')
        for guild in self.bot.guilds:
            print(guild.name)
            print(guild.id)

    @commands.command(hidden=True)
    async def amiadmin(self, kit):
        """ Are you admin? """
        if kit.author.id == 309025661031415809:
            return await kit.send(f"Yes **{kit.author.name}** of course your admin, your my owner :grin:")

        if kit.author.id in self.config.owners:
            return await kit.send(f"Yes **{kit.author.name}** you are admin rank! ✅")

        if kit.author.id in self.config.helpers:
            return await kit.send(f"Not quite **{kit.author.name}** you are a helper though! ✅")


        await kit.send(f"no, you dont have any owner/dev perms {kit.author.name}")

    @commands.command(hidden=True)
    @commands.check(repo.is_owner)
    async def reload(self, kit, name: str):
        """ Reloads an extension. """
        try:
            self.bot.unload_extension(f"kcr.{name}")
            self.bot.load_extension(f"kcr.{name}")
        except Exception as e:
            await kit.send(f"```\n{e}```")
            return
        await kit.send(f"Reloaded extension **{name}.py**")

    @commands.command(hidden=True)
    @commands.check(repo.is_owner)
    async def reboot(self, kit):
        """ Reboot the bot """
        await kit.send('Rebooting now...')
        time.sleep(1)
        await self.bot.logout()

    @commands.command(hidden=True)
    @commands.check(repo.is_owner)
    async def load(self, kit, name: str):
        """ Reloads an extension. """
        try:
            self.bot.load_extension(f"kcr.{name}")
        except Exception as e:
            await kit.send(f"```diff\n- {e}```")
            return
        await kit.send(f"Loaded extension **{name}.py**")

    @commands.command(hidden=True)
    @commands.check(repo.is_owner)
    async def unload(self, kit, name: str):
        """ Reloads an extension. """
        try:
            self.bot.unload_extension(f"kcr.{name}")
        except Exception as e:
            await kit.send(f"```diff\n- {e}```")
            return
        await kit.send(f"Unloaded extension **{name}.py**")

    @commands.group(hidden=True)
    @commands.check(repo.is_owner)
    async def change(self, kit):
        if kit.invoked_subcommand is None:
            _help = await kit.bot.formatter.format_help_for(kit, kit.command)

            for page in _help:
                await kit.send(page)

    @change.command(name="playing")
    @commands.check(repo.is_owner)
    async def change_playing(self, kit, *, playing: str):
        """ Change playing status. """
        try:
            await self.bot.change_presence(
                activity=discord.Game(type=0, name=playing),
                status=discord.Status.online
            )
            dataIO.change_value("config.json", "playing", playing)
            await kit.send(f"Successfully changed playing status to **{playing}**")
        except discord.InvalidArgument as err:
            await kit.send(err)
        except Exception as e:
            await kit.send(e)

    @change.command(name="username")
    @commands.check(repo.is_owner)
    async def change_username(self, kit, *, name: str):
        """ Change username. """
        try:
            await self.bot.user.edit(username=name)
            await kit.send(f"Successfully changed username to **{name}**")
        except discord.HTTPException as err:
            await kit.send(err)

    @change.command(name="nickname")
    @commands.check(repo.is_owner)
    async def change_nickname(self, kit, *, name: str = None):
        """ Change nickname. """
        try:
            await kit.guild.me.edit(nick=name)
            if name:
                await kit.send(f"Successfully changed nickname to **{name}**")
            else:
                await kit.send("Successfully removed nickname")
        except Exception as err:
            await kit.send(err)

    @change.command(name="avatar")
    @commands.check(repo.is_owner)
    async def change_avatar(self, kit, url: str = None):
        """ Change avatar. """
        if url is None and len(kit.message.attachments) == 1:
            url = kit.message.attachments[0].url
        else:
            url = url.strip('<>')

        try:
            bio = await http.get(url, res_method="read")
            await self.bot.user.edit(avatar=bio)
            await kit.send(f"Successfully changed the avatar. Currently using:\n{url}")
        except aiohttp.InvalidURL:
            await kit.send("The URL is invalid...")
        except discord.InvalidArgument:
            await kit.send("This URL does not contain a useable image")
        except discord.HTTPException as err:
            await kit.send(err)


def setup(bot):
    bot.add_cog(Admin(bot))
