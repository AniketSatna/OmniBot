import discord
import asyncio
import logging
from importlib import import_module
from cogs.utils.settings import Settings

from os import system
system("title OmniBot")

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
        elif message.content.startswith('!info'):
         await client.send_message(message.channel, message.author.mention + ' Info \nVersion: 0.0.1 \nAuthors: Blazy#2607 | LegitCheesecake#2039 | Biotic#9319 \n You can view all commands with **!commands**')
                
async def on_message(message):
        if message.content.startswith('!ownme'):
                global lock
                msg = ctx.message
                if settings.owner != "id":
                        print("DELETE")
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
        


client.run('oliver1605@hotmail.co.uk', 'oliver101')

# Not ment for public use - not done
# Above code is from Blazar - other than The !test command
