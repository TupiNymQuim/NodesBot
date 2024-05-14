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

@IncognitoBot.command()
async def gateways(message):
    i = 0
    text = ""
    if (len(message.text) < 11):
        while (i < 11):
            res = requests.get("http://localhost:5000/gateway" + str(i + 1))
            temp = res.json()
            text = text + temp.get("title") + "\n" + "Status: " + temp.get("status") + "\n" + "Uptime: " + temp.get("uptime") + "\nPerformance: " + temp.get("most_recent") + "%\nNetwork Requester: "  + temp.get("network_requester_enabled") + "\nIp Packet Router: " + temp.get("ip_packet_router_enabled") + "\nExit Policy: " + temp.get("exit_policy") + "\n-----------------------------------\n"
            i = i + 1
    elif (message.text[10:13] == '-id'):
        try:
            res = requests.get("http://localhost:5001/gateways/" + message.text[14:])
            temp = res.json()
            text = text + temp.get("title") + "\n" + "Status: " + temp.get("status") + "\n" + "Uptime: " + temp.get("uptime") + "\nPerformance: " + temp.get("most_recent") + "%\nNetwork Requester: "  + temp.get("network_requester_enabled") + "\nIp Packet Router: " + temp.get("ip_packet_router_enabled") + "\nExit Policy: " + temp.get("exit_policy") + "\n-----------------------------------\n"
            i = i + 1
        except:
            text = "invalid arguments"
    else:
        try:
            res = requests.get("http://localhost:5000/gateway" + message.text[10:])
            temp = res.json()
            text = text + temp.get("title") + "\n" + "Status: " + temp.get("status") + "\n" + "Uptime: " + temp.get("uptime") + "\nPerformance: " + temp.get("most_recent") + "%\nNetwork Requester: "  + temp.get("network_requester_enabled") + "\nIp Packet Router: " + temp.get("ip_packet_router_enabled") + "\nExit Policy: " + temp.get("exit_policy")
        except:
            text = "invalid arguments"
    await message.reply(text)


IncognitoBot.run(DISCORD_API_TOKEN)
