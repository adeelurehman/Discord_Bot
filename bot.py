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
async def permss(ctx, courses=None):
    id = ctx.author.id
    print(str(ctx.author.mention))
    print(id)
    for channel in ctx.guild.text_channels:
        perms = channel.overwrites_for(member)
        perms.send_messages = False
        print(str(channel))
        await channel.set_permissions(id, overwrite=perms, reason="Muted!")
    await ctx.send(f"{id} has been muted.")

@client.command()
async def perms(ctx, member: discord.Member):
    for channel in ctx.guild.text_channels:
        if channel=='general':
        perms = channel.overwrites_for(member)
        perms.send_messages = False
        perms.read_messages = False
        await channel.set_permissions(member, overwrite=perms, reason="Muted!")
    await ctx.send(f"{member} has been muted.")




token_file = open("token.txt",'r')
for l in token_file:
    token = l
    print(token)
client.run(token)





