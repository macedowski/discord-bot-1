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
    
    if message.content == 'Julio':
        await message.channel.send('Julio eh otaku')
    if message.content == 'julio':
        await message.channel.send('Julio, como vai sua tia?')
    if message.content == 'prova':
        await message.channel.send("Prova eh o caralho, tia do julio eh minha")

    await bot.process_commands(message)

bot.run(TOKEN)
