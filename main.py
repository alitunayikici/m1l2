import discord

from config import token

import os
import random

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


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


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """bu kod ile o havali mi onu bulabiliyoruz"""
    if ctx.invoked_subcommand is None:
        await ctx.send(f'Hayır, {ctx.subcommand_passed} havalı değil.')


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')


@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong!🏓 Gecikmen:{round(bot.latency * 1000)}ms")


@bot.command()
async def carpma(ctx, left: int, right: int):
    """Multiplies two numbers together."""
    await ctx.send(left * right)


@bot.command()
async def bolme(ctx, left: int, right: int):
    """Divides two numbers together."""
    await ctx.send(left / right)


@bot.command()
async def cikarma(ctx, left: int, right: int):
    """Subtracts two numbers together."""
    await ctx.send(left - right)


@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def mem2(ctx):
    with open('images/mem2.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def mem3(ctx):
    with open('images/mem3.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def kedim(ctx):
    with open('images/kedim.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def mem1(ctx):
    with open('images/mem1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def kelime(ctx, *arg):
    """Adds letters together."""
    await ctx.send(''.join(arg))

@bot.command()
async def yardım(ctx):
    await ctx.send("$hello: merhaba der            $add: $add 1 2'yi toplar          $_bot: bot havalı mı onu test eder            $ping: gecikmenizin ne kadar olduğunu ölçer           $carpma, $bolme, $cikarma: bunlar ile aynı toplamadaki gibi bölüp çarpıp çıkarabilirsiniz             $mem: 4 mem arasından rastgele bir mem atar         $mem1, $mem2, $mem3: seçilmiş memleri atar         $kedim: kedi fotoğrafı atar                            $kelime: toplamadaki gibi ama $kelime mer ha ba = merhaba der          $sayı: $sayı 1 100 bu şekilde 1 ile 100 arasında sayı seçer         $sa: sana aleyküm selam der")

@bot.command()
async def sayı(ctx, left: int, right: int):
    random_number = random.randint(left, right) 
    await ctx.send(f"Rastgele sayı: {random_number}") 

@bot.command()
async def sa(ctx):
    await ctx.send(f'Aleyküm selâm ben {bot.user}')

@bot.command()
async def çöp1(ctx):
    with open('words/kelime.txt'):
        copler = discord.File()
    await ctx.send(file=copler)

çöp2 = input("plastik hangi renk?")
print(os.listdir('images'))

bot.run(token)
