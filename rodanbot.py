import discord
from botjoke import internet_joke_api
from botoverflow import stackoverflow

from discord.ext import commands
# internet_jokes = get_random()


client = commands.Bot(command_prefix='.')

@client.event

async def on_ready():
    print('Bot is ready.')


@client.command()

# async def ping(ctx):
#     await ctx.send('Pong') 

async def joke(ctx):
    await ctx.send(f'{internet_joke_api()}')


@client.command()

async def stack_search(ctx, *, arg):
    message = stackoverflow(arg)
    if message == None:
        await ctx.send('Could not find this question on stackoverflow.')
    else:
        await ctx.send(message)
    


client.run('NzM0MjE0MjkyOTQ1MjQwMTA2.XxSWkQ.4jA7PZ87bfWpSm2BAfnXUe_u6eE')

