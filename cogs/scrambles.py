import discord
from discord.ext import commands
from pyTwistyScrambler import scrambler333,scrambler222,scrambler444,scrambler555,pyraminxScrambler,scrambler666,scrambler777,megaminxScrambler,squareOneScrambler,skewbScrambler,clockScrambler
from pycubescrambler import side
import random,json

class Scrams(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command(aliases=["3x3 edges"])
  async def edges(self,ctx,numofscrambles:int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler333.get_edges_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)

  @commands.command(aliases=["3x3 corners"])
  async def corners(self,ctx,numofscrambles:int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler333.get_corners_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)
  
  @commands.command(aliases=["3x3 LL"])
  async def LL(self,ctx,numofscrambles:int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler333.get_LL_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)

  @commands.command(aliases=["3x3 cross"])
  async def cross(self,ctx,moves:int=0,numofscrambles:int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler333.get_easy_cross_scramble(moves)
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)

  @commands.command()
  async def F2L(self,ctx,numofscrambles:int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler333.get_easy_cross_scramble(0)
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)

  @commands.command()
  async def LSLL(self,ctx,numofscrambles:int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler333.get_LSLL_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)

  @commands.command()
  async def ZBLL(self,ctx,numofscrambles:int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler333.get_ZBLL_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)
  @commands.command()
  async def LSE(self,ctx,numofscrambles:int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler333.get_LSE_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)

  @commands.command()
  async def CMLL(self,ctx,numofscrambles:int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler333.get_CMLL_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)

  @commands.command(aliases=["2gen","2GLL"])
  async def twogen(self,ctx,numofscrambles:int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler333.get_LSLL_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)


    


def setup(bot):
  bot.add_cog(Scrams(bot))
