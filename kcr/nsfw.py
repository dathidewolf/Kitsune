import random
import discord
import json

from io import BytesIO
from discord.ext import commands
from ut import lists, permissions, http, default


class NSFW_commands:
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("conf.json")

    async def randomimageapi(self, kit, url, endpoint):
        try:
            r = await http.get(url, res_method="json", no_cache=True)
        except json.JSONDecodeError:
            return await kit.send("Couldn't find anything from the API")

        await kit.send(r[endpoint])

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def hentai(self, kit):
        """THIS IS NSFW ONLY"""
        if kit.channel.is_nsfw():
            await self.randomimageapi(kit, 'https://api.computerfreaker.cf/v1/hentai', 'url')
        else:
            await kit.send("T-this is not a nsfw channel you dummy <:Woww:437412713057222666>")

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def trap(self, kit):
        """not really nsfw but eh"""
        if kit.channel.is_nsfw():
            await self.randomimageapi(kit, 'https://api.computerfreaker.cf/v1/trap', 'url')
        else:
            await kit.send("T-this is not a nsfw channel you dummy <:Woww:437412713057222666>")

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def holo(self, kit):
        """THIS IS NSFW ONLY"""
        if kit.channel.is_nsfw():
            await self.randomimageapi(kit, 'https://nekos.life/api/v2/img/hololewd', 'url')
        else:
            await kit.send("T-this is not a nsfw channel you dummy <:Woww:437412713057222666>")

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def foxgirl(self, kit):
        """THIS IS NSFW ONLY"""
        if kit.channel.is_nsfw():
            await self.randomimageapi(kit, 'https://nekos.life/api/v2/img/fox_girl', 'url')
        else:
            await kit.send("T-this is not a nsfw channel you dummy <:Woww:437412713057222666>")

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def hentaigif(self, kit):
        """THIS IS NSFW ONLY"""
        if kit.channel.is_nsfw():
            await self.randomimageapi(kit, 'https://nekos.life/api/v2/img/Random_hentai_gif', 'url')
        else:
            await kit.send("T-this is not a nsfw channel you dummy <:Woww:437412713057222666>")

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def nekogif(self, kit):
        """THIS IS NSFW ONLY"""
        if kit.channel.is_nsfw():
            await self.randomimageapi(kit, 'https://nekos.life/api/v2//img/nsfw_neko_gif', 'url')
        else:
            await kit.send("T-this is not a nsfw channel you dummy <:Woww:437412713057222666>")

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def futa(self, kit):
        """THIS IS NSFW ONLY"""
        if kit.channel.is_nsfw():
            await self.randomimageapi(kit, 'https://nekos.life/api/v2//img/futanari', 'url')
        else:
            await kit.send("T-this is not a nsfw channel you dummy <:Woww:437412713057222666>")

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def cum(self, kit):
        """THIS IS NSFW ONLY"""
        if kit.channel.is_nsfw():
            await self.randomimageapi(kit, 'https://nekos.life/api/v2/img/cum', 'url')
        else:
            await kit.send("T-this is not a nsfw channel you dummy <:Woww:437412713057222666>")

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def yuri(self, kit):
        """THIS IS NSFW ONLY"""
        if kit.channel.is_nsfw():
            await self.randomimageapi(kit, 'https://nekos.life/api/v2/img/yuri', 'url')
        else:
            await kit.send("T-this is not a nsfw channel you dummy <:Woww:437412713057222666>")

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def smallboobs(self, kit):
        """THIS IS NSFW ONLY"""
        if kit.channel.is_nsfw():
            await self.randomimageapi(kit, 'https://nekos.life/api/v2/img/smallboobs', 'url')
        else:
            await kit.send("T-this is not a nsfw channel you dummy <:Woww:437412713057222666>")


def setup(bot):
    bot.add_cog(NSFW_commands(bot))
