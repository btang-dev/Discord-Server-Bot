# Discord Server Bot (Python)

A simple bot that manages and moderates your discord server. It can assign and remove roles, manage messages, and create polls by itself.

---

## Features

- Responds to a `!hello` command
- Assigns and removes a configured role from a user (`!assign`, `!remove`)
- Send direct messages to users using `!dm` (example: `!dm Hello there`)
- Reply to messages with `!reply`
- Create a quick poll (adds 👍/👎 reactions) with `!poll` (example: `!poll Is pizza best food?`)
- Sends a welcome DM to users who join the server
- Auto-moderation: deletes messages containing some banned words and sends a warning message
- `!secret` command that is restricted to users with the configured secret role
- Logging to `discord.log`

---

## Project structure

- `main.py` - Main bot implementation file with example commands and events
- `requirements.txt` - Python package dependencies
- `.env` - Environment variables (do not commit to version control; contains the bot token)
- `discord.log` - Bot log output file (created at runtime)

---

## Prerequisites

- Python 3.11+ (3.13 used in development, but the bot works with typical 3.10+ environments used with discord.py 2.x)
- A Discord bot token (create one at the Discord Developer Portal)

---

## Quick setup (recommended: virtual environment)

1. Clone the repo (or copy files into your workspace)
2. Create a virtual environment and activate it (Windows PowerShell):

```powershell
C:/Users/iking/AppData/Local/Microsoft/WindowsApps/python3.13.exe -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

4. Create a `.env` file in the project root with your Discord token (do not commit this to version control):

```dotenv
DISCORD_TOKEN=your_discord_bot_token_here
```

> Important: You currently already have a `.env` file in the repository. It's recommended to remove real tokens from version control, rotate the token if it was accidentally committed, and use a `.env.example` file with placeholder values instead.

5. Ensure your bot is invited to your server with the required permissions and intents (see below).

6. Run the bot:

```powershell
python main.py
```

---

## Required Discord Bot Settings & Permissions

- Go to the Discord Developer Portal -> Your App -> Bot -> Privileged Gateway Intents
  - Enable the `Message Content Intent` and `Server Members Intent` (the code sets these: `intents.message_content = True` and `intents.members = True`).
- Invite the bot to your server using OAuth2 URL builder (select the `bot` scope and add the permissions you need, typically `Send Messages`, `Manage Messages`, `Add Reactions`, `Manage Roles` for role-assignment functionality).

---

## Role configuration

The bot assigns/removes a role called `Cool Role` by default. The role name is stored in `main.py`:

```python
secret_role = "Cool Role"
```

Make sure you either (a) create a role named `Cool Role` in the server, or (b) change the `secret_role` variable to match the role name you'd like to use.

---

## Commands

- `!hello` - Bot greets the user
- `!assign` - Assigns the configured secret role (if it exists)
- `!remove` - Removes the configured secret role (if it exists)
- `!dm <message>` - Sends a DM to the user that invoked the command
- `!reply` - Bot replies directly to your message
- `!poll <question>` - Posts an embedded poll and adds 👍/👎 reactions
- `!secret` - Restricted command; only users with the configured `secret_role` can use it

---

## Logging

- Bot writes logs to `discord.log` in the project root. The logging handler is created in `main.py`:
  - `logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')`

---

## Contributing

If you'd like to help extend the bot, please follow these suggested steps:

1. Make a feature branch
2. Keep secrets out of version control (.env should not be tracked)
3. Create a PR describing your change

