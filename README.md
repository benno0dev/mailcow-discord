# A Mailcow Discord-bot
A very simple bot to create aliases for a mailcow-mailserver
## Installation
```
git clone https://github.com/benno0dev/mailcow-discord
```
```
cd mailcow-discord
```
- Create a file named ".env" and paste the code down below in there and edit it to fit your server
```bash
TOKEN="MSADA47834..."
ALLOWED_USERS=12843828384, 28382830028
DOMAIN="example.org"
USER="user"
API_KEY="77SDSD8-9273FFA..."
```
TOKEN: your discord bot token\
ALLOWED_USERS: discord user ids who are allowed to use the bot (seperated by ", ")\
DOMAIN: your domain you also use for your mail server and for emails (only works if your mailserver runs on mail-subdomain (mail.example.org) and your emails run on that domain (user@example.org))\
USER: the email address you wanna give the aliases to (the left side of the email)\
API_KEY: your mailcow api key
- Recommended: create a venv (has not been tested with no venv enabled)
- Install the requirements
```bash
pip install -r requirements.txt
```
- Run main.py (in your venv)
## Issues, Whishes and more
- Open an Issue (might not see it lol)
- DM me on [Twitter](https://x.com/benno0_), [Bluesky](https://bsky.app/profile/benno0.bsky.social) or Discord (@benno0_)
