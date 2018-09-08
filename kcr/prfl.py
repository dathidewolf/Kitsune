import time
import discord
import psutil
import os
import json

from discord.ext import commands
from datetime import datetime
from ut import repo, default


class profile:
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("conf.json")
        self.process = psutil.Process(os.getpid())
        self.totalmembers = set({})
# just took out 343 lines of juicy delicious profile code
# bet you wanted it right?
# yeah nope 
# dont want anyone to just take this cause
# 1 its coded horrible
# 2 its mine not urs hah ur mum gayyyyyyy


def setup(bot):
    bot.add_cog(profile(bot))
