import telebot
from getfile import getnewmembers, setnewmembers, addnewmember, listnewmember, randommember, eraselist
from settings import TOKEN
from scraper import  getBS, getRoutingScore, getHourScore, getTitle

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['nodes'])
def send_welcome(message):
    bs = getBS("https://mixnet.explorers.guru/mixnode/7PvubVkboJQm881PxAJR6oBkMB6f8R1Au55tQjnmTasr")
    routing = getRoutingScore(bs)
    hour = getHourScore(bs)
    title = getTitle(bs)
    bot.reply_to(message, f"{title}\nAvgScore: {routing} HourScore: {hour}")
@bot.message_handler(commands=['apagar'])
def send_welcome(message):
    eraselist()
    bot.reply_to(message, "Lista Apagada")

@bot.message_handler(commands=['listar'])
def send_welcome(message):

    chat_id = message.chat.id
    size = getnewmembers() - 1
    text = ""
    while (size >= 0):
        text = text + listnewmember(size)
        size = size - 1
    bot.send_message(chat_id, f"Lista de Participantes do Sorteio:\n{text}")


@bot.message_handler(commands=['sortear'])
def send_welcome(message):
    chat_id = message.chat.id
    winner = randommember()
    bot.send_message(chat_id, f"O Vencedor do sorteio foi: {winner}")

@bot.message_handler(commands=['joined'])
def send_welcome(message):
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


bot.infinity_polling()