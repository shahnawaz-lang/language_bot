# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands
from requests import request
from help_func import formatter


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@Bot.command()
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
