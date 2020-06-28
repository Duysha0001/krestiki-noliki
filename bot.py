import discord
from discord.ext import commands
import requests
from discord.ext import tasks
from discord.utils import *
import random
import os
import time
import asyncio
import datetime


prefix = ['/']
bot = commands.Bot( command_prefix = prefix)
bot.remove_command("help")
bot.load_extension("jishaku")

@bot.event
async def on_ready():
    print(">> Bot is ready\n"
        f">> Bot user: {bot.user}\n"
        ">> Loading Cogs...")
    for file_name in os.listdir("./cogs"):
        if file_name.endswith(".py"):
            client.load_extension(f'cogs.{file_name[:-3]}')
            print(f'The Cog {file_name[:-3]} was loaded successfully')
    print(f">> Changing my status")
    await bot.change_presence( status = discord.Status.online)
    print(f">> Status changed successfully")
    print(f">> Changing my activity")
    act = 'v1.0'
    await bot.change_presence(activity=discord.Streaming(name='/help | '+str(act)))
    print(f">> Activity changed successfully")
    print(f'The version of the bot - {act}')
    embed = discord.Embed(
        title = 'Restart'
    )
    guild = client.get_guild(565603241933668381)
    channel = guild.get_channel(723885963625103360)
    time = datetime.datetime.today()
    embed.add_field(name = 'Time', value = f'{time}', inline = False)
    embed.add_field(name = 'Ping', value = f'{bot.latency * 1000:.0f} ms', inline = False)
    await channel.send(embed = embed)

@bot.command()
async def help(ctx):
    embed = discord.Embed(title = 'Вот все мои команды', description = '- `/help` - команда помощи\n- `/ttt @user` - предложу поиграть в крестики нолики упомянутому пользователю\n- `/ping` - покажу свой пинг')
    await ctx.send(embed = embed)

@bot.command()
async def ping(ctx):
    await ctx.send(f'Мой пинг: {bot.latency * 1000:.0f} ms')

@bot.command()
async def online(ctx):
    if ctx.author.id == 465853102914928640:
        await ctx.message.delete()
        await bot.change_presence( status = discord.Status.online)
        await ctx.author.send(f'Cтатус `online` успешно поставлен')

@bot.command()
async def idle(ctx):
    if ctx.author.id == 465853102914928640:
        await ctx.message.delete()
        await bot.change_presence( status = discord.Status.idle)
        await ctx.author.send(f'Cтатус `idle` успешно поставлен')
           
@bot.command()
async def dnd(ctx):
    if ctx.author.id == 465853102914928640:
        await ctx.message.delete()
        await bot.change_presence( status = discord.Status.dnd)
        await ctx.author.send(f'Cтатус `dnd` успешно поставлен')

@bot.command()
async def offline(ctx):
    if ctx.author.id == 465853102914928640:
        await ctx.message.delete()
        await bot.change_presence( status = discord.Status.offline)
        await ctx.author.send(f'Cтатус `offline` успешно поставлен')

@bot.command()
async def load(ctx, extensions):
    if ctx.author.id == 465853102914928640:
        bot.load_extension(f'cogs.{extensions}')
        await ctx.send(f'{ctx.author.mention}, cog `{extensions}` is loaded')

@bot.command()
async def unload(ctx, extensions):
    if ctx.author.id == 465853102914928640:
        bot.unload_extension(f'cogs.{extensions}')
        await ctx.send(f'{ctx.author.mention}, cog `{extensions}` is unloaded')

@bot.command()
async def reload(ctx, extensions):
    if ctx.author.id == 465853102914928640:
        bot.reload_extension(f'cogs.{extensions}')
        await ctx.send(f'{ctx.author.mention}, cog `{extensions}` is reloaded')

@bot.command()
async def logout(ctx):
    await ctx.message.add_reaction('✅') 
    await bot.logout()



token = str(os.environ.get("token"))
bot.run(token)
