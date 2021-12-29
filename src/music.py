import discord
from discord.ext import commands
from discord import Embed
import youtube_dl
import os


#comamands
# python src/main.py
# python src/main.py

# discord.FFmpegPCAudio(source="mp3.mp3")
# %play https://www.youtube.com/watch?v=BlKZfUWN69M&ab_channel=ラブライブ%21シリーズ公式チャンネル

queue = []

class music(commands.Cog):

    def __init__ (self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("¡No estás conectado en un Canal de Voz! ¡Baaaakaaa!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self, ctx):
        server = ctx.message.guild.voice_client
        await server.disconnect(force=True)
        await ctx.send('EL BOT HA SIDO DESCONECTADO CORRECTAMENTE')
        print ('disconnected')
        """ await ctx.voice_client.disconnect(force=True) """
    
    @commands.command()
    async def play(self, ctx, url):
        if ctx.author.voice is None:
            await ctx.send("¡No estás conectado en un Canal de Voz! ¡Baaaakaaa!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()        
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
            YDL_OPTIONS = {
            'format': 'bestaudio/best',
            'postprocessors':[{
                'key': 'FFmpegExtractAudio',
                'preferredcodec':'mp3',
                'preferredquality':'320',
            }],}
            queue.append(url)
            vc = ctx.voice_client
            if not vc.is_playing():
                while queue != []:
                    url = queue[0]
                    queue.pop(0)
                    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                        ctx.message.guild.voice_client.stop()
                        info = ydl.extract_info(url, download=False)
                        url2 = info['formats'][0]['url']
                        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                        vc.play(source)
                        vc.is_playing()
                        print ('Escuchando')
                        await ctx.send('REPRODUCIENDO ')
                        print (queue)
            else:
                queue.append(url)
                print ('Ya está reproduciendo una canción')
                print (queue)
        else:
            await ctx.voice_client.move_to(voice_channel)
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
            YDL_OPTIONS = {
            'format': 'bestaudio/best',
            'postprocessors':[{
                'key': 'FFmpegExtractAudio',
                'preferredcodec':'mp3',
                'preferredquality':'320',
            }],}
            queue.append(url)
            vc = ctx.voice_client
            if not vc.is_playing():
                while queue != []:
                    url = queue[0]
                    queue.pop(0)
                    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                        ctx.message.guild.voice_client.stop()
                        info = ydl.extract_info(url, download=False)
                        url2 = info['formats'][0]['url']
                        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                        vc.play(source)
                        vc.is_playing()
                        print ('Escuchando')
                        print (queue)
            else:
                queue.append(url)
                await ctx.send('CANCION AGREGADA A LA LISTA')
                print ('Ya está reproduciendo una canción')
                print (queue)

    # python src/main.py
    @commands.command()
    async def pause(self, ctx):
        vz = discord.utils.get(self.client.voice_clients,guild = ctx.guild)
        vz.pause()
        await ctx.send("Pausado")
        print ('Pausado')
        

    @commands.command()
    async def resume(self, ctx):
        vz = discord.utils.get(self.client.voice_clients,guild = ctx.guild)
        vz.resume()
        await ctx.send("Reanudando")
        print ('Reanudando')

    @commands.command()
    async def stop(self, ctx):
        vz = discord.utils.get(self.client.voice_clients,guild = ctx.guild)
        vz.stop()
        await ctx.send('EL BOT SE HA A DETENIDO')

    @commands.command()
    async def next(self, ctx):
        queue.pop[0]
        await ctx.send('Otra weá')
    
def setup(client):
    client.add_cog(music(client))