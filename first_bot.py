# Importação das dependências
import discord
from discord.ext import commands
from discord import Intents

# Criação do bot com intents
intents = Intents.default()  # Inclui intents padrão
intents.message_content = True  # Permite que o bot acesse o conteúdo das mensagens
bot = commands.Bot("!", intents=intents)

# Evento de conexão
@bot.event
async def on_ready():
    print(f"Let the Kitsune guide you! Estou conectado como {bot.user}")

@bot.command(name="teste")
async def teste(ctx):
   name = ctx.author.name

   response = "Vertebral, você é um decepção. Palavras do" + name

   await ctx.send(response)

@bot.command(name="puladaponte")
async def teste(ctx):

   response = "VAI TOMAR NO MEIO DO SEU CU <@526900183821320212>"
   await ctx.send(response)
   
# Execução do bot
bot.run("MTIwOTYzOTg4MDY2NjI1OTQ1Nw.GVwl6Y.H2Xds-Cn2PZ6neYdtw-SPTq_VRWjUveW9gzmuI")  # Substitua por seu token

