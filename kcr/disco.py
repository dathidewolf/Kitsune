import discord
from io import BytesIO

from ut import default, repo
from discord.ext import commands


class Discord_Info:
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("conf.json")


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(rate=1, per=7.5, type=commands.BucketType.user)
    async def bft(self, kit, *, BF: str):
        await kit.send("".join(["+"*ord(i)+".[-]"for i in BF]))

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def avatar(self, kit, user: discord.Member = None):
        """ Get the avatar of you or someone else """
        if user is None:
            user = kit.author

        await kit.send(f"Avatar to **{user.name}**\n{user.avatar_url_as(size=1024)}")

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(rate=1, per=5.0, type=commands.BucketType.user)
    async def roles(self, kit):
        """ Get all roles in current server """
        allroles = ""

        for num, role in enumerate(sorted(kit.guild.roles, reverse=True), start=1):
            allroles += f"[{str(num).zfill(2)}] {role.id}\t{role.name}\t[ Users: {len(role.members)} ]\r\n"

        data = BytesIO(allroles.encode('utf-8'))
        await kit.send(content=f"Roles in **{kit.guild.name}**", file=discord.File(data, filename=f"{default.timetext('Roles')}"))

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def joinedat(self, kit, user: discord.Member = None):
        """ Check when a user joined the current server """
        if user is None:
            user = kit.author

        embed = discord.Embed(colour=user.top_role.colour.value)
        embed.set_thumbnail(url=user.avatar_url)
        embed.description = f'**{user}** joined **{kit.guild.name}**\n{default.date(user.joined_at)}'
        await kit.send(embed=embed)

    @commands.group()
    @commands.guild_only()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def server(self, kit):
        """ Check info about current server """
        if kit.invoked_subcommand is None:
            findbots = sum(1 for member in kit.guild.members if member.bot)

            embed = discord.Embed()
            embed.set_thumbnail(url=kit.guild.icon_url)
            embed.add_field(name="Server Name", value=kit.guild.name, inline=True)
            embed.add_field(name="Server ID", value=kit.guild.id, inline=True)
            embed.add_field(name="Members", value=kit.guild.member_count, inline=True)
            embed.add_field(name="Bots", value=findbots, inline=True)
            embed.add_field(name="Owner", value=kit.guild.owner, inline=True)
            embed.add_field(name="Region", value=kit.guild.region, inline=True)
            embed.add_field(name="Created", value=default.date(kit.guild.created_at), inline=True)
            await kit.send(content=f"ℹ information about **{kit.guild.name}**", embed=embed)

    @server.command(name="avatar", aliases=["icon"])
    @commands.guild_only()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def server_avatar(self, kit):
        """ Get the current server icon """
        await kit.send(f"Avatar of **{kit.guild.name}**\n{kit.guild.icon_url_as(size=1024)}")

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def user(self, kit, user: discord.Member = None):
        """ Get user information """
        if user is None:
            user = kit.author

        embed = discord.Embed(colour=user.top_role.colour.value)
        embed.set_thumbnail(url=user.avatar_url)

        embed.add_field(name="Full name", value=user, inline=True)
        embed.add_field(name="Nickname", value=user.nick if hasattr(user, "nick") else "None", inline=True)
        embed.add_field(name="Account created", value=default.date(user.created_at), inline=True)
        embed.add_field(name="Joined this server", value=default.date(user.joined_at), inline=True)

        embed.add_field(
            name="Roles",
            value=', '.join([f"<@&{x.id}>" for x in user.roles if x is not kit.guild.default_role]) if len(user.roles) > 1 else 'None',
            inline=False
        )

        await kit.send(content=f"ℹ About **{user.id}**", embed=embed)

    @commands.command(hidden=True)
    @commands.check(repo.is_owner)
    async def GDK(self, kit, *, guild_id: int):
        """ somthing i ripped off a german bot named like pixel or somthing """ # scratch that it was owo pup :eyes: dont kill me dad
        guild = self.bot.get_guild(guild_id)
        try:
            members = set(guild.members)
            bots = filter(lambda m: m.bot, members)
            bots = set(bots)
            members = len(members) - len(bots)
            if guild == kit.guild:
                roles = ", ".join([x.mention for x in guild.roles])
            else:
                roles = "Cant find roles"

            info = discord.Embed(title="Guild info", description=f":small_red_triangle:  | Name: {guild.name}\n:small_red_triangle_down: | Members/Bots: {members}/{len(bots)}"
                                                                  f"\n:small_red_triangle:  | Owner: {guild.owner}\n:small_red_triangle: | Created at: {guild.created_at}"
                                                                  f"\n:small_red_triangle_down: | Roles: {roles}", color=0xff0000)
            info.set_thumbnail(url=guild.icon_url)
            await kit.send(embed=info)
        except:
            await kit.send("Guild Machine Broke, i dont think im in that server, or you should reload and try again")

def setup(bot):
    bot.add_cog(Discord_Info(bot))
