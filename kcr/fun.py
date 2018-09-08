import random
import discord
import json
import aiohttp
import asyncio
import async_timeout

from io import BytesIO
from discord.ext import commands
from ut import lists, permissions, http, default
from random import randint

class Fun_Commands:
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("conf.json")

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def clap(self, kit, *, msg: str):
        """👏 We 👏 all 👏 need 👏 clapping 👏 in 👏 our 👏 lives. 👏"""
        await kit.send(f"👏{'👏'.join(msg.split(' '))}👏")

            # oh yeah almost none of this is mine kek



    @commands.command(aliases=['8ball'])
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def eightball(self, kit, *, question: commands.clean_content):
        """ Consult 8ball to receive an answer """
        answer = random.choice(lists.ballresponse)
        await kit.send(f"🎱 **Question:** {question}\n**Answer:** {answer}")

    async def randomimageapi(self, kit, url, endpoint):
        try:
            r = await http.get(url, res_method="json", no_cache=True)
        except json.JSONDecodeError:
            return await kit.send("Couldn't find anything from the API")

        await kit.send(r[endpoint])



    @commands.command(aliases=['flip', 'coin'])
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def coinflip(self, kit):
        """ Coinflip! """
        coinsides = ['Heads', 'Tails']
        await kit.send(f"**{kit.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")

    @commands.command(aliases=['define', 'dict'])
    @commands.cooldown(rate=1, per=3.5, type=commands.BucketType.user)
    async def urban(self, kit, *, search: str):
        """ Find the 'best' definition to your words """
        if not permissions.can_embed(kit):
            return await kit.send("I cannot send embeds here ;-;")

        url = await http.get(f'http://api.urbandictionary.com/v0/define?term={search}', res_method="json")

        if url is None:
            return await kit.send("I think the API broke...")

        count = len(url['list'])
        if count == 0:
            return await kit.send("Couldn't find your search in the dictionary...")
        result = url['list'][random.randint(0, count - 1)]

        definition = result['definition']
        if len(definition) >= 1000:
                definition = definition[:1000]
                definition = definition.rsplit(' ', 1)[0]
                definition += '...'

        embed = discord.Embed(colour=0xC29FAF, description=f"**{result['word']}**\n*by: {result['author']}*")
        embed.add_field(name='Definition', value=definition, inline=False)
        embed.add_field(name='Example', value=result['example'], inline=False)
        embed.set_footer(text=f"👍 {result['thumbs_up']} | 👎 {result['thumbs_down']}")

        try:
            await kit.send(embed=embed)
        except discord.Forbidden:
            await kit.send("I found something, but have no access to post it... [Embed permissions]")

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def reverse(self, kit, *, text: str):
        """ !poow ,ffuts esreveR
        Everything you type after reverse will of course, be reversed
        """
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        await kit.send(f"🔁 {t_rev}")

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def rate(self, kit, *, thing: commands.clean_content):
        """ Rates what you desire """
        numbers = random.randint(0, 100)
        decimals = random.randint(0, 9)

        if numbers == 100:
            decimals = 0

        await kit.send(f"I'd rate {thing} a **{numbers}.{decimals} / 100**")

    @commands.command(aliases=['howhot', 'hot'])
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def hotcalc(self, kit, user: discord.Member = None):
        """ Returns a random percent for how hot is a discord user """
        if user.id == 309025661031415809:
                    return await kit.send(f"**dathidewolf** is **100%** hot 💞")
        if user is None:
            user = kit.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        emoji = "💔"
        if hot > 25:
            emoji = "❤"
        if hot > 50:
            emoji = "💖"
        if hot > 75:
            emoji = "💞"

        await kit.send(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")



    @commands.command(aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def slot(self, kit):
        """ Roll the slot machine """
        if kit.author.id == 309025661031415809:
            return await kit.send(f"""
**wolfirik** rolled the slots...
[ :strawberry: :strawberry: :strawberry: ]
and... won! 🎉""")
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        if (a == b == c):
            message = 'and won! 🎉'
        elif (a == b) or (a == c) or (b == c):
            message = 'and almost won (2/3)'
        else:
            message = 'and lost...'

        result = f"**{kit.author.name}** rolled the slots...\n**[ {a} {b} {c} ]**\n{message}"
        await kit.send(result)

def setup(bot):
    bot.add_cog(Fun_Commands(bot))
