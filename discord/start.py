import discord
import requests
from discord.ext import commands
from settings import DISCORD_API_TOKEN, ID_CHANNEL, commandPrefix


IncognitoBot = commands.Bot(intents=discord.Intents.all(), command_prefix=commandPrefix)


@IncognitoBot.event
async def on_ready():
    print(f'Logado com sucesso como {IncognitoBot.user}')

@IncognitoBot.event
async def on_member_join(member):
    welcome_channel = IncognitoBot.get_channel(ID_CHANNEL)
    await welcome_channel.send(f"Olá, eu sou o Incognito, seja bem vindo ao servidor In The Galaxy, {member.mention}!")

@IncognitoBot.command()
async def hello(message): # Sem receber nenhum parâmetro
    await message.reply(f"Hello, {message.author.mention}!\nI am an anonymous search tool running through mixnet 👋")

@IncognitoBot.command()
async def nodes(message, *nodes):
    text = ""
    if (len(nodes) == 0):
        for x in range(6):
                temp = requests.get("http://localhost:5000/tupi" + str(x + 1)).json()
                text = text + temp.get("title") + "\n" + "Avg Score: " + temp.get("avg_uptime") + "\nRouting Score: " + temp.get("node_performance") + "%\nTotal Stake: " + temp.get("total_stake")[:6] + "\nLocation: " + temp.get("location") + "\n" + "----------------------------------\n"
    elif (len(nodes) == 1):
        temp = requests.get("http://localhost:5000/tupi" + nodes[0]).json()
        text = temp.get("title") + "\n" + "Avg Score: " + temp.get("avg_uptime") + "\nRouting Score: " + temp.get("node_performance") + "%\nTotal Stake: " + temp.get("total_stake") + "\nLocation: " + temp.get("location")

    await message.reply(f"{text}")

@IncognitoBot.command()
async def commands(message):
    await message.reply(f"Tupinymquim only taught me how to say hello so far, I will soon have more features.")

IncognitoBot.run(DISCORD_API_TOKEN)
