import discord
from discord.ext import commands
import datetime

#comamands

#COMANDO PARA ELMINAR MENSAJES
# python src/main.py
# python src/main.py
  
class admin(commands.Cog):

    def __init__ (self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, n:int):
        if (n < 1000):

            deleted = await ctx.channel.purge(limit=n+1)
            await ctx.send('Eliminando {} mensajes'.format(n))

        else:
            await ctx.send('No se pueden eliminar más de 1000 mensajes')

    #comamands
    # python src/main.py
    # python src/main.py


    @commands.command()
    async def info(self, ctx):
        embed = discord.Embed(title =f"{ctx.guild.name}",description  ="HOLA QUE HACE MANO",
                timestamp = datetime.datetime.utcnow(),color=discord.Color.blue())
        embed.add_field(name = "Este servidor fue creado el",value = f"{ctx.guild.created_at}")
        
        embed.add_field(name = "Region del servidor",value =f"{ctx.guild.region}")
        embed.add_field(name = "ID del servidor",value =f"{ctx.guild.id}")
        embed.set_image(url="https://hentai9.org/wp-content/uploads/2021/09/bokura-no-love-live-25-kitaku-jikan-kitaku-yakimochi-a-symmetry-love-live-sunshine-chinese-cover-1.jpg")
        embed.add_field(name="Dueño del servidor",value =f"{ctx.guild.owner}")
            
        await ctx.send(embed = embed)
        print({ctx.guild.icon_url})

def setup(client):
    client.add_cog(admin(client))