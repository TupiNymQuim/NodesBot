import os
from dotenv import load_dotenv
# Load .env file
load_dotenv()

TOKEN = str(os.getenv("TOKEN"))
