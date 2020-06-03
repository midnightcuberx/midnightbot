import discord
from discord.ext import commands
import pymongo
import dns
import os
import json


mongosecret=os.environ.get("mongosecret")
client = pymongo.MongoClient(mongosecret)
db = client["comp"]
collection=db["results"]



bot = commands.Bot(command_prefix= "m!")

@bot.event
async def on_ready():

    activity = discord.Game(name=f"m!help", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('Bot is ready')
    print('------')
bot.remove_command('help')
for filename in os.listdir('./cogs'):
  if filename.endswith(".py"):
    bot.load_extension(f"cogs.{filename[:-3]}")

@bot.event
async def on_guild_join(guild):
  mongosecret=os.environ.get("mongosecret")
  client = pymongo.MongoClient(mongosecret)
  db=client["comp"]
  collection=db["results"]
  collection.insert_one({"_id":guild.id,"3x3":{},"4x4":{},"2x2":{},"5x5":{},"6x6":{},"7x7":{},"square-1":{},"skewb":{},"clock":{},"pyraminx":{},"oh":{},"megaminx":{},"3bld":{},"4bld":{},"5bld":{}})
  db=client["comp"]
  collection=db["config"]
  collection.insert_one({"_id":guild.id,"3x3":{"mode":"on"},"4x4":{"mode":"on"},"2x2":{"mode":"on"},"5x5":{"mode":"on"},"6x6":{"mode":"on"},"7x7":{"mode":"on"},"square-1":{"mode":"on"},"skewb":{"mode":"on"},"clock":{"mode":"on"},"pyraminx":{"mode":"on"},"oh":{"mode":"on"},"megaminx":{"mode":"on"},"3bld":{"mode":"on"},"4bld":{"mode":"on"},"5bld":{"mode":"on"}})
  db=client["comp"]
  collection=db["bans"]
  collection.insert_one({"_id":guild.id,"bans":{}})
  collection=db["mode"]
  collection.insert_one({"_id":guild.id,"mode":"off"})


@bot.event
async def on_bot_remove(guild):
  mongosecret=os.environ.get("mongosecret")
  client = pymongo.MongoClient(mongosecret)
  db=client["comp"]
  collection=db["results"]
  collection.delete_one({"_id":guild.id})
  db=client["comp"]
  collection=db["config"]
  collection.delete_one({"_id":guild.id})
  db=client["comp"]
  collection=db.bans
  collection.delete_one({"_id":guild.id})
  collection=db["mode"]
  collection.insert_one({"_id":guild.id})




@commands.is_owner()
async def reload(ctx,*,file=None):
  if not file:
    for filename in os.listdir('./cogs'):
      if filename.endswith(".py"):
        bot.unload_extension(f"cogs.{filename[:-3]}")
        bot.load_extension(f"cogs.{filename[:-3]}")
        await ctx.send(f"Successfully reloaded {filename}!")
    return
  bot.unload_extension(f"cogs.{file[:-3]}")
  bot.load_extension(f"cogs.{file[:-3]}")
  await ctx.send(f"Successfully reloaded {file}!")


@bot.command()
async def invite(ctx):
  await ctx.send("Use this to invite Midnight Scrambler to your server : https://discord.com/oauth2/authorize?client_id=694632046730936390&permissions=71680&scope=bot")



token=os.environ.get("botsecret")
bot.run(token)
