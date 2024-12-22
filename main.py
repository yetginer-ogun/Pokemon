import discord
from discord.ext import commands
from config import token
from logic import *
import random

intents = discord.Intents.default()  
intents.messages = True              
intents.message_content = True       
intents.guilds = True                


bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Giriş yapıldı:  {bot.user.name}')  


@bot.command()
async def go(ctx):
    author = ctx.author.name  
    if author not in Pokemon.pokemons.keys():
        sinif = random.randint(1,3)
        if sinif == 1:
            pokemon = Pokemon(author)  
        elif sinif == 2:
            pokemon = Warrior(author)
        elif sinif == 3:
            pokemon = Mage(author)
        else:
            pokemon = Pokemon(author)
        await ctx.send(await pokemon.info())  
        image_url = await pokemon.show_img() 
        if image_url:
            embed = discord.Embed()  
            embed.set_image(url=image_url)  
            await ctx.send(embed=embed)  
        else:
            await ctx.send("Pokémonun görüntüsü yüklenemedi!")
    else:
        await ctx.send("Zaten kendi Pokémonunuzu oluşturdunuz!")  


bot.run(token)
