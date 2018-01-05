import discord
import asyncio
import random
import pickle
import os
from discord.ext.commands import Bot
from discord.ext import commands

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_member_join(member):
    UserID = member.id
    await client.send_message(client.get_channel("282007993938083841"), "Welcome <@%s> to my trashcan! Feel free to shitpost here. Check #Rules for the rules of the server" % (UserID))

@client.event
async def on_member_remove(member):
    UserID = member.id
    await client.send_message(client.get_channel("282007993938083841"), "<@%s> has left the trash can" % (UserID))
	
@client.event
async def on_message(message):
    if message.content.startswith('!potato'):      
          await client.send_message(message.channel, 'potato confirmed!')
client.run('Mzk4Njc5OTg1MjQzODE1OTU3.DTFdOw.jNL5fGYwv28pL_SH6pW0KRdnEw0')
