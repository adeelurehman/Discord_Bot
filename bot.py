import discord
from discord.ext import commands
from discord.utils import get
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

client = commands.Bot(command_prefix='!')


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
async def room(ctx, *args):
    message = '!reserve \"' + ctx.message.author.display_name + '\'s Room\" ' + str(len(args)+1) + ' ' + str(ctx.message.author.id) + ' '
    for user in args:
        id = getID(ctx,user)
        if (id is not None):
            message += str(id) + ' '
    await ctx.send(message)
    print(message)

def getID(ctx, name):
    memberList = ctx.guild.members
    for member in memberList:
        if ( member.nick == name or member.name.startswith(name) or member.mention == name):
            return member.id

@client.command()
async def clear(ctx, amount=1):
    if "admin" in [y.name.lower() for y in ctx.author.roles]:
        await ctx.channel.purge(limit=amount)
    else:
        await ctx.send('Sorry, this command is restricted to admin use only')

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
    courses_string = ''
    for c in classes:
        courses_string+=', '+c
    await ctx.send(f'```'
                   f'enrolled in{courses_string[1:]}'
                   f'```')

@client.command()
async def drop(ctx, courses=''):
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
                perms.send_messages = False
                perms.read_messages = False
                await channel.set_permissions(author, overwrite=perms, reason="New Class Added")

    for channel in categories:
        if str(channel).lower() == 'classes_voice':
            classes_index = categories.index(channel)
    for channel in categories[classes_index].voice_channels:
        for course in classes:
            if course == str(channel):
                # print(course)
                perms = channel.overwrites_for(author)
                perms.view_channel = False

                await channel.set_permissions(author, overwrite=perms, reason="New Class Added")
    courses_string = ''
    for c in classes:
        courses_string+=', '+c
    await ctx.send(f'```'
                   f'dropped in{courses_string[1:]}'
                   f'```')

@client.command()
async def courses(ctx):
    categories = ctx.guild.categories
    author = ctx.message.author
    courses =[]
    for channel in categories:
        if str(channel).lower()=='classes':
            classes_index = categories.index(channel)
    for channel in categories[classes_index].text_channels:
        perms = channel.overwrites_for(author)
        if perms.read_messages==True:
            courses.append(str(channel))
    courses_string = ''
    for c in courses:
        courses_string += ', ' + c
    await ctx.send(f'```'
                   f'my courses are{courses_string[1:]}'
                   f'```')

@client.command()
async def Help(ctx):
    await ctx.send('```'
                   'Commands: \n'
                   '.enroll class1,class2,class3 for this format \n'
                   '.courses will list out your current courses \n'
                   '.drop class1,class2,class3 will drop these class \n'
                   '```')

token_file = open("token.txt",'r')
for l in token_file:
    token = l
    print(token)
client.run(token)





