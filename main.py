from random import randint
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
    if message.author.name == "Julião":
        await message.reply('Cala boca julio')
        return await bot.process_commands(message)
    lista = ["Julio", "julio","otaku", "Otaku","prova","Prova","@Juliao","@Julião","Julião","Juliao"]
    for i in lista:
        b=0
        a = re.findall(i,message.content)
        if a !=[]:
            b = randint(1,4)
        if b == 1:
            await message.reply('Julio eh otaku')
            break
        elif b == 2:
            await message.reply('Julio, como vai sua tia?')
            break
        elif b == 3:
            await message.reply(f"{i} eh o caralho, tia do julio eh minha")
            break
        elif b == 4:
            await message.reply(f"ihhhhhhh ala, ta falando de {i}, o que importa mesmo eh a tia do julio")
            break
        

    await bot.process_commands(message)

bot.run(TOKEN)

