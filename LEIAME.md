
# Incognito Bot

![Version](https://img.shields.io/badge/versão-0.0.2-blue)
![GitHub Issues](https://img.shields.io/github/issues/tupinymquim/IncognitoBot.svg) 
![Live Demo](https://img.shields.io/badge/status-online-blue.svg)

<img src="https://github.com/TupiNymQuim/incognito_bot_t/assets/95882160/145a4f4e-fcdf-47e1-aa88-b426c68ebb4c" width=200 height=200></img>

Um bot para visualizar o status dos nodes em tempo real e um utilitário para gerência dos canais da TupiNymQuim.

## Referências

 - [pyTelegramBot](https://github.com/eternnoir/pyTelegramBotAPI)
 - [DiscordPy](https://discordpy.readthedocs.io/en/latest/index.html)

## Documentação da API

#### Retorna o status do node através do ID do Nym Explorer

```http
  GET /mixnodes/<nodeid>
```

| Parâmetro   | Tipo      | Descrição                          |
| :---------- | :--------- | :---------------------------------- |
| `nodeid` | `string` | **Obrigatório**. Node ID|

## Demo

![Demo](https://github.com/TupiNymQuim/IncognitoBot/assets/95882160/eec24c81-920c-47e7-8965-bf3d0f7974e0)
## Features

- Vê o status do node

## Variáveis de Ambiente

Para executar este projeto, você vai precisar adicionar as seguintes variáveis de ambiente em seu .env

`TELEGRAM_API_TOKEN` - (Consiga uma em [FatherBot](https://web.telegram.org/k/#@BotFather))

`DISCORD_API_TOKEN` - (Consiga uma em  [Discord Developer Portal](https://discord.com/developers/applications))
  

`DISCORD_ID_CHANNEL` - (Para as mensagens de boas vindas do Discord, id do canal em que ele está)


## Feedback

Se você tiver qualquer feedback, deixe-nos saber através de tupinymquim@gmail.com


## Instalação

### Como instalar o bot do Discord:

#### Pré-Requisitos
- Python3.8 ou superior
#### Configuração
    1) Navegue para a pasta do discord usando `cd discord`
    2) Instale os requisitos usando `pip install -r requirements.txt`
    3) Execute o aplicativo usando `python3 start.py`


### Como instalar o bot do Telegram:

#### Pré-requisitos
- Python3.8 ou superior
  
#### Configuração
    1) Navegue para a pasta do telegram usando `cd telegram`
    2) Instale os requisitos usando `pip install -r requirements.txt`
    3) Execute o app usando `python3 start.py`


### Como usar o Handler:
#### Pré-requisitos
- Python3.8 ou superior
#### Configuração
    1) Navega para a pasta do handler usando `cd handler`
    2) Instale os requisitos usando `pip install -r requirements.txt`
    3) Execute o aplicativo usando `python3 handler.py`

## Autores
[@vitorsantanna2](https://github.com/vitorsantanna2)

## Contribuições
Contribuições e sugestões são sempre bem-vindas.

Abra uma pull request ou crie uma issue.

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
