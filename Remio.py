import discord
import asyncio
import os

token = os.environ.get('DISCORD_BOT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('チャイム')

@client.event
async def on_message(messsge):
    if message.content.startswith('#レミオロメン:'):
        kaaaaaaaaaaaaaaaaaaaaaaasiiiiiiiiiiiiiiiiiiii = message.content.replace('#レミオロメン', '')
        with open(kaaaaaaaaaaaaaaaaaaaaaaasiiiiiiiiiiiiiiiiiiii) as f:
            kasi = f.read()
        await message.channel.send(kasi)

client.run(token)
