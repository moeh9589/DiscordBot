import os
import sys
import discord
from dotenv import load_dotenv
import random
from discord import file

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.channel.send(
        f'Hi {member.name}, welcome to Potato'
    )

@client.event
async def on_message(message):
    channel = client.get_channel(939652486212509739)


    
        # await channel.send(file=picture)
    if message.author == client.user:
        return

    if message.content.lower() == 'potato':
        path = "C:\\Users\\justi\\DiscordBot\\potatoes"
        files = os.listdir(path)

        d = random.choice(files)
        d = "C:/Users/justi/DiscordBot/potatoes/" + d
        print(d)
        with open(d.strip("'"), 'rb') as f:
            picture = discord.File(f)

        response = "Potato"

        await message.channel.send(response)
        await channel.send(file=picture)

    elif message.content.lower() == 'donut':
        path = "C:\\Users\\justi\\DiscordBot\\donuts"
        files = os.listdir(path)

        d = random.choice(files)
        d = "C:/Users/justi/DiscordBot/donuts/" + d

        with open(d.strip("'"), 'rb') as f:
            picture = discord.File(f)

        response = "Donut"
        await message.channel.send(response)
        await channel.send(file=picture)

    elif 'dick' in message.content.lower():
        response = "Jeff's is tiny"
        
        await message.channel.send(response)

    elif message.content.lower() == "josh":
        response = "no hoes"

        await message.channel.send(response)

    elif 'josh' and 'porn' in message.content.lower():
        path = "C:\\Users\\justi\\DiscordBot\\gifs"
        files = os.listdir(path)

        d = random.choice(files)
        d = "C:/Users/justi/DiscordBot/gifs/" + d

        with open(d.strip("'"), 'rb') as f:
            picture = discord.File(f)

        response = "no hoes"
        await message.channel.send(response)

        await channel.send(file=picture)
        
    elif "porn" in message.content.lower():
        path = "C:\\Users\\justi\\DiscordBot\\gifs"
        files = os.listdir(path)

        d = random.choice(files)
        d = "C:/Users/justi/DiscordBot/gifs/" + d

        with open(d.strip("'"), 'rb') as f:
            picture = discord.File(f)

        await channel.send(file=picture)




# @bot.command(name='clear', help='this command will clear msgs')
# async def clear(ctx, amount = 50): # Change amount
#   if ctx.message.author.id == ("Justinmo17"):
#     await ctx.channel.purge(limit=amount)
#   else:
#     await ctx.channel.send(f"{ctx.author.mention} you are not allowed")

client.run(TOKEN)