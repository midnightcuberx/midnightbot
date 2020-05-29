import discord
from discord.ext import commands
import random
class Cubing(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  async def help(self,ctx,cat=None):
    if not cat:
      embed=discord.Embed(title="Commands for Midnight Scrambler",description="A bot with comp features and wca legal scrambles\n\nPrefix: ``m!``",color=0xfff000)
      embed.add_field(name="__**Comp**__",value="comp, podiums, resetuser, view, config, ban, unban, records, events, submit, bans, resetrecord, avg",inline=False)
      embed.add_field(name="__**Scrambles**__",value="2x2, 3x3, 4x4, 5x5, 6x6, 7x7, OH, FMC, square-1, skewb, clock, mega, pyra, 3bld, 4bld, 5bld, corners, edges, cross, F2L, LL, ZBLL, LSLL, LSE, CMLL, 2GLL",inline=False)
      embed.add_field(name="__**Other**__",value="pbs, update",inline=False)
    elif cat.lower()=="comp":
      embed=discord.Embed(title="Comp commands for Midnight Scrambler",description="",color=0xfff000)
      embed.add_field(name="comp",value="generates scrambles for the weekly comp",inline=False)
      embed.add_field(name="podiums",value="Generates results and the overall winner for the week",inline=False)
      embed.add_field(name="submit <event> <single> <average>",value="Submits your weekly comp results",inline=False)
      embed.add_field(name="resetuser <member> <event>",value="resets results of an event for a user",inline=False)
      embed.add_field(name="view",value="You can view your own results",inline=False)
      embed.add_field(name="config <event>",value="configurate the events in your weekly comp",inline=False)
      embed.add_field(name="ban <member>",value="bans a member from weekly comps",inline=False)
      embed.add_field(name="unban <member>",value="unbans a member from weekly comps",inline=False)
      embed.add_field(name="records",value="shows the server records",inline=False)
      embed.add_field(name="resetrecord <event> <single or average>",value="resets a record",inline=False)
      embed.add_field(name="avg <time1> <time2> <time3> <time4> <time5>",value="calculate your average! Comes in handy when calculating your results for the weekly comp",inline=False)
    elif cat.lower()=="other":
      embed=discord.Embed(title="Other commands for Midnight Scrambler",description="",color=0xfff000)
      embed.add_field(name="pbs",value="Shows your pbs")
      embed.add_field(name="update <event> <single or avg> <time>",value="updates your pbs")
    await ctx.send(embed=embed)
  


    

  
    


def setup(bot):
  bot.add_cog(Cubing(bot))
