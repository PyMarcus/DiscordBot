import discord
from discord.ext import commands
import datetime

cliente = commands.Bot(command_prefix=">", case_insensitive=True)  # define how to call and add case insensitive


"""
lets see if the bot is on
"""

@cliente.event
async def ligado():
    print("ON")

"""
lets to write commands
"""
# verify
@cliente.command()
async def verificar(contexto):
    print(f"Sim, estou ativo.\nTenha um bom dia, {cliente.user}")
    print(f"Bip Bop! Eu sou uma criação perfeita do Marcus e estou aqui para ajudar!")
    await  contexto.send(f"Sim, estou ativo.\nTenha um bom dia, {cliente.user}")
    await  contexto.send(f"Bip Bop! Eu sou uma criação perfeita do Marcus e estou aqui para ajudar!")

# say hello
@cliente.command()
async def ola(contexto):
    await contexto.send(f"Bip, bop... Olá também, {cliente.user}!")

# datatime information
@cliente.command()
async def data(contexto):
    await contexto.send(f"{cliente.user}, hoje são, exatamente: {datetime.datetime.now()}")

# about me
@cliente.command()
async def sobre(contexto):
    await contexto.send("Para mais informações acesse: https://www.github.com/PyMarcus")

def membros():
    # about all members
    for guild in cliente.guilds:
        for member in guild.members:
            print(member)
            yield member

@cliente.command()
async def members(contexto):
    await contexto.send(list(membros()))


if __name__ == '__main__':
    cliente.run('ODk0MjM3NzgwOTcwOTcxMTY2.YVnF1Q.yjANn2dpOn9HYG1BFlYR5kdqDUU')
