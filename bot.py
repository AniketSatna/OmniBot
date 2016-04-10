import discord
import asyncio
import logging
from importlib import import_module
import django
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
                await client.send_message(message.channel, message.author.mention + ', WIP: please dont use this command')
                
async def on_message(message):
        if message.content.startswith('!ownme')
                global lock
                msg = ctx.message
                if settings.owner != "id":

#Enable bot for plugin use

def main():
    django.setup()  # configures logging etc.
    logger.info('Starting up bot/plugins')

    pool = MethodPool()  # pool that holds all callbacks
    for plugin, options in settings.PLUGINS.items():
        if not options.get('enabled', True):
            continue

        module = 'bot.plugins.%s' % plugin
        if module in settings.INSTALLED_APPS:
            module = '%s.plugin' % module
        _plugin = import_module(module)
        plugin = _plugin.Plugin(client, options)
        pool.register(plugin)
        logger.debug('Configured plugin %r', plugin)
        


client.run('email', 'password')

# Not ment for public use - not done
# Above code is from Blazar - other than The !test command
