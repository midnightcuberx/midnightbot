import discord
from discord.ext import commands
import random
import pymongo
import dns
import os

def convert(seconds):
    minutes =seconds/60
    for i in range(10000):
      if minutes>=i and minutes<i+1:
        minutes=i

        
    secs=round((seconds % 60),2)
    if minutes==0:
      time="{}".format(secs)
    else:
      if secs <10:
        secs="0{}".format(secs)
      time=f"{minutes}:{secs}"
    return time
def get_sec(time_str):
  count=time_str.count(":")
  if count==1:
    m, s = time_str.split(':')
    check= float(m) * 60 + float(s)
    if check<=0:
      return "invalid time"
    else:
      return check
  elif count==2:
    h, m, s = time_str.split(':')
    check=float(h) * 3600 + float(m) * 60 + float(s)
    if check<=0:
      return "invalid time"
    else:
      return check

  elif count==0:
    try:
      check=float(time_str)
    except ValueError:
      return "invalid time"

    if check<=0:
      return "invalid time"
    else:
      return check

mongosecret=os.environ.get("mongosecret")
client = pymongo.MongoClient(mongosecret)
db = client["pbs"]
collection=db["pbs"]
class Pbs(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  '''@commands.command()
  async def pbs(self,ctx):
    userlist={}
    eventlist=["2x2","3x3","4x4","5x5","6x6","7x7","pyraminx","oh","skewb","square-1","clock","megaminx","3bld","4bld","5bld","fmc","mbld"]
    try:
      collection.insert_one({"_id":ctx.author.id})
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
    await ctx.send(embed=embed)'''

  @commands.command()
  async def pbs(self,ctx):
    userlist={}
    eventlist=["2x2","3x3","4x4","5x5","6x6","7x7","pyraminx","oh","skewb","square-1","clock","megaminx","3bld","4bld","5bld","fmc","mbld"]
    pbs=collection.find_one({"_id":"pbs"})
    try:
      a=pbs[str(ctx.author.id)]
    except KeyError:
      for event in eventlist:
        userlist[event]={"single":"None","average":"None"}
      thig={}
      for key in pbs:
        if key !="_id":
          thig[key]=pbs[key]
      thig[str(ctx.author.id)]=userlist

      collection.update_one({"_id":"pbs"},{"$set":thig})

    pbs=collection.find_one({"_id":"pbs"})
    embed=discord.Embed(title=f"{ctx.author}'s Pbs",description="",color=0xffff00)
    for event in eventlist:
      embed.add_field(name=event,value=f"single: {pbs[str(ctx.author.id)][event]['single']}\nAverage: {pbs[str(ctx.author.id)][event]['average']}")
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
      a=collection.find_one({"_id":"pbs"})
      b=a[str(ctx.author.id)]
    except KeyError:
      userlist={}
      eventlist=["2x2","3x3","4x4","5x5","6x6","7x7","pyraminx","oh","skewb","square-1","clock","megaminx","3bld","4bld","5bld","fmc","mbld"]
      for event in eventlist:
        userlist[event]={"single":"None","average":"None"}
      thig={}
      for key in a:
        if key !="_id":
          thig[key]=a[key]
      thig[str(ctx.author.id)]=userlist

      collection.update_one({"_id":"pbs"},{"$set":thig})
      
    results=collection.find_one({"_id":"pbs"})
    
    pbs=results
    userlist={}
    for user in pbs:
      if user!="_id":
        userlist[user]=pbs[user]
    userlist[str(ctx.author.id)][events][sora]=time
    collection.update_one({"_id":"pbs"},{"$set":userlist})
    await ctx.send(f"Successfully set your {events} {sora} to {time}!")
    
  @commands.command(aliases=["leaderboard"])
  async def lb(self,ctx,events="3x3",sora="single"):
    eventlist=["2x2","3x3","4x4","5x5","6x6","7x7","pyraminx","oh","skewb","square-1","clock","megaminx","3bld","4bld","5bld","fmc","mbld"]
    lblist={}
    users=[]
    lb_list=[]
    users=[]
    lb1=collection.find_one({"_id":"pbs"})
    sora=sora.lower()
    events=events.lower()
    if sora != "single" and sora != "average":
      await ctx.send("That is invalid, please enter single or average!")
      return
    if events not in eventlist:
      await ctx.send("That event is not recognised!")
      return
    for key in lb1:
      if key != "_id":
        users.append(key)

    for item in users:

        eco=lb1[item]
        lblist[item]=eco[events][sora]
    lblust={}
    for key in lblist:
      if get_sec(lblist[key])!="invalid time":
        lblust[key]=lblist[key]
        
    print(lblist)
    for key, value in sorted(lblust.items(),reverse=False, key=lambda item: get_sec(item[1])):
      if lblist[key]!="None":
        user=discord.utils.get(ctx.guild.members,id=int(key))
        try:
          string=f"{user.name}#{user.discriminator} : {value}"
          lb_list.append(string)
        except AttributeError:
          pass
    length=len(lb_list)
    if length>5:
      length=5
    for i in range(5-length):
      lb_list.append("Nobody : None")
    
    embed = discord.Embed(title=f"Top 5 {events} {sora}s in the server", description=f"🥇{lb_list[0]}\n🥈{lb_list[1]}\n🥉{lb_list[2]}\n4️⃣{lb_list[3]}\n5️⃣{lb_list[4]}",color=0xeee657)
    await ctx.send(embed=embed)
def setup(bot):
  bot.add_cog(Pbs(bot))
