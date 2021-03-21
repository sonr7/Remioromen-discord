import discord
import asyncio
import os

token = os.environ.get('DISCORD_BOT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('チャイム')

@client.event
async def on_message(message):
    if message.content.startswith("#レミオロメン:"):
        kasi = message.content.replace('#レミオロメン:', '')
        with open(kasi) as kasii:
            kasiyaru = kasii.read()
        await message.channel.send(kasiyaru)

client.run(token)
