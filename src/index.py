#IMPORT
import discord
import datetime
import admin
import urllib
import re
import youtube_dl
import os

import music.py
import spotify.py

from discord.ext import commands
from urllib import parse,request
from discord.utils import get


bot = commands.Bot(command_prefix='%',description="comando ayuda")

#COMANDO INFO SERVER
@bot.command()
async def status(ctx):
    embed = discord.Embed(title =f"{ctx.guild.name}",description  ="HOLA QUE HACE MANO",
            timestamp = datetime.datetime.utcnow(),color=discord.Color.blue())
    embed.add_field(name = "Este servidor fue creado el",value = f"{ctx.guild.created_at}")
    
    embed.add_field(name = "Region del servidor",value =f"{ctx.guild.region}")
    embed.add_field(name = "ID del servidor",value =f"{ctx.guild.id}")
    embed.set_thumbnail(video="{ctx.guild.icon}")
    embed.add_field(name="Dueño del servidor",value =f"{ctx.guild.owner}")
        
    await ctx.send(embed = embed)
    print({ctx.guild.icon_url})


#eventos
@bot.event
async def on_ready():
    print('my bot is ready')




    
bot.run('OTI0ODU0Mjc3MTQ1NTE0MDY0.Ycknqg.90QmLqy025Jo912w9NRXtXg65Ik')
    
    