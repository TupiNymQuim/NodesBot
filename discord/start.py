import os
import sys
sys.path.append('/root/NodesBot/')
import discord
import requests
from discord.ext import commands
from settings import DISCORD_API_TOKEN, ID_CHANNEL, commandPrefix
import utils.utils as utils


IncognitoBot = commands.Bot(intents=discord.Intents.all(), command_prefix=commandPrefix)

async def on_message(message):
    if(message.channel.id == 1233766482257907813):
        if message.author != IncognitoBot.user:
            if(message.content == "!Ola"):
                await message.channel.send("Olá! O que gostaria de fazer?")
                await message.channel.send("1 ) !tarefas")
                await message.channel.send("--- Você pode: ""!tarefas adicionar"" para adicionar um item em sua lista de tarefas")
                await message.channel.send("--- Você pode: ""!tarefas remover"" para remover um item da sua lista de tarefas com base no indice")
                await message.channel.send("--- Você pode: ""!tarefas listar"" para listar sua lista de tarefas")
                await message.channel.send("2) !juntar -- junta uma string e a retorna como uma coisa só")
            if(message.content == "!tarefas listar"):
                with open("tarefas.txt", 'r') as arquivo:
                    if(os.path.getsize("tarefas.txt") == 0):
                        await message.channel.send("Sinto muito, mas sua lista está vazia")
                    else:
                        for linha in arquivo:
                            await message.channel.send(linha.strip())

            if(message.content.startswith ("!tarefas adicionar")):
                aux = message.content[18:]
                with open("tarefas.txt", 'a') as arquivo:
                    arquivo.write(aux + '\n') 
                    await message.channel.send("Tarefa adicionada com sucesso")

            if(message.content.startswith ("!tarefas remover")):
                aux = message.content[16:]
                try:
                    aux = int(aux) - 1
                    with open("tarefas.txt", 'r') as arquivo:
                        linhas = arquivo.readlines()
                    with open("tarefas.txt", 'w') as arquivo:
                        for i, linha in enumerate(linhas):
                            if i != aux:
                                arquivo.write(linha)
                except ValueError:
                    await message.channel.send("Inválido")


@IncognitoBot.command()
async def add(message, *lista):
    await message.reply(utils.set_item(lista[0]))

@IncognitoBot.command()
async def remove(message, *lista):
    print(lista)
    await message.reply(utils.remove_item(lista[0]))

@IncognitoBot.command()
async def list(message):
    i = 0
    temp = ""
    while (i < len(utils.get_item())):
        temp =  temp + utils.get_item()[i]
        i = i + 1
    await message.reply(f"{temp}")

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
    i = 0
    text = ""
    if (len(nodes) == 0):
        while (i < 7):
            res = requests.get("http://localhost:5000/nodes" + str(i + 1))
            temp = res.json()
            text = text + temp.get("title") + "\n" + "Avg Score: " + temp.get("avg_uptime") + "\nRouting Score: " + temp.get("node_performance") + "%\nTotal Stake: " + temp.get("total_stake")[:6] + "\nLocation: " + temp.get("location") + "\n" + "----------------------------------\n"
            i = i + 1
    elif (message.text[7:10] == '-id'):
        try:
            res = requests.get("http://localhost:5001/mixnodes/" + message.text[11:])
            temp = res.json()
            text = "Avg Score: " + temp.get("avg_uptime") + "\nRouting Score: " + temp.get("node_performance") + "%\nTotal Stake: " + temp.get("total_stake") + "\nLocation: " + temp.get("location")
        except:
            text = "invalid id"
    else:
        try:
            res = requests.get("http://localhost:5000/nodes" + message.text[7])
            temp = res.json()
            text = temp.get("title") + "\n" + "Avg Score: " + temp.get("avg_uptime") + "\nRouting Score: " + temp.get("node_performance") + "%\nTotal Stake: " + temp.get("total_stake") + "\nLocation: " + temp.get("location")
        except:
            text = "invalid arguments"
    await message.reply(f"{text}")

@IncognitoBot.command()
async def gateways(message, *gateways):
    i = 0
    text = ""

    if (len(gateways) == 0):
        while (i < 12):
            res = requests.get("http://localhost:5000/gateway" + str(i + 1))
            temp = res.json()
            text = text + temp.get("title") + "\n" + "Status: " + temp.get("status") + "\n" + "Uptime: " + temp.get("uptime") + "\nPerformance: " + temp.get("most_recent") + "%\nConfig Score: " + temp.get("config_score") + "\n-----------------------------------\n"
            i = i + 1
    elif (message.text[10:13] == '-id'):
        try:
            res = requests.get("http://localhost:5001/gateways/" + message.text[14:])
            temp = res.json()
            text = text + temp.get("title") + "\n" + "Status: " + temp.get("status") + "\n" + "Uptime: " + temp.get("uptime") + "\nPerformance: " + temp.get("most_recent") + "%\nConfig Score: " + temp.get("config_score") + "\n-----------------------------------\n"
            i = i + 1
        except:
            text = "invalid arguments"
    else:
        try:
            res = requests.get("http://localhost:5000/gateway" + message.text[10:])
            temp = res.json()
            text = text + temp.get("title") + "\n" + "Status: " + temp.get("status") + "\n" + "Uptime: " + temp.get("uptime") + "\nPerformance: " + temp.get("most_recent") + "%\nConfig Score: " + temp.get("config_score") + "\n-----------------------------------\n"
        except:
            text = "invalid arguments"
    await message.reply(f"{text}")

@IncognitoBot.command()
async def commands(message):
    await message.reply(f"Tupinymquim only taught me how to say hello so far, I will soon have more features.")

IncognitoBot.run(DISCORD_API_TOKEN)