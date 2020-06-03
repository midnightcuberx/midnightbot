import discord,os,pymongo,dns
from discord.ext import commands
import pyTwistyScrambler
import pycubescrambler
from pyTwistyScrambler import scrambler333,scrambler222,scrambler444,scrambler555,pyraminxScrambler,scrambler666,scrambler777,megaminxScrambler,squareOneScrambler,skewbScrambler,clockScrambler
from pycubescrambler import side

mongosecret=os.environ.get("mongosecret")
client = pymongo.MongoClient(mongosecret)
db = client["comp"]
collection=db["config"]



class Comp(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def start(self,ctx):
    coll=db["mode"]
    coll.update_one({"_id":ctx.guild.id},{"$set":{"mode":"on"}})
    await ctx.send("Successfully started the weekly comp")
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def comp(self,ctx):
    coll=db["mode"]
    coll.update_one({"_id":ctx.guild.id},{"$set":{"mode":"on"}})
    await ctx.send("This may take a while to generate. Please give it a minute")
    scrambles=[]
    results=collection.find({"_id":ctx.guild.id})
    for result in results:
      config=result
    if config['2x2']['mode']=="on":
      for i in range(5):
        scram=scrambler222.get_WCA_scramble()
        scrambles.append(scram)
      await ctx.send(f"2x2:\n-\n> 1) {scrambles[0]}\n-\n> 2) {scrambles[1]}\n-\n> 3) {scrambles[2]}\n-\n> 4) {scrambles[3]}\n-\n> 5) {scrambles[4]}")
    scrambles=[]
    if config['3x3']['mode']=="on":
      for i in range(5):
        scram=scrambler333.get_WCA_scramble()
        scrambles.append(scram)
      await ctx.send(f"3x3:\n-\n> 1) {scrambles[0]}\n-\n> 2) {scrambles[1]}\n-\n> 3) {scrambles[2]}\n-\n> 4) {scrambles[3]}\n-\n> 5) {scrambles[4]}")
    scrambles=[]
    if config['4x4']['mode']=="on":
      for i in range(5):
        client1= pymongo.MongoClient("mongodb+srv://midnightcuberx:Annarcher811@cluster0-epubu.mongodb.net/test?retryWrites=true&w=majority")
        db2=client1["scrambles"]
        coll=db2["4x4"]
        results=coll.find({})
        
        scramble=results[0]["scramble"]
        scrambles.append(scramble)
        scram=coll.find({"scramble":scramble})
        list2=[]
        for result in scram:
          list2.append(result["_id"])
        coll.delete_one({"_id":list2[-1],"scramble":scramble})
      await ctx.send(f"4x4:\n-\n> 1) {scrambles[0]}\n-\n> 2) {scrambles[1]}\n-\n> 3) {scrambles[2]}\n-\n> 4) {scrambles[3]}\n-\n> 5) {scrambles[4]}")
    scrambles=[]
    if config['5x5']['mode']=="on":
      for i in range(5):
        scram=scrambler555.get_WCA_scramble()
        scrambles.append(scram)
      await ctx.send(f"5x5:\n-\n> 1) {scrambles[0]}\n-\n> 2) {scrambles[1]}\n-\n> 3) {scrambles[2]}\n-\n> 4) {scrambles[3]}\n-\n> 5) {scrambles[4]}")
    scrambles=[]

    if config['6x6']['mode']=="on":
      for i in range(3):
        scram=scrambler666.get_WCA_scramble()
        scrambles.append(scram)
      await ctx.send(f"6x6:\n-\n> 1) {scrambles[0]}\n-\n> 2) {scrambles[1]}\n-\n> 3) {scrambles[2]}")
    scrambles=[]

    if config['7x7']['mode']=="on":
      for i in range(3):
        scram=scrambler777.get_WCA_scramble()
        scrambles.append(scram)
      await ctx.send(f"7x7:\n-\n> 1) {scrambles[0]}\n-\n> 2) {scrambles[1]}\n-\n> 3) {scrambles[2]}")
    scrambles=[]
    if config['oh']['mode']=="on":
      for i in range(5):
        scram=scrambler333.get_WCA_scramble()
        scrambles.append(scram)
      await ctx.send(f"OH:\n-\n> 1) {scrambles[0]}\n-\n> 2) {scrambles[1]}\n-\n> 3) {scrambles[2]}\n-\n> 4) {scrambles[3]}\n-\n> 5) {scrambles[4]}")
    scrambles=[]
    if config['3bld']['mode']=="on":
      for i in range(3):
        scram=scrambler333.get_3BLD_scramble()
        scrambles.append(scram)
      await ctx.send(f"3BLD:\n-\n> 1) {scrambles[0]}\n-\n> 2) {scrambles[1]}\n-\n> 3) {scrambles[2]}")
    scrambles=[]
    
    if config['4bld']['mode']=="on":
      for i in range(3):
        scram=scrambler444.get_4BLD_scramble()
        scrambles.append(scram)
      await ctx.send(f"4BLD:\n-\n> 1) {scrambles[0]}\n-\n> 2) {scrambles[1]}\n-\n> 3) {scrambles[2]}")
    scrambles=[]
    if config['5bld']['mode']=="on":
      for i in range(3):
        scram=scrambler555.get_5BLD_scramble()
        scrambles.append(scram)
      await ctx.send(f"5BLD:\n-\n> 1) {scrambles[0]}\n-\n> 2) {scrambles[1]}\n-\n> 3) {scrambles[2]}")
    scrambles=[]

    if config['pyraminx']['mode']=="on":
      for i in range(5):
        scram=pyraminxScrambler.get_WCA_scramble()
        scrambles.append(scram)
      await ctx.send(f"Pyraminx:\n-\n> 1) {scrambles[0]}\n-\n> 2) {scrambles[1]}\n-\n> 3) {scrambles[2]}\n-\n> 4) {scrambles[3]}\n-\n> 5) {scrambles[4]}")
    scrambles=[]

    if config['skewb']['mode']=="on":
      for i in range(5):
        scram=skewbScrambler.get_WCA_scramble()
        scrambles.append(scram)
      await ctx.send(f"Skewb:\n-\n> 1) {scrambles[0]}\n-\n> 2) {scrambles[1]}\n-\n> 3) {scrambles[2]}\n-\n> 4) {scrambles[3]}\n-\n> 5) {scrambles[4]}")
    scrambles=[]

    if config['square-1']['mode']=="on":
      for i in range(5):
        scram=squareOneScrambler.get_WCA_scramble()
        scrambles.append(scram)
      await ctx.send(f"Square-1:\n-\n> 1) {scrambles[0]}\n-\n> 2) {scrambles[1]}\n-\n> 3) {scrambles[2]}\n-\n> 4) {scrambles[3]}\n-\n> 5) {scrambles[4]}")
    scrambles=[]

    if config['clock']['mode']=="on":
      for i in range(5):
        scram=clockScrambler.get_WCA_scramble()
        scrambles.append(scram)
      await ctx.send(f"Clock:\n-\n> 1) {scrambles[0]}\n-\n> 2) {scrambles[1]}\n-\n> 3) {scrambles[2]}\n-\n> 4) {scrambles[3]}\n-\n> 5) {scrambles[4]}")
    scrambles=[]
    if config['megaminx']['mode']=="on":
      for i in range(5):
        scram=side.get_mega()
        scrambles.append(scram)
      await ctx.send(f"Megaminx:\n-\n> 1) {scrambles[0]}\n-\n> 2) {scrambles[1]}\n-\n> 3) {scrambles[2]}\n-\n> 4) {scrambles[3]}\n-\n> 5) {scrambles[4]}")
    await ctx.send("All done.")
    scrambles=[]
    if config["fmc"]["mode"]=="on":
      for i in range(5):
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
        scrambles.append("R' U' F " + " ".join(a) + " R' U' F")
      await ctx.send(f"Megaminx:\n-\n> 1) {scrambles[0]}\n-\n> 2) {scrambles[1]}\n-\n> 3) {scrambles[2]}\n-\n> 4) {scrambles[3]}\n-\n> 5) {scrambles[4]}")
    await ctx.send("All done")
  



def setup(bot):
  bot.add_cog(Comp(bot))
