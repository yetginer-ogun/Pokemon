import discord
from discord.ext import commands
from config import token
from logic import Pokemon

intents = discord.Intents.default()  
intents.messages = True              
intents.message_content = True       
intents.guilds = True                


bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Giriş yapıldı:  {bot.user.name}')  

# '!go' komutu
@bot.command()
async def go(ctx):
    author = ctx.author.name  
    if author not in Pokemon.pokemons.keys():
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
