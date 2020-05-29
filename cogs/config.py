import discord
from discord.ext import commands
import pymongo
import dns
import os

mongosecret=os.environ.get("mongosecret")
client = pymongo.MongoClient(mongosecret)
db = client["comp"]
collection=db["config"]


class Config(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def bans(self,ctx):
    collection=db["bans"]
    results=collection.find({"_id":ctx.guild.id})
    for result in results:
      bans=result
    banlist={}
    for key in bans["bans"]:
      if key !="_id":
        if bans["bans"][key]=="banned":
          banlist[key]=bans["bans"][key]
    banlist2=[]
    print (banlist)
    for key in banlist:
      target=discord.utl
      banlist2.append(f"<@{key}>")
    
    if len(banlist)==0:
      banlist2.append("None")
    embed=discord.Embed(title=f"Bans for {ctx.guild}",description=" , ".join(banlist2),color=0xffff00)
    await ctx.send(embed=embed)

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def config(self,ctx,event):
    results=collection.find({"_id":ctx.guild.id})
    for result in results:
      config=result
    try:
      mode=config[event]["mode"]
    except KeyError:
      await ctx.send("That event is not recognised!")
      return
    if mode=="on":
      onoff="off"
      collection.update_one({"_id":ctx.guild.id},{"$set":{event:{"mode":onoff}}})
    elif mode=="off":
      onoff="on"
      collection.update_one({"_id":ctx.guild.id},{"$set":{event:{"mode":onoff}}})
    await ctx.send(f"Successfully toggled {event} to {onoff}")
  
  @config.error
  async def config_error(self,ctx,error):
    if isinstance(error,commands.MissingPermissions):
      await ctx.send("Sorry you need manage messages permissions to run this command")
    else:
      raise error

  


  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def ban(self,ctx,user:discord.Member=None):
    if not user:
      await ctx.send("You need to mention a user to ban from competitions!")
    collban=db.bans
    results=collban.find({"_id":ctx.guild.id})
    for result in results:
      ban=result
    print(ban)
    userlist={}
    for key in ban["bans"]:
      userlist[key]=ban["bans"][key]
    userlist[str(user.id)]="banned"
    collban.update_one({"_id":ctx.guild.id},{"$set":{"bans":userlist}})
    collection=db["results"]
    results=collection.find({"_id":ctx.guild.id})
    for result in results:
      comp=result
    userlist={}
    eventlist=["2x2","3x3","4x4","5x5","6x6","7x7","pyraminx","oh","skewb","square-1","clock","megaminx","3bld","4bld","5bld"]
    for event in eventlist:
      for key in comp[event]:
        try:
          userlist[key]=comp[event][key]
        except KeyError:
          ok=1
      try:
        del userlist[str(user.id)]
      except KeyError:
        ok=1
      collection.update_one({"_id":ctx.guild.id},{"$set":{event:userlist}})
    await ctx.send(f"Successfully banned {user} from future competitions")
  
  @ban.error
  async def ban_error(self,ctx,error):
    if isinstance(error,commands.MissingPermissions):
      await ctx.send("Sorry you need manage messages permissions to run this command")
    else:
      raise error

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def unban(self,ctx,user:discord.Member=None):
    if not user:
      await ctx.send("You need to mention a user to unban from competitions!")
    collban=db.bans
    results=collban.find({"_id":ctx.guild.id})
    for result in results:
      ban=result
    userlist={}
    for key in ban["bans"]:
      userlist[key]=ban["bans"][key]
    userlist[str(user.id)]="not banned"
    collban.update_one({"_id":ctx.guild.id},{"$set":{"bans":userlist}})
    await ctx.send(f"Successfully unbanned {user} from future competitions")
  @unban.error
  async def unban_error(self,ctx,error):
    if isinstance(error,commands.MissingPermissions):
      await ctx.send("Sorry you need manage messages permissions to run this command")


  @commands.command()
  async def events(self,ctx):
    collection=db["config"]
    eventlist=["2x2","3x3","4x4","5x5","6x6","7x7","pyraminx","oh","skewb","square-1","clock","megaminx","3bld","4bld","5bld"]
    eventson=[]
    eventsoff=[]
    results=collection.find({"_id":ctx.guild.id})
    for result in results:
      config=result
    for event in eventlist:
      if config[event]["mode"]=="on":
        eventson.append(event)
      else:
        eventsoff.append(event)
      if len(eventsoff)==0:
        eventsoff.append("None")
      if len(eventson)==0:
        eventson.append("None")
    onevent=", ".join(eventson)
    offevent=", ".join(eventsoff)
    embed=discord.Embed(title=f"Events in {ctx.guild}",description="",color=0xffff00)
    embed.add_field(name="Enabled events:",value=onevent,inline=False)
    embed.add_field(name="Disabled events:",value=offevent,inline=False)
    await ctx.send(embed=embed)
    
      
      

def setup(bot):
  bot.add_cog(Config(bot))
