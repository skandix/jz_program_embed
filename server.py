import discord
import asyncio
from apiFetch import api_format

# https://discordapp.com/oauth2/authorize?client_id=463326592412942356&scope=bot 
BOT_TOKEN = ''

client = discord.Client()

def format(data):
    return ("```\n{}\n```".format(data))

@client.event
async def on_message(message):
    if message.author.bot or message.author == client.user:
        return
    
    tokens = message.content.split(' ')
    print (tokens)
    if "https://2018.javazone.no/program/" in tokens[0]:       
        data = api_format(tokens[0])

        embed = discord.Embed(title=data[-1], colour=discord.Colour(0xfd9e01), url=tokens[0], description=data[2])
        embed.set_author(name=data[1], url="", icon_url="")
        embed.add_field(name="Room", value=data[3], inline=True)
        embed.add_field(name="Format", value=data[4], inline=True)
        embed.add_field(name="Length", value=data[5], inline=True)
        await client.send_message(message.channel, embed=embed)

    else:
        return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(BOT_TOKEN)