import os
import discord
from discord.ext import commands
import dotenv
from dotenv import load_dotenv

from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument

from discord import Intents

# Criação do bot com intents
intents = Intents.default() # Inclui intents padrão
intents.message_content = True # Permite que o bot acesse o conteúdo das mensagens
bot = commands.Bot("!", intents=intents)

# Evento de conexão
@bot.event
async def on_ready():
  print(f"Let the Kitsune guide you! Estou conectado como {bot.user}")

@bot.event
async def on_command_error(ctx, error):
   if isinstance(error, MissingRequiredArgument):
       await ctx.send("Favor enviar todos os argumentos no comando. Digite !help para ver a lista de comandos")
   elif isinstance(error, CommandNotFound):
       await ctx.send("O Comando não existe. Digite !help para ver a lista de comandos")
   else:
      raise error

@bot.command(name="teste", help="Triste Vertebral")
async def teste(ctx):
 name = ctx.author.name

 response = "Vertebral, você é um decepção. Palavras do" + name

 await ctx.send(response)

@bot.command(name="puladaponte", help="Xinga o mik (de lei)")
async def teste(ctx):

 response = "VAI TOMAR NO MEIO DO SEU CU <@526900183821320212>"
 await ctx.send(response)

@bot.command(name="foto", help="gera um foto aleatoria com ajuda do picsum")
async def get_random_image(ctx):
 url_image = "https://picsum.photos/1920/1080"

 embed = discord.Embed(
   title= "AVISO",
   description= "a busca foi totalmente aleatoria",
   color= 0x9c0606
 )

 embed.set_author(name="SEU PAI")

 embed.set_image(url=url_image)

 await ctx.send(embed=embed)

# Execução do bot
dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN_SECRETO")
bot.run(TOKEN)
