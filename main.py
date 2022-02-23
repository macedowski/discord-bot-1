from discord.ext import commands
TOKEN = "OTQ2MDk4MTU5OTM4MDc2Njc1.YhZwkg.wYcWmunc6SRfkaFVU5DnRn75vK0"

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
