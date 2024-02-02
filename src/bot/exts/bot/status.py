from datetime import timedelta
import time
from discord.ext import commands
from discord import Embed
from psutil import cpu_percent, virtual_memory
from bot import Bot
from constants import EmbedColor, Emoji


class Status(commands.Cog):
    """Subclass of Cog for status command

    Commands
    ---------
    status - returns latency, ram usage, cpu usage and uptime of the bot.
    """

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.command(
        name="status",
        description="Returns stats about bot.",
    )
    async def _command(self, ctx: commands.Context):
        # Gets stats
        latency = round(self.bot.latency * 1000)
        uptime = timedelta(seconds=round(time.time()) - self.bot.start_time)
        cpu_usage = cpu_percent()
        memory_usage = virtual_memory().percent

        # Creates embed with stats and reply with it
        embed = Embed(
            description=f"**Bot's Ping** {Emoji.LATENCY}\n{latency}ms\n"
            + f"**Cpu  Usage** {Emoji.CPU}\n{cpu_usage}%\n"
            + f"**Ram  Usage** {Emoji.RAM}\n{memory_usage}%\n"
            + f"**Last Down** {Emoji.UPTIME}\n{uptime}",
            color=EmbedColor.DEFAULT_EMBED_COLOR,
        )
        await ctx.send(embed=embed)

        # Logs it for debug only
        self.bot.logger.debug(
            "Status command invoked by %s, info %s",
            ctx.author.name,
            (latency, uptime, cpu_usage, memory_usage),
        )

        # Returns for test purposes
        return (latency, uptime, cpu_usage, memory_usage)


def setup(bot: Bot):
    """Called by discord.py to setup the cog."""
    bot.add_cog(Status(bot))
