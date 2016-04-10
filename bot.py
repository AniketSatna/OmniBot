import discord
import asyncio
from cogs.utils.settings import Settings

from os import system
system("title UnnamedBot")

client = discord.Client()

@client.event
async def on_ready():
	dcord = discord.Client()
	print('Successfully logged in!')

#	name = 'with Python'
#	game = discord.Game(name=name)
#	await client.change_status(game)

@bot.event
async def on_command(command, ctx):
    pass

@client.event
async def on_message(message):
	if message.content.startswith('!test'):
		await client.send_message(message.channel, message.author.mention + ', Okay it works :D')
async def on_message(message):
        if message.content.startswith('!cometome')
                
async def on_message(message):
        if message.content.startswith('!ownme')
                global lock
                msg = ctx.message
                if settings.owner != "id":
                
client.run('email', 'password')

# Not ment for public use - not done
# Above code is from Blazar - other than The !test command
