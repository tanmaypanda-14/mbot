import discord
import os
from recommendationmodel import *
from utils.bb import *
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
sp=auth.authorize()


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
    elif msg.startswith('$top5'):
        await message.channel.send(song1.title)
        await message.channel.send(song2.title)
        await message.channel.send(song3.title)
        await message.channel.send(song4.title)
        await message.channel.send(song5.title)
    # elif msg.startswith('$recommend'):
    #     track1 = msg.split("$recommend ", 1)[1]
    #     await message.channel.send(suggestion_system_func(track1))
    elif msg.startswith('$recommend'):
        track1 = msg.split("$recommend", 1)[1]
        results = sp.search(track1, types=('track',), limit=5)
        Song_info = results[0].asbuiltin()

        Search_result = []
        for i in range(0, 5):
            Search_result.append((Song_info['items'][i]['name'] + " by " + Song_info['items'][i]['artists'][0]['name']))

        for i in range(0, 5):
            await message.channel.send(str(i + 1) + "." + Song_info['items'][i]['name'] + " by " + Song_info['items'][i]['artists'][0]['name'])

        await message.channel.send('Enter Song no.')
        mesg = await client.wait_for("message",check = lambda message: message.author == message.author and message.channel == message.channel)
        if mesg:
            choice = mesg.content
            choice_con=int(choice)
            print(choice_con)
        ch_id = Song_info['items'][choice_con - 1]['id']
        
        await message.channel.send(recommend(ch_id, ref_df=df, sp=sp, n_recs=5))


client.run(TOKEN)
