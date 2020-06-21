# bot.py
import os

import discord
from dotenv import load_dotenv

token_file = open("token.txt")
token = token_file.read()

load_dotenv()
TOKEN = os.getenv(token)

print(token)

