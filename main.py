import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import json
import os

client = commands.Bot(command_prefix = '?')

@client.event
async def on_ready():
    print("The Bot is now ready for use!")
    print("-----------------------------")



@client.command()
async def test(ctx):
    await ctx.send("TEST")
    
client.run('KEY')

@client.event
async def on_message(message):

    if message.content == "Retard, Skibidi, Rizz, Gyatt, Rizzler, Paki, Nigga, Nigger, Twink, Chink, Tranny, Faggot":
        await message.delete()
        await message.channel.send("Message deleted as it contained one or more blacklisted words.")

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.sned(f'User {member} has been kicked')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to kick members.")



@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.sned(f'User {member} has been banned.')
    
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to ban members.")
  
