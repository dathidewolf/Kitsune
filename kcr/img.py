import discord
from discord.ext import commands

import json
from random import randint

import random
import aiohttp
import asyncio
import async_timeout

class images:

    shib = ''
    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession(loop=self.bot.loop)

#your mom gay
    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def fox(self, kit):
        """Fox's! floofy FOX"""
        isVideo = True
        while isVideo:
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://randomfox.ca/floof/') as resp:
                    res = await resp.json()
                    res = res['image']
                    cs.close()
            if res.endswith('.mp4'):
                pass
            else:
                isVideo = False
        em = discord.Embed()
        await kit.send(embed=em.set_image(url=res))

    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def anime(self, kit):
        """Weeb shit"""
        isVideo = True
        while isVideo:
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://api.computerfreaker.cf/v1/anime') as resp:
                    res = await resp.json()
                    res = res['url']
                    cs.close()
            if res.endswith('.mp4'):
                pass
            else:
                isVideo = False
        em = discord.Embed()
        await kit.send(embed=em.set_image(url=res))

    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def neko(self, kit):
        """some cat girls"""
        isVideo = True
        while isVideo:
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://nekos.life/api/neko') as resp:
                    res = await resp.json()
                    res = res['neko']
                    cs.close()
            if res.endswith('.mp4'):
                pass
            else:
                isVideo = False
        em = discord.Embed()
        await kit.send(embed=em.set_image(url=res))

    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def duck(self, kit):
        """QUACK"""
        isVideo = True
        while isVideo:
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://random-d.uk/api/v1/random') as resp:
                    res = await resp.json()
                    res = res['url']
                    cs.close()
            if res.endswith('.mp4'):
                pass
            else:
                isVideo = False
        em = discord.Embed()
        await kit.send(embed=em.set_image(url=res))

    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def dog(self, kit):
        """Only the goodest boys"""
        isVideo = True
        while isVideo:
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://random.dog/woof.json') as resp:
                    res = await resp.json()
                    res = res['url']
                    cs.close()
            if res.endswith('.mp4'):
                pass
            else:
                isVideo = False
        em = discord.Embed()
        await kit.send(embed=em.set_image(url=res))

    @commands.command(pass_context=True)
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def cat(self, kit):
        """The little satans"""
        isVideo = True
        while isVideo:
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://nekos.life/api/v2/img/meow') as resp:
                    res = await resp.json()
                    res = res['url']
                    cs.close()
            if res.endswith('.mp4'):
                pass
            else:
                isVideo = False
        em = discord.Embed()
        await kit.send(embed=em.set_image(url=res))


    class Shibs():
        data = None
        size = None

def setup(bot):
    bot.add_cog(images(bot))
