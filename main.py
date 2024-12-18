import os
import discord
from discord.ext import commands
from requests import request
from help_func import formatter

url = 'http://lindat.mff.cuni.cz/services/udpipe/api/process'
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.command()
async def parse_sentence(ctx, model, string):
    embed = discord.Embed(title=string, colour=discord.Colour.blue())
    output_string = formatter(request('GET', url=url, params={'model': str(model).lower() or "english",
                                                              'tokenizer': '',
                                                              'parser': '',
                                                              'tagger': '',
                                                              'data': string}).json()['result'])
    for k, v in output_string.items():
        embed.add_field(name=k, value=v, inline=False)
    await ctx.send(embed=embed)



bot.run(os.environ["DISCORD_TOKEN"])
