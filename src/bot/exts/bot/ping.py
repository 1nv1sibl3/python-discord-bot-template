from discord.ext import commands
from discord import Embed
from bot import Bot
from constants import EmbedColor, Emoji


class Ping(commands.Cog):
    """Subclass of Cog for ping command

    Commands
    ---------
    ping - returns latency of bot.
    """

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.command(
        name="ping",
        description="Check bot response time.",
    )
    async def _command(self, ctx: commands.Context):
        # Creates embed with latency and responds
        latency = round(self.bot.latency * 1000)
        embed = Embed(
            description=f"**Pong!** {latency}ms {Emoji.LATENCY}",
            color=EmbedColor.DEFAULT_EMBED_COLOR,
        )
        await ctx.send(embed=embed)

        # Logs it for debug only
        self.bot.logger.debug(
            "Ping command invoked by %s, current latency is %sms",
            ctx.author.name,
            latency,
        )

        # returns for test purposes
        return latency


def setup(bot: Bot):
    """Called by discord.py to setup the cog."""
    bot.add_cog(Ping(bot))
