import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

Cog = getattr(commands, 'Cog', object)


class Information(Cog):
    """Information plugin"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def information(self, ctx):
        """Information about this server."""

        embed = discord.Embed(
            title="Information",
            color=discord.Color.blue(),
            description="Sample Text",
            embed.add_field(name="2nd field",value="sample 2")
        )
        embed.set_thumbnail(url=ctx.guild.icon_url)
        
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
