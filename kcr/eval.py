from discord.ext import commands
import asyncio
import traceback
import discord
import inspect
import textwrap
from contextlib import redirect_stdout
import io
from ut import repo, default

# to expose to the eval command
import datetime
from collections import Counter


class evalc:
    """Eval command"""

    def __init__(self, bot):
        self.bot = bot
        self._last_result = None
        self.sessions = set()
        self.emotes = default.get("emoji.json")

    def cleanup_code(self, content):
        """Automatically removes code blocks from the code."""
        # remove ```py\n```
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

        # remove `foo`
        return content.strip('` \n')

    def get_syntax_error(self, e):
        if e.text is None:
            return f'```py\n{e.__class__.__name__}: {e}\n```'
        return f'```py\n{e.text}{"^":>{e.offset}}\n{e.__class__.__name__}: {e}```'

    @commands.command(pass_context=True, hidden=True, name='eval')
    @commands.check(repo.is_owner)
    async def _eval(self, kit, *, body: str):
        """Evaluates a code"""

        env = {
            'bot': self.bot,
            'kit': kit,
            'channel': kit.channel,
            'author': kit.author,
            'guild': kit.guild,
            'message': kit.message,
            '_': self._last_result,
            'emote':  self.emotes
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await kit.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await kit.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await kit.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await kit.send(f'```py\n{value}\n```')
            else:
                self._last_result = ret
                await kit.send(f'```py\n{value}{ret}\n```')
# oh nanananan na na 


def setup(bot):
    bot.add_cog(evalc(bot))
