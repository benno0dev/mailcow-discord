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

intents = discord.Intents.default()
intents.message_content = False
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)
            
def create_email(name):
    alias = f"{name}@{DOMAIN}"
    data = {
        "active": "1",
        "address": alias,
        "goto": MAILBOX,
        "domain": DOMAIN
    }
    headers = {"X-API-Key": API_KEY,
               "Content_Type": "application/json"}
    r = requests.post(f"{MAILCOW_URL}/add/alias", json=data, headers=headers)
    if r.status_code == 200:
        if not r.text == "":
            answer = f"Successfully created: {alias}!"
            print(r.text)
        else: answer = "Error: API request to Mailcow did not go through!"
    else:
        answer = f"Error {r.status_code}: {r.text}"
    return answer

def create_email_test(name):
    print(name)
    return f"Successful! {name}"

@tree.command(
    name="create_email",
    description="Creates an Email Address",
)
async def create_email_command(interaction, message: str):
    if interaction.user.id in ALLOWED_USERS:
        await interaction.response.send_message(create_email(message), ephemeral=True)
    else:
        await interaction.response.send_message("You cannot access this command, sorry :(", ephemeral=True)


@bot.event
async def on_ready():
    await tree.sync()
    print('Command Tree synced!')
    print('Ready!')


bot.run(TOKEN)
