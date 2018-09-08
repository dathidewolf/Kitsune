import discord
import re

from io import BytesIO
from discord.ext import commands
from ut import permissions, default


# Source: https://github.com/Rapptz/RoboDanny/blob/rewrite/cogs/mod.py
class MemberID(commands.Converter):
    async def convert(self, kit, argument):
        try:
            m = await commands.MemberConverter().convert(kit, argument)
        except commands.BadArgument:
            try:
                return int(argument, base=10)
            except ValueError:
                raise commands.BadArgument(f"{argument} is not a valid member or member ID.") from None
        else:
            can_execute = kit.author.id == kit.bot.owner_id or \
                          kit.author == kit.guild.owner or \
                          kit.author.top_role > m.top_role

            if not can_execute:
                raise commands.BadArgument('You cannot do this action on this user due to role hierarchy.')
            return m.id


class ActionReason(commands.Converter):
    async def convert(self, kit, argument):
        ret = argument

        if len(ret) > 512:
            reason_max = 512 - len(ret) - len(argument)
            raise commands.BadArgument(f'reason is too long ({len(argument)}/{reason_max})')
        return ret


class Moderator:
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("conf.json")

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(kick_members=True)
    async def kick(self, kit, member: discord.Member, *, reason: str = None):
        """ Kicks a user from the current server. """
        try:
            await member.kick(reason=default.responsible(kit.author, reason))
            await kit.send(default.actionmessage("kicked"))
        except Exception as e:
            await kit.send(e)

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(kick_members=True)
    async def warn(self, kit, id: int, reason: str, *, why: str):
        """Kit-warn (userid) (reasonwarned[nospaces]) (why warned)
        Example Kit-warn (userid) spamming-in-general you were spamming"""
        ##########################################################YEEEEEEEEEEEEEET

    @commands.command(aliases=["nick"])
    @commands.guild_only()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    @permissions.has_permissions(manage_nicknames=True)
    async def nickname(self, kit, member: discord.Member, *, name: str = None):
        """ Nicknames a user from the current server. """
        try:
            await member.edit(nick=name, reason=default.responsible(kit.author, "Changed by command"))
            message = f"Changed **{member.name}'s** nickname to **{name}**"
            if name is None:
                message = f"Reset **{member.name}'s** nickname"
            await kit.send(message)
        except Exception as e:
            await kit.send(e)

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(ban_members=True)
    async def ban(self, kit, member: MemberID, *, reason: str = None):
        """ Bans a user from the current server. """
        try:
            await kit.guild.ban(discord.Object(id=member), reason=default.responsible(kit.author, reason))
            await kit.send(default.actionmessage("banned"))
        except Exception as e:
            await kit.send(e)

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(rate=1, per=10.0, type=commands.BucketType.user)
    @permissions.has_permissions(ban_members=True)
    async def massban(self, kit, reason: ActionReason, *members: MemberID):
        """ Mass bans multiple members from the server. """

        try:
            for member_id in members:
                await kit.guild.ban(discord.Object(id=member_id), reason=default.responsible(kit.author, reason))
            await kit.send(default.actionmessage("massbanned", mass=True))
        except Exception as e:
            await kit.send(e)

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(ban_members=True)
    async def unban(self, kit, member: MemberID, *, reason: str = None):
        """ Bans a user from the current server. """
        try:
            await kit.guild.unban(discord.Object(id=member), reason=default.responsible(kit.author, reason))
            await kit.send(default.actionmessage("unbanned"))
        except Exception as e:
            await kit.send(e)

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(manage_roles=True)
    async def mute(self, kit, member: discord.Member, *, reason: str = None):
        """ Mutes a user from the current server. """
        message = []
        for role in kit.guild.roles:
            if role.name == "Muted":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except IndexError:
            return await kit.send("Are you sure you've made a role called **Muted**? Remember that it's case sensetive too...")

        try:
            await member.add_roles(therole, reason=default.responsible(kit.author, reason))
            await kit.send(default.actionmessage("muted"))
        except Exception as e:
            await kit.send(e)

    @commands.command()
    @commands.guild_only()
    @permissions.has_permissions(manage_roles=True)
    async def unmute(self, kit, member: discord.Member, *, reason: str = None):
        """ Mutes a user from the current server. """
        message = []
        for role in kit.guild.roles:
            if role.name == "Muted":
                message.append(role.id)
        try:
            therole = discord.Object(id=message[0])
        except IndexError:
            return await kit.send("Are you sure you've made a role called **Muted**? Remember that it's case sensetive too...")

        try:
            await member.remove_roles(therole, reason=default.responsible(kit.author, reason))
            await kit.send(default.actionmessage("unmuted"))
        except Exception as e:
            await kit.send(e)

    @commands.group()
    @commands.guild_only()
    @commands.cooldown(rate=1, per=5.5, type=commands.BucketType.user)
    @permissions.has_permissions(manage_messages=True)
    async def prune(self, kit):
        """ Removes messages from the current server. """

        if kit.invoked_subcommand is None:
            help_cmd = self.bot.get_command('help')
            await kit.invoke(help_cmd, 'remove')

    async def do_removal(self, kit, limit, predicate, *, before=None, after=None, message=True):
        if limit > 2000:
            return await kit.send(f'Too many messages to search given ({limit}/2000)')

        if before is None:
            before = kit.message
        else:
            before = discord.Object(id=before)

        if after is not None:
            after = discord.Object(id=after)

        try:
            deleted = await kit.channel.purge(limit=limit, before=before, after=after, check=predicate)
        except discord.Forbidden as e:
            return await kit.send('I do not have permissions to delete messages.')
        except discord.HTTPException as e:
            return await kit.send(f'Error: {e} (try a smaller search?)')

        deleted = len(deleted)
        if message is True:
            await kit.send(f'🚮 Successfully removed {deleted} message{"" if deleted == 1 else "s"}.')

    @prune.command()
    async def embeds(self, kit, search=100):
        """Removes messages that have embeds in them."""
        await self.do_removal(kit, search, lambda e: len(e.embeds))

    @prune.command()
    async def files(self, kit, search=100):
        """Removes messages that have attachments in them."""
        await self.do_removal(kit, search, lambda e: len(e.attachments))

    @prune.command()
    async def images(self, kit, search=100):
        """Removes messages that have embeds or attachments."""
        await self.do_removal(kit, search, lambda e: len(e.embeds) or len(e.attachments))

    @prune.command(name='all')
    async def _remove_all(self, kit, search=100):
        """Removes all messages."""
        await self.do_removal(kit, search, lambda e: True)

    @prune.command()
    async def user(self, kit, member: discord.Member, search=100):
        """Removes all messages by the member."""
        await self.do_removal(kit, search, lambda e: e.author == member)

    @prune.command()
    async def contains(self, kit, *, substr: str):
        """Removes all messages containing a substring.
        The substring must be at least 3 characters long.
        """
        if len(substr) < 3:
            await kit.send('The substring length must be at least 3 characters.')
        else:
            await self.do_removal(kit, 100, lambda e: substr in e.content)

    @prune.command(name='bots')
    async def _bots(self, kit, prefix=None, search=100):
        """Removes a bot user's messages and messages with their optional prefix."""

        def predicate(m):
            return m.author.bot or (prefix and m.content.startswith(prefix))

        await self.do_removal(kit, search, predicate)

    @prune.command(name='users')
    async def _users(self, kit, prefix=None, search=100):
        """Removes only user messages. """

        def predicate(m):
            return m.author.bot is False

        await self.do_removal(kit, search, predicate)

    @prune.command(name='emoji')
    async def _emoji(self, kit, search=100):
        """Removes all messages containing custom emoji."""
        custom_emoji = re.compile(r'<:(\w+):(\d+)>')

        def predicate(m):
            return custom_emoji.search(m.content)

        await self.do_removal(kit, search, predicate)

    @prune.command(name='reactions')
    async def _reactions(self, kit, search=100):
        """Removes all reactions from messages that have them."""

        if search > 2000:
            return await kit.send(f'Too many messages to search for ({search}/2000)')

        total_reactions = 0
        async for message in kit.history(limit=search, before=kit.message):
            if len(message.reactions):
                total_reactions += sum(r.count for r in message.reactions)
                await message.clear_reactions()

        await kit.send(f'Successfully removed {total_reactions} reactions.')


def setup(bot):
    bot.add_cog(Moderator(bot))
