import discord
from discord import app_commands
import os
import requests
from dotenv import load_dotenv
load_dotenv()
#import tracemalloc #NEWLINE# tracemalloc.start()

TOKEN = os.getenv("TOKEN")
ALLOWED_USERS = [int(x.strip()) for x in os.getenv("ALLOWED_USERS").split(",")]
API_KEY = os.getenv("API_KEY")
DOMAIN = os.getenv("DOMAIN")
MAILCOW_URL = f"https://mail.{DOMAIN}/api/v1"
USER = os.getenv("USER")
MAILBOX = f"{USER}@{DOMAIN}"


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_console() # Only for live Console 

            
def create_email(name):
    alias = f"{name}@{DOMAIN}"
    data = {
        "active": "1",
        "address": alias,
        "goto": MAILBOX,
    }
    headers = {"X-API-Key": API_KEY}
    print(f"{MAILCOW_URL}/add/alias")
    print(data)
    r = requests.post(f"{MAILCOW_URL}/add/alias", json=data, headers=headers)
    if r.status_code == 200:
        print(r)
        print(r.headers)
        print(r.text)
        answer = f"Successfully created: {alias}!"
    else:
        answer = f"Error {r.status_code}: {r.text}"
    return answer

print(create_email(input()))
input()