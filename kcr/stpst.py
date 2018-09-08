import time
import aiohttp
import discord
import asyncio
import random

from discord.ext import commands
from io import BytesIO
from ut import repo, default, http, dataIO


class shitposting:
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("conf.json")

    async def randomimageapi(self, kit, url, endpoint):
        try:
            r = await http.get(url, res_method="json", no_cache=True)
        except json.JSONDecodeError:
            return await kit.send("Couldn't find anything from the API")

        await kit.send(r[endpoint])

# have at it 
# these are from server i was in :hyperkek:
    @commands.command(pass_context=True)
    async def Night(self, kit):
        await kit.send("""
Ash - Today at 8:16 PM
I like palm trees""")

    @commands.command()
    async def floofwonslots(self, kit):
        """YAY"""
        embed = discord.Embed(title='YAY', description='''
☁ floof ☁ - Today at 1:34 PM
Kit-slots
KitsuneBOT - Today at 1:34 PM
:cloud:  floof  :cloud: rolled the slots...
[ :tangerine: :tangerine: :tangerine: ]
and won! :tada:
☁ floof ☁ - Today at 1:34 PM
OMGH''', color=0x0d00ff)
        embed.set_footer(text=' YAY ')
        await kit.send(embed=embed)


    @commands.command()
    async def togglewonslots(self, kit):
        """YAY"""
        embed = discord.Embed(title='EZ', description='''
ilyToggle - Today at 1:35 PM
Kit-slots
KitsuneBOT - Today at 1:35 PM
ilyToggle rolled the slots...
[ :lemon: :lemon: :lemon: ]
and won! :tada:
ilyToggle - Today at 1:35 PM
YES
WINNNNNNNNNNN''', color=0xff9600)
        embed.set_footer(text=' YES ')
        await kit.send(embed=embed)

    @commands.command()
    async def abuse(self, kit):
        """abuse him"""
        embed = discord.Embed(title='ABUSE!', description='''
GamingFeatured - Today at 4:40 PM
abusive staff
3 warns for one ping
woah chill
Pbknowall - Today at 4:41 PM
Chill?!
dathidewolf - Today at 4:41 PM
want 4 warns?
GamingFeatured - Today at 4:41 PM
haha for what
dathidewolf - Today at 4:41 PM
existing
Pbknowall - Today at 4:41 PM
Chill my fucking ass I'll get you kicked before you can say ping
GamingFeatured - Today at 4:42 PM
abuse
abuse''', color=0x0d00ff)
        embed.set_footer(text=' ABUSIVE MODS ')
        await kit.send(embed=embed)



    @commands.command()
    async def drinkwatery(self, kit):
        """chill 0-0"""
        embed = discord.Embed(title='chill damn', description='''
wolfirikToday at 9:36 AM
drink watery diarrhea
『รpøøziɛ』ᴮᵒᵗToday at 9:36 AM
yikes
υикиσωиToday at 9:36 AM
Chill

''', color=0x0d00ff)
        embed.set_footer(text=' 0-0 ')
        await kit.send(embed=embed)

    @commands.command()
    async def modabuse(self, kit):
        'SOMEONE CALL SELTROX'
        await kit.send("""⚒ Mod BotBOT - today at 7:39 :dynoSuccess: kisaaaaaa#6087 was muted
⚒ Mod BotBOT - Today at 7:41 AM :dynoSuccess: kisaaaaaa#6087 was unmuted
kisaaaaaa - Today at 7:41 AM abuse'
kisaaaaaa - Today at 7:41 AM eat dirt
kisaaaaaa - Today at 7:41 AM not more than what you deserve after that""")

    @commands.command()
    async def rook(self, rook):
        await rook.send("I have sent a rooK!")





def setup(bot):
    bot.add_cog(shitposting(bot))
