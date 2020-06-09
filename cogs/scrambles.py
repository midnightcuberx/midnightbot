import discord
from discord.ext import commands
from pyTwistyScrambler import scrambler333,scrambler222,scrambler444,scrambler555,pyraminxScrambler,scrambler666,scrambler777,megaminxScrambler,squareOneScrambler,skewbScrambler,clockScrambler
from pycubescrambler import side
import random,json

class Scrams(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  '''@commands.command(aliases=["2x2","2"])
  async def two(self,ctx, numofscrambles: int=1):
    if numofscrambles>5:
      numofscrambles=5

    for i in range(numofscrambles):
      a=scrambler222.get_WCA_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)

  @commands.command(aliases=["3x3","3","OH"])
  async def two2(self,ctx, numofscrambles: int=1,tipe=None):
    if numofscrambles>5:
      numofscrambles=5

    for i in range(numofscrambles):
      a=scrambler333.get_WCA_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)'''


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

  '''@commands.command(aliases=["4x4","4"])
  async def two1(self,ctx, numofscrambles: int=1):
    if numofscrambles>5:
      numofscrambles=5

    for i in range(numofscrambles):
      with open('scrams.json','r') as f:
        scram=json.load(f)
      for i in range(numofscrambles):
        ok=list(scram)[-1]
        if ok=="1":
          a=scrambler444.get_random_state_scramble()
          await ctx.send(a)

        else:
          a=scram[ok]
          del scram[ok]
          with open('scrams.json','w') as f:
            json.dump(scram,f,indent=4)
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)

  @commands.command(aliases=["5x5","5"])
  async def two3(self,ctx, numofscrambles: int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler555.get_WCA_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)

  @commands.command(aliases=["6x6","6"])
  async def two4(self,ctx, numofscrambles: int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler666.get_WCA_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)


  @commands.command(aliases=["7x7","7"])
  async def two4(self,ctx, numofscrambles: int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler777.get_WCA_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)

  @commands.command(aliases=["squan","sq-1","square-1"])
  async def sq1(self,ctx, numofscrambles: int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=squareOneScrambler.get_WCA_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)

  @commands.command(aliases=["skweeb"])
  async def skewb(self,ctx, numofscrambles: int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=skewbScrambler.get_WCA_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)

  @commands.command(aliases=["cloncc","watch","time"])
  async def clock(self,ctx, numofscrambles: int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=clockScrambler.get_WCA_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)
  
  @commands.command(aliases=["FMC"])
  async def fmc(self,ctx,numofscrambles=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler333.get_WCA_scramble().split()
      list1=["F","F2","F'","B'","B2","B"]
      list2=["R2","R","R'","L","L'","L2"]
      list3=["F","F2","F'"]
      list4=["R2","R","R'"]
      print(a[-1])
      print(a)
      times=0
      while (a[0] in list1 and a[1] in list1) or (a[0] in list3) or (a[-1] in list2 and a[-2] in list2) or (a[-1] in list4):
        if times>3:
          a=scrambler333.get_WCA_scramble().split()
          times=0

        if a[0] in list3:
          a.remove(a[0])
          times+=1

        if (a[0] in list1 and a[1] in list1):
          if a[0] not in list3:
            a.remove(a[1])
            times+=1
          else:
            a.remove(a[0])
            times+=1
        
        if a[-1] in list4:
          a.remove(a[-1])
          times+=1
        
        if (a[-1] in list2 and a[-2] in list2):
          if a[-1] not in list4:
            a.remove(a[-2])
            times+=1
          else:
            a.remove(a[-1])
            times+=1
        print(times)
      scramble="R' U' F " + " ".join(a) + " R' U' F"
      embed=discord.Embed(title="",description=scramble,color=0xffff00)
      await ctx.send(embed=embed)
  
  @commands.command(aliases=["pyra"])
  async def pyraminx(self,ctx, numofscrambles: int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=pyraminxScrambler.get_WCA_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)

  @commands.command(aliases=["3bld"])
  async def bld3(self,ctx, numofscrambles: int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler333.get_3BLD_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)

  @commands.command(aliases=["4bld"])
  async def bld4(self,ctx, numofscrambles: int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler444.get_4BLD_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)

  @commands.command(aliases=["5bld"])
  async def bld5(self,ctx, numofscrambles: int=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=scrambler555.get_5BLD_scramble()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)'''

  @commands.command(aliases=["mega"])
  async def megaminx(self,ctx,numofscrambles=1):
    if numofscrambles>5:
      numofscrambles=5
    for i in range(numofscrambles):
      a=side.get_mega()
      embed=discord.Embed(title="",description=a,color=0xffff00)
      await ctx.send(embed=embed)



    


def setup(bot):
  bot.add_cog(Scrams(bot))
