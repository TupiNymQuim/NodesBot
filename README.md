
# Incognito Bot

![Version](https://img.shields.io/badge/version-0.0.2-blue)
![GitHub Issues](https://img.shields.io/github/issues/tupinymquim/IncognitoBot.svg) 
![Live Demo](https://img.shields.io/badge/status-online-blue.svg)

<img src="https://github.com/TupiNymQuim/incognito_bot_t/assets/95882160/145a4f4e-fcdf-47e1-aa88-b426c68ebb4c" width=200 height=200></img>

A bot to show real-time node status and other utilities for TupiNymQuim

## References

 - [pyTelegramBot](https://github.com/eternnoir/pyTelegramBotAPI)
 - [DiscordPy](https://discordpy.readthedocs.io/en/latest/index.html)

## API documentation

#### Return node status by explorer ID

```http
  GET /mixnodes/<nodeid>
```

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `nodeid` | `string` | **Required**. Node ID|

## Demo

![Demo](https://github.com/TupiNymQuim/IncognitoBot/assets/95882160/eec24c81-920c-47e7-8965-bf3d0f7974e0)
## Features

- View node status

## Environment Variables

To run this project, you will need to add the following environment variables to your .env

`TELEGRAM_API_TOKEN` - A Telegram Token API. (Get it at [FatherBot](https://web.telegram.org/k/#@BotFather))

`DISCORD_API_TOKEN` - (Get it at [Discord Developer Portal](https://discord.com/developers/applications))
  

`DISCORD_ID_CHANNEL`


## Feedback

If you have any feedback, please let us know via tupinymquim@gmail.com


## Installation

### How to install the discord bot:

#### Prerequisites
- Python3.8 or newer
#### Setup
    1) Browse to the discord folder using `cd discord`
    2) Install the requirements using `pip install -r requirements.txt`
    3) Run the app using `python3 start.py`


### How to install the telegram bot:

#### Prerequisites
- Python3.8 or newer
  
#### Setup
    1) Browse to the telegram folder using `cd telegram`
    2) Install the requirements using `pip install -r requirements.txt`
    3) Run the app using `python3 start.py`


### How to use the handler:
#### Prerequisites
-  Python 3.8 or newer
#### Setup
    1) Browse to the api folder using `cd handler`
    1) Install the requirements using `pip install -r requirements.txt`
    2) Run the app using `python3 handler.py`


## Authors
[@vitorsantanna2](https://github.com/vitorsantanna2)

## Contributions
Contributions and Suggestions are always welcome!

Open a pull request or issue.

## License

[MIT](https://choosealicense.com/licenses/mit/)
