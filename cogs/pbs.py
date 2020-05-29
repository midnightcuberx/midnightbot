import discord
from discord.ext import commands
import random
import pymongo
import dns
import os


mongosecret=os.environ.get("mongosecret")
client = pymongo.MongoClient(mongosecret)
db = client["pbs"]
collection=db["pbs"]
class Pbs(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  async def pbs(self,ctx):
    eventlist=["2x2","3x3","4x4","5x5","6x6","7x7","pyraminx","oh","skewb","square-1","clock","megaminx","3bld","4bld","5bld","fmc","mbld"]
    try:
      collection.insert_one({"_id":ctx.author.id})
      userlist={}
      for event in eventlist:
        userlist[event]={"single":"None","average":"None"}
      collection.update_one({"_id":ctx.author.id},{"$set":userlist})
    except pymongo.errors.DuplicateKeyError:
      pass
    results=collection.find_one({"_id":ctx.author.id})
    
    pbs=results
    print(pbs)
    embed=discord.Embed(title=f"{ctx.author}'s Pbs",description="",color=0xffff00)
    for event in eventlist:
      embed.add_field(name=event,value=f"single: {pbs[event]['single']}\nAverage: {pbs[event]['average']}")
    await ctx.send(embed=embed)

  @commands.command()
  async def update(self,ctx, events=None,sora=None,time=None):
    eventlist=["2x2","3x3","4x4","5x5","6x6","7x7","pyraminx","oh","skewb","square-1","clock","megaminx","3bld","4bld","5bld","fmc","mbld"]
    if not events:
      await ctx.send("What event are you trying to update a pb for?")
      return
    events=events.lower()
    if not sora:
      await ctx.send("Are you trying to update your single or average???")
      return
    sora=sora.lower()
    if sora != "single" and sora != "average":
      await ctx.send("Please tell me if you want to update your average or single!")
      return
    elif events not in eventlist:
      await ctx.send("That event is not recognised!")
      return
    if not time:
      await ctx.send("You need to enter a time to update your pb to!")
      return
    try:
      collection.insert_one({"_id":ctx.author.id})
      userlist={}
      eventlist=["2x2","3x3","4x4","5x5","6x6","7x7","pyraminx","oh","skewb","square-1","clock","megaminx","3bld","4bld","5bld","fmc","mbld"]
      for event in eventlist:
        userlist[event]={"single":"None","average":"None"}
      collection.update_one({"_id":ctx.author.id},{"$set":userlist})
    except pymongo.errors.DuplicateKeyError:
      pass
    results=collection.find_one({"_id":ctx.author.id})
    
    pbs=results
    userlist={}
    for event in eventlist:
      userlist[event]=pbs[event]
    userlist[events][sora]=time
    collection.update_one({"_id":ctx.author.id},{"$set":userlist})
    await ctx.send(f"Successfully set your {events} {sora} to {time}!")
    

def setup(bot):
  bot.add_cog(Pbs(bot))
