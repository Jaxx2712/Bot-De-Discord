import discord
import random
import os
import requests

from discord.ext import commands
from settings import token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def saludo(ctx):
    await ctx.send("Hola, bienvenido a mi servidor!")

@bot.command()
async def saludo_nombre(ctx, nombre:str):
    await ctx.send(f"Hola, {nombre} bienvenido a mi servidor!")

@bot.command()
async def suma(ctx, numero1:int, numero2:int):
    await ctx.send(f"La suma de {numero1} + {numero2} es {numero1 + numero2}")

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def meme(ctx):
    with open("imagenes/meme1.jpeg", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def memes(ctx):
    imagenes = os.listdir("imagenes")
    with open(f"imagenes/{random.choice(imagenes)}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)

    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que darme un pokemon")

@bot.command()
async def memes_animales(ctx):
    memes_animales = os.listdir("animales")
    with open(f"animales/{random.choice(memes_animales)}", "rb") as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def reciclar(ctx):
    await ctx.send(f"https://www.youtube.com/watch?v=uaI3PLmAJyM, En pocas palabras,reciclar es muy importante para el medio ambiente, ya que lo vuelve un material nuevo y util, en vez de desecharlo y dañar el oceano o el aire. Un metodo practico seria buscar empresas que reciclen.")

@bot.command()
async def como_reciclar(ctx):
    await ctx.send(f"Podrias hacer una serie de manualidades que te gusten, pon el material reciclable que quieres utilizar para hacer tu manualidad. (plastico, papel o carton)")

@bot.command()
async def plastico(ctx):
    await ctx.send(f"https://www.youtube.com/watch?v=DpR2ICmNznY, este es un tutorial para que escojas lo que quieres hacer con plastico")

@bot.command()
async def papel(ctx):
    await ctx.send(f"https://www.youtube.com/watch?v=ulBc2ZAhzTs, este es un tutorial para que escojas lo que quieres hacer con papel")

@bot.command()
async def carton(ctx):
    await ctx.send(f"https://www.youtube.com/watch?v=sguZd31yyVU, este es un tutorial para que escojas lo que quieres hacer con carton")

bot.run(token)
