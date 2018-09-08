from discord.ext import commands
import asyncio
import traceback
import discord
import inspect
import textwrap
import aiohttp
import random
from contextlib import redirect_stdout
import io
from ut import repo
# webhooks shit
from discord import Webhook, AsyncWebhookAdapter


class web:
    """Webook things"""

    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()
# weebhook in my emoji server
  # # get yeeted on foOL




    @commands.command()
    @commands.check(repo.is_owner)
    async def testw(self, kit):
        """webhook testing"""
        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url('put a webhook link in here my guy', adapter=AsyncWebhookAdapter(session))
            await webhook.send("Test")

    @commands.command()
    @commands.check(repo.is_owner)
    async def weebhook(self, kit):
        """webhook testing"""
        choice = ["https://www.playreplay.com.br/wp-content/uploads/2018/04/anime-melhores-aberturas-inverno-2018.jpg", "https://media.giphy.com/media/BejdfvEt6eoV2/giphy-facebook_s.jpg",
                  "https://static.tumblr.com/1b4f1fc6b2f2d3a1b7d324ec4ce9c763/ck5ozn4/Pp0nxx4jo/tumblr_static_tumblr_static_10a6v85mw4a8oc88ws004ksw0_640.jpg"]
        sendem = random.choice(choice)
        async with aiohttp.ClientSession() as session:
            weeb = discord.Embed(title="Heckin weeb",
                                 description="", color=0xffffff)
            weeb.set_image(url=sendem)
            webhook = Webhook.from_url(
                'again, put a link here idios', adapter=AsyncWebhookAdapter(session))
            await webhook.send(embed=weeb)




def setup(bot):
    bot.add_cog(web(bot))
