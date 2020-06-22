import discord
from discord.ext import commands
from discord.utils import get
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_member_join(member):
    print('welcome: '+str(member))


@client.event
async def on_member_remove(member):
    print(str(member) + ' bye')


@client.command()
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

@client.command()
async def enroll(ctx, courses=''):
    author = ctx.message.author
    classes = courses.split(',')
    categories = ctx.guild.categories
    classes_index=None
    for channel in categories:
        if str(channel).lower()=='classes':
            classes_index = categories.index(channel)
    for channel in categories[classes_index].text_channels:
        for course in classes:
            if course == str(channel):
                perms = channel.overwrites_for(author)
                perms.send_messages = True
                perms.read_messages = True
                await channel.set_permissions(author, overwrite=perms, reason="New Class Added")

    for channel in categories:
        if str(channel).lower() == 'classes_voice':
            classes_index = categories.index(channel)
    for channel in categories[classes_index].voice_channels:
        for course in classes:
            if course == str(channel):
                # print(course)
                perms = channel.overwrites_for(author)
                perms.view_channel = True

                await channel.set_permissions(author, overwrite=perms, reason="New Class Added")



token_file = open("token.txt",'r')
for l in token_file:
    token = l
    print(token)
client.run(token)





