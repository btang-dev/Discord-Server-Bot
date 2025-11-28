import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

## LOADING ENVIRONMENT VARIABLES

load_dotenv()  # Load environment variables from a .env file (if present)
token = os.getenv('DISCORD_TOKEN')  # Load the Discord bot token from environment variables

if not token:
    print('ERROR: DISCORD_TOKEN not found in environment. Create a .env file with DISCORD_TOKEN or set the env var.')
    raise SystemExit(1)

## SETTING UP THE BOT

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w') ## Set up logging to a file, w means write mode
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

## CREATE THE BOT INSTANCE AND RUN IT

bot = commands.Bot(command_prefix='!', intents=intents) ## Create a bot instance with command prefix '!' and specified intents; ex: !help, !remove

secret_role = "Cool Role"

@bot.event
async def on_ready():
    print(f"We are ready to go! Logged in as {bot.user.name}") ## Print a message when the bot is ready

@bot.event
async def on_member_join(member):
    await member.send(f"{member} has joined the server!") ## Print a message when a new member joins the server

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return ## Ignore messages sent by the bot itself
    
    if "shit" in message.content.lower():
        await message.delete()  ## Delete messages containing the word
        await message.channel.send(f"Please watch your language, {message.author.mention}!") ## Respond to messages containing the word
    if "fuck" in message.content.lower():
        await message.delete()  ## Delete messages containing the word
        await message.channel.send(f"Please watch your language, {message.author.mention}!") ## Respond to messages containing the word
    
    await bot.process_commands(message) ## Process commands after handling the message

##
## COMMANDS
##


## Hello Command
@bot.command()
async def hello(ctx): ## ctx = context
    await ctx.send(f"Hello {ctx.author.mention}!")

## assign role
@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name = secret_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} is now assigned to {secret_role}")
    else:
        await ctx.send("This role does not exist.")

# remove role
@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name = secret_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} has had the {secret_role} removed.")
    else:
        await ctx.send("This role does not exist.")

## Direct Message ex: !dm hello world
@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f"You said {msg}")

## Replying to a message
@bot.command()
async def reply(ctx):
    await ctx.reply("This is a reply to your message.")

## Poll
@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title = "New Poll", description = question)
    poll_message = await ctx.send(embed = embed)
    await poll_message.add_reaction("👍")
    await poll_message.add_reaction("👎")

## If a person has a specific role
@bot.command()
@commands.has_role(secret_role)
async def secret(ctx):
    await ctx.send("Welcome to the Cool Role group!")

## If they do not have a role
@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You do not have permission to do that!")


bot.run(token, log_handler=handler, log_level = logging.DEBUG) ## Run the bot with the specified token