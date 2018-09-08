import os
from discord.ext import commands
from ut import repo
import time
import discord
import logging

from discord.ext.commands import HelpFormatter
from brn import KitsuneClient
from ut import permissions, default

#yeet
config = default.get("conf.json")

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



class HelpFormat(HelpFormatter):
    async def format_help_for(self, context, command_or_bot):
        if permissions.can_react(context):
            await context.message.add_reaction(chr(0x2709))

        return await super().format_help_for(context, command_or_bot)


print("Magic charging...")
help_attrs = dict(hidden=True)
Kitsune = KitsuneClient(command_prefix=commands.when_mentioned_or("Kit-"), prefix=commands.when_mentioned_or("Kit-"), pm_help=True, help_attrs=help_attrs, formatter=HelpFormat(), description="kit")

for file in os.listdir("kcr"):
    if file.endswith(".py"):
        name = file[:-3]
        Kitsune.load_extension(f"kcr.{name}")


@Kitsune.event
async def on_resumed():
    print("Reconnected to discord!")



# yeet yeet 
Kitsune.run(config.token)
