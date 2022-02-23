import os
from discord.ext import commands
TOKEN = os.getenv("TOKEN")

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user: 
        return
    
    if message.content == 'Julio' or "julio":
        await message.reply.channel.send('Julio eh bobao')
    if message.content == 'bye':
        await message.reply.channel.send(f'Goodbye {message.author}')

    await bot.process_commands(message)

bot.run(TOKEN)
