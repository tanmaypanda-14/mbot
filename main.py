import discord
import os
# from json import loads
from recommendationmodel import *
from utils.bb import *
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    # await client.change_presence(activity=discord.Game(name="with ur mom"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith('$help'):
        await message.channel.send('help')  # to-do help env
    if msg.startswith('$top5'):
        await message.channel.send(song1.title)
        await message.channel.send(song2.title)
        await message.channel.send(song3.title)
        await message.channel.send(song4.title)
        await message.channel.send(song5.title)
    if msg.startswith('$recommend'):
        track1 = msg.split("$recommend ", 1)[1]
        await message.channel.send(recommend(track_id=track1, ref_df=df, sp=sp, n_recs=5))

client.run(TOKEN)
