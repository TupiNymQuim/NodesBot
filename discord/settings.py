import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

DISCORD_API_TOKEN = str(os.getenv("DISCORD_API_TOKEN"))
ID_CHANNEL = str(os.getenv("ID_CHANNEL"))

commandPrefix = "/"
