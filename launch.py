import discord
import config
import os
import sys
import sqlite3

from discord.ext import commands
intents = discord.Intents.all()
client = commands.Bot(command_prefix=config.PREFIX, intents=intents)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.load_extension(f'faucet')

client.run(config.TOKEN)
