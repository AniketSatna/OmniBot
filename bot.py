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
	if message.content.startswith('!help'):
	await client.send_message(PrivateChannel + 'Here is some Commands I can do: /n !help - The command you just did')

async def on_message(message):
	if message.content.startswith('!ping'):
		await client.send_message(message.channel, message.author.mention + ' PONG!')
		await asynco.sleep(1)
		await client.send_message(message.channel + 'Did you really think this command would work?')
		await asynco.sleep(1)
		await client.send_message(message.channel, message.author.mention + ' PONG!')
		
async def on_message(message):
        if message.content.startswith('!voice')

async def on_message(message):
        if message.content.startswith('!ownme')
                global lock
                msg = ctx.message
                if settings.owner != "id":
                	print("PLACEHOLDER")
                
client.run('email', 'password')

# Not ment for public use - not done
# Above code is from Blazar - other than The !test command
