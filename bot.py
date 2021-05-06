import discord
from discord.ext.commands import Bot, Cog

client = Bot(command_prefix='!')

@client.event
async def on_ready():
#After our bot connects to the server, do this first
    print(f'Logged in as {client.user.name} {client.user.id}')

    await client.change_presence(status=discord.Status.online)


@client.event
async def on_message(message):
    if message.content.startswith('hello'):
        await message.channel.send('Hello there!')

    elif message.content == "stop":
        await message.channel.send('Ok bye!')
        await client.close()

cogs = ['cogs.8ball', 'cogs.pokemon']
for cog in cogs:
    client.load_extension(cog)

client.run('')

#python bot.py
