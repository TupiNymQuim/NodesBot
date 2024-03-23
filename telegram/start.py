import telebot
from telebot import custom_filters
import requests
from getfile import getnewmembers, setnewmembers, addnewmember, listnewmember, randommember, eraselist
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['nodes'])
def list_nodes(message):
    i = 0
    text = ""
    if (len(message.text) < 7):
        while (i < 6):
            res = requests.get("http://localhost:5000/tupi" + str(i + 1))
            temp = res.json()
            text = text + temp.get("title") + "\n" + "Avg Score: " + temp.get("avg_uptime") + "\nRouting Score: " + temp.get("node_performance") + "%\nTotal Stake: " + temp.get("total_stake")[:6] + "\nLocation: " + temp.get("location") + "\n" + "----------------------------------\n"
            i = i + 1
    elif (message.text[7:10] == '-id'):
        try:
            res = requests.get("http://localhost:5000/mixnodes/" + message.text[11:])
            temp = res.json()
            text = "Avg Score: " + temp.get("avg_uptime") + "\nRouting Score: " + temp.get("node_performance") + "%\nTotal Stake: " + temp.get("total_stake") + "\nLocation: " + temp.get("location")
        except:
            text = "invalid id"
    else:
        try:
            res = requests.get("http://localhost:5000/tupi" + message.text[7])
            temp = res.json()
            text = temp.get("title") + "\n" + "Avg Score: " + temp.get("avg_uptime") + "\nRouting Score: " + temp.get("node_performance") + "%\nTotal Stake: " + temp.get("total_stake") + "\nLocation: " + temp.get("location")
        except:
            text = "invalid arguments"
    bot.reply_to(message, f"{text}")

@bot.message_handler(commands=['gateways'])
def list_gateways(message):
    i = 0
    text = ""
    if (len(message.text) < 10):
        while (i < 8):
            res = requests.get("http://localhost:5000/gateway" + str(i + 1))
            temp = res.json()
            print(temp)
            text = text + temp.get("title") + "\n" + "Status: " + temp.get("status") + "\n" + "Uptime: " + temp.get("uptime") + "\nPerformance: " + temp.get("most_recent") + "%\n"
            i = i + 1
    else:
        try:
            res = requests.get("http://localhost:5000/gateway" + message.text[10])
            temp = res.json()
            text = text + temp.get("title") + "\n" + "Status: " + temp.get("status") + "\n" + "Uptime: " + temp.get("uptime") + "\nPerformance: " + temp.get("most_recent") + "%\n"
        except:
            text = "invalid arguments"
    bot.reply_to(message, f"{text}")

@bot.message_handler(chat_id=[2092310259], commands=['apagar'])
def delete_list(message):
    eraselist()
    bot.reply_to(message, "Lista Apagada")

@bot.message_handler(commands=['listar'])
def show_list(message):

    chat_id = message.chat.id
    size = getnewmembers() - 1
    text = ""
    while (size >= 0):
        text = text + listnewmember(size)
        size = size - 1
    bot.send_message(chat_id, f"Lista de Participantes do Sorteio:\n{text}")


@bot.message_handler(commands=['sortear'])
def random_list(message):
    chat_id = message.chat.id
    winner = randommember()
    bot.send_message(chat_id, f"O Vencedor do sorteio foi: {winner}")

@bot.message_handler(commands=['joined'])
def joined_list(message):
    # Responde o usuário que inseriu o comando
    bot.reply_to(message, "Tivemos " + str(getnewmembers()) + " novos membros.")


# Aguarda a entrada de novos membros no chat
@bot.message_handler(content_types=["new_chat_members"])
def on_new_chat_member(message):
    # Obtém o id do grupo
    chat_id = message.chat.id

    # Obtém o nome do usuário que entrou no grupo
    user_name = message.new_chat_members[0].username
    first_name = message.new_chat_members[0].first_name

    if (user_name != None):
        user_name = "@" + user_name
        addnewmember(user_name)
    else:
        addnewmember(first_name)
        user_name = first_name
    # Envia uma mensagem ao grupo
    bot.send_message(chat_id, f"Olá, {user_name}!\nSeja bem-vindo ao canal oficial do Squad TupiNymQuim!\nAcesse nossa página em: https://tupinymquim.github.io\nEstá procurando um node para delegar seus nym tokens e contribuir para a privacidade no mundo? Veja a nossa familia de nodes em: https://tupinymquim.github.io/nodes/\nQuer ficar por dentro do que a TupiNymQuim tem feito de contribuições? Veja em https://tupinymquim.github.io/contribuicoes/")

    setnewmembers(getnewmembers() + 1)

bot.add_custom_filter(custom_filters.ChatFilter())

bot.infinity_polling()
