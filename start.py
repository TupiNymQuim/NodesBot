import telebot
from settings import TOKEN


bot = telebot.TeleBot(TOKEN)


# Aguarda a inserção dos comandos espeficificados
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # Responde o usuário que inseriu o comando
	bot.reply_to(message, "Howdy, how are you doing?")


# Aguarda a entrada de novos membros no chat
@bot.message_handler(content_types=["new_chat_members"])
def on_new_chat_member(message):
    # Obtém o id do grupo
    chat_id = message.chat.id

    # Obtém o nome do usuário que entrou no grupo
    user_name = message.new_chat_members[0].first_name

    # Envia uma mensagem ao grupo
    bot.send_message(chat_id, f"Olá, {user_name}!\nSeja bem-vindo ao canal oficial do Squad TupiNymQuim!\nAcesse nossa página em: https://tupinymquim.github.io\nEstá procurando um node para delegar seus nym tokens e contribuir para a privacidade no mundo? Veja a nossa familia de nodes em: https://tupinymquim.github.io/nodes/\nQuer ficar por dentro do que a TupiNymQuim tem feito de contribuições? Veja em https://tupinymquim.github.io/contribuicoes/")

bot.infinity_polling()
