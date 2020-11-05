# NesnejBot.py
# 2 items have been needed to be installed via pip install. Those being:
    # pip install -U discord.py
    # pip install -U python-dotenv

# Imports for all needed items
import os
import random
import discord

from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix='Nes!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord.')

@bot.command(name='dadjoke', help='Cringe.')
async def dad_joke(ctx):
    dadjoke = [
        'I was created using Python. I guesssss it wassss a sssssuccessssss..',
        'I like to go on a seafood diet. I see food and I eat it',        
        'When commanders were protected by air support whilst commanding a Sherman, do they reply with "Tank you"?',
        '*insert dad joke here*',
        'Why did the skeleton want to get friends? He was feeling Bonely.',
        'A guy walks into a bar, and a chair, and a table. Ouch'       
    ]

    dadresponse = random.choice(dadjoke)
    await ctx.send(dadresponse)

@bot.command(name='testme', help='Responds with a random message testing to see if the command works')
async def test_1(ctx):
    testmeme = [
        'Testing bot command',
        'Testing 2nd bot command',
        (
            'Repeat after me.\n'
            'yeyeyeyeyeyeyeye\n'
            'hoiyoyoyoyoyoyoy.'
        ),
    ]

    response = random.choice(testmeme)
    await ctx.send(response)

@bot.command(name='roll', help='Roll some dice.')
async def roll_dice(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='create-channel')
@commands.has_role('Admin')
async def create_channel(ctx, channel_name='nesnejbot-channel'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

@client.event
async def on_member_join(member):
    await member.send('Hi {member.name}, Welcome to the Discord server.\nThis is NesnejBot, a discord bot I\'ve created using Python 3.8.\nIf you received this message it would be a great help to know if you did. Thanks \n- Nesnej')


        
bot.run(TOKEN)