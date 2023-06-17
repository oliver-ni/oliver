import contextlib
import os

import discord

client = discord.Client(intents=discord.Intents(guilds=True, members=True))


@client.event
async def on_member_add(member: discord.Member):
    with contextlib.suppress(discord.Forbidden):
        await member.edit(nick="oliver")


client.run(os.environ["TOKEN"])
