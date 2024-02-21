from first_bot import bot
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument


@bot.event
async def on_command_error(ctx, error):
   if isinstance(error, MissingRequiredArgument):
      await ctx.send("Favor enviar todos os argumentos no comando")
   elif isinstance(error, CommandNotFound):
      await ctx.send("O Comando não existe")
   else:
      raise error