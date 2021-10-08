import discord.errors
from discord.ext import commands
import datetime
from dotenv import load_dotenv

players = {}
COR = 0xF7f2E


cliente = commands.Bot(command_prefix=">", case_insensitive=True)  # define how to call and add case insensitive


# COMMANDS

# verify
@cliente.command()
async def verificar(contexto):
    print(f"Sim, estou ativo.\nTenha um bom dia, {cliente.user}")
    print(f"Bip Bop! Eu sou uma criação perfeita do Marcus e estou aqui para ajudar!")
    await contexto.send(f"Sim, estou ativo.\nTenha um bom dia, {cliente.user}")
    await contexto.send(f"Bip Bop! Eu sou uma criação perfeita do Marcus e estou aqui para ajudar!")


# datatime information
@cliente.command()
async def data(contexto):
    await contexto.send(f"{cliente.user}, hoje são, exatamente: {datetime.datetime.now()}")


# about me
@cliente.command()
async def sobre(contexto):
    await contexto.send("Para mais informações acesse: https://www.github.com/PyMarcus")


# EVENTS


@cliente.event
async def on_message(message):
    """
    Detecta mensagens de cumprimentos
    """
    if message.content.startswith("oi") or message.content.startswith("olá") or message.content.startswith("ei") or message.content.startswith("opa"):
        await message.channel.send(f"Bip, bop... Olá, {cliente.user}!")


@cliente.event
async def on_ready():
    print("ON")


@cliente.event
async def on_message(msg):
    """
    read the channel
    """
    if msg.content.startswith("bora") or msg.content.startswith("vamo") or msg.content.startswith("pronto"):
        await msg.channel.send("Finalmente...")

    if msg.content.startswith("flw") or msg.content.startswith("bye") or msg.content.startswith("até"):
        await msg.channel.send("Vai com Deus...")

    if msg.content.startswith("blz"):
        await msg.channel.send("OK")
        
        

    # private messages:
    # block:
    lista_palavroes = [
        'lista de palavrões para bloqueio'
        ]
    for words in lista_palavroes:
        if words.lower() in msg.content.lower():
            await msg.author.send("Linguajar chulo não será tolerado!")
        if words.lower() in msg.content.lower():
            await msg.delete(delay=None)
    if msg.content == "ping":
        await msg.channel.send(f"pong com a latência(ping) de : {round(cliente.latency, 2) * 1000} ms\nOu seja, este "
                               f"é o tempo para ir do seu dispositivo ao servidor do discord")

        
        

    # musica
    if msg.content == 'chegaMais' and msg.author.voice.channel:  # enter in the channel
        channel = msg.author.voice.channel
        await channel.connect() # enter

    if msg.content == "boraBot":
        channel1 = msg.author.voice.channel
        return channel1.disconnect() #get out of the channel

    

    #Music player:
if __name__ == '__main__':
    load_dotenv()
    token = 'token here'
    cliente.run(token)
