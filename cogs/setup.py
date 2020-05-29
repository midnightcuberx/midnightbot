import discord,pymongo,dns,os
from discord.ext import commands


mongosecret=os.environ.get("mongosecret")
client = pymongo.MongoClient(mongosecret)
db = client["comp"]
collection=db["results"]


class Setup(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command()
  async def bansetup(self,ctx):
    for guild in self.bot.guilds:
      db=client["comp"]
      collection=db.bans
      collection.insert_one({"_id":guild.id,"bans":{}})
      await ctx.send("done")

  @commands.command()
  @commands.is_owner()
  async def recordsetup(self,ctx):
    for guild in self.bot.guilds:
      collection=db["records"]
      eventrecords={}
      eventlist=["2x2","3x3","4x4","5x5","6x6","7x7","pyraminx","oh","skewb","square-1","clock","megaminx","3bld","4bld","5bld"]
      for event in eventlist:
        eventrecords[event]={"single":"Nobody - None","average":"Nobody - None"}
        
      collection.insert_one({"_id":guild.id})
      collection.update_one({"_id":guild.id},{"$set":eventrecords})
    await ctx.send("done")

  @commands.command()
  @commands.is_owner()
  async def comps123(self,ctx):
    for guild in self.bot.guilds:
      collection.insert_one({"_id":guild.id,"3x3":{},"4x4":{},"2x2":{},"5x5":{},"6x6":{},"7x7":{},"square-1":{},"skewb":{},"clock":{},"pyraminx":{},"oh":{},"megaminx":{},"3bld":{},"4bld":{},"5bld":{}})
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def compsetup(self,ctx):
    try:
      collection.insert_one({"_id":ctx.guild.id,"3x3":{},"4x4":{},"2x2":{},"5x5":{},"6x6":{},"7x7":{},"square-1":{},"skewb":{},"clock":{},"pyraminx":{},"oh":{},"megaminx":{},"3bld":{},"4bld":{},"5bld":{}})
    except pymongo.errors.DuplicateKeyError:
      await ctx.send("The comp is already set up in your server!")
  
  @commands.command()
  @commands.is_owner()
  async def config123(self,ctx):
    collection=db["config"]
    for guild in self.bot.guilds:
      collection.insert_one({"_id":guild.id,"3x3":{"mode":"on"},"4x4":{"mode":"on"},"2x2":{"mode":"on"},"5x5":{"mode":"on"},"6x6":{"mode":"on"},"7x7":{"mode":"on"},"square-1":{"mode":"on"},"skewb":{"mode":"on"},"clock":{"mode":"on"},"pyraminx":{"mode":"on"},"oh":{"mode":"on"},"megaminx":{"mode":"on"},"3bld":{"mode":"on"},"4bld":{"mode":"on"},"5bld":{"mode":"on"}})



    


def setup(bot):
  bot.add_cog(Setup(bot))
