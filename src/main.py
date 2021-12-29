import discord
from discord.ext import commands
import admin, music

client = commands.Bot(command_prefix='%',description="comando ayuda", intent = discord.Intents.all())

cogs = [admin, music]

for i in range(len(cogs)):
    cogs[i].setup(client)

@client.event
async def on_ready():
    print('my bot is ready')

client.run('OTI0ODU0Mjc3MTQ1NTE0MDY0.Ycknqg.90QmLqy025Jo912w9NRXtXg65Ik')
