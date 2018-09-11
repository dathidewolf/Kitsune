import discord
import os
import json
import secrets

from discord.ext import commands
from ut import repo, default
from sec import keyg


class regis:
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("conf.json")
        self.emote = default.get("emoji.json")

    @commands.command()
    async def reg(self, kit):
        await kit.send(f"Ur Mum Gay {self.emote.lmao}")

    @commands.command()
    async def register(self, kit):
        """TEst register command"""
        try:
            REGKey = keyg.secure()
            fileopen = r"reg/" + str(kit.message.author.id) + ".reg.json"
            file = open(fileopen, "w", encoding="utf-8")
            data = {}
            data["Username"] = " " + str(kit.message.author.name) + \
                " #" + str(kit.message.author.discriminator) + " "
            data["ID"] = " " + str(kit.message.author.id)
            data["REGKey"] = f"{REGKey}"
            json.dump(data, file, ensure_ascii=False)
            file.close()
            await kit.send(f"Sure...you registerd for..somthing? {self.emote.thelook}")
            await kit.author.send(f"This is your REGKey '{REGKey}', dont delete this.")
        except Exception as e:
            await kit.send(f"There was a error editing the JSON, i wouldint even bother honestly, this is just a test, But here ur error my guy\n{e}")

    @commands.command()
    async def freg(self, kit, user: discord.Member = None):
        """TEst register command"""
        if user is None:
            await kit.send("Mention someone dumbass")
        try:
            REGKey = keyg.secure()
            fileopen = r"reg/" + str(user.id) + ".reg.json"
            file = open(fileopen, "w", encoding="utf-8")
            data = {}
            data["Username"] = " " + str(user.name) + "#" + str(user.discriminator) + " "
            data["ID"] = " " + str(user.id)
            data["REGKey"] = f"{REGKey}"
            data["Force reg?"] = f"Yes, forced by {kit.message.author.id}"
            json.dump(data, file, ensure_ascii=False)
            file.close()
            await kit.send(f"Sure...you registerd for..somthing? {self.emote.thelook}")
            await user.send(f"This is your REGKey '{REGKey}', dont delete this.")
        except Exception as e:
            await kit.send(f"Yeah this happens everytime you run force register, just ignore it\nThere was a error editing the JSON, i wouldint even bother honestly, this is just a test, But here ur error my guy\n{e}")

def setup(bot):
    bot.add_cog(regis(bot))
