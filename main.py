import discord, os, json, re, datetime, requests
from discord.ext import commands

client = commands.Bot(command_prefix='', self_bot=True)

def clear():
    if os.name != 'nt':
        os.system('clear')
    else:
        os.system('cls')

def install():
    if os.path.exists('./config.json'):
        return
    else:
        with open('./config.json', 'w') as f:
            tk = input('Enter your Discord token\n> ')
            data = {
                "token": tk
            }
            json.dump(data, f, indent=4)

install()

with open('./config.json', 'r') as ff:
    config = json.load(ff)
    
token = config.get('token')

@client.event
async def on_connect():
    print(f'Sniping Nitro and Slotbot on {len(client.guilds)} servers.\n\n')
            
@client.listen('on_message')
async def nitro(message):
    if 'discord.gift/' in message.content:
        start = datetime.datetime.now()
        code = re.search("discord.gift/(.*)", message.content).group(1)
        token = config.get('token')
        headers = {'Authorization': token}
        r = requests.post(
            f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
            headers=headers,
        ).text
        elapsed = f'{datetime.datetime.now() - start}s'

        if len(code) < 16 or len(code) > 20:
            print(f"[Nitro Sniper] Nitro Code sent by {message.author}.")
            print(f"[Nitro Sniper] Message Content: {message.content}")
            print(f"[Nitro Sniper] Server: {message.guild}")
            print(f"[Nitro Sniper] Channel: {message.channel}"       )
            print(f"[Nitro Sniper] Status: Fake Code")
            print(f"[Nitro Sniper] Date: {datetime.datetime.now().strftime('%H:%M:%S %p')}")
            print(f"[Nitro Sniper] Elapsed: {elapsed}\n\n")

        elif 'This gift has been redeemed already.' in r:
            print(f"[Nitro Sniper] Nitro Code sent by {message.author}.")
            print(f"[Nitro Sniper] Message Content: {message.content}")
            print(f"[Nitro Sniper] Server: {message.guild}")
            print(f"[Nitro Sniper] Channel: {message.channel}"       )
            print(f"[Nitro Sniper] Status: Already Redeemed")
            print(f"[Nitro Sniper] Date: {datetime.datetime.now().strftime('%H:%M:%S %p')}")
            print(f"[Nitro Sniper] Elapsed: {elapsed}\n\n")

        elif 'subscription_plan' in r:
            print(f"[Nitro Sniper] Nitro Code sent by {message.author}.")
            print(f"[Nitro Sniper] Message Content: {message.content}")
            print(f"[Nitro Sniper] Server: {message.guild}")
            print(f"[Nitro Sniper] Channel: {message.channel}"       )
            print(f"[Nitro Sniper] Status: Successful")
            print(f"[Nitro Sniper] Date: {datetime.datetime.now().strftime('%H:%M:%S %p')}")
            print(f"[Nitro Sniper] Elapsed: {elapsed}\n\n")

        elif 'Unknown Gift Code' in r:
            print(f"[Nitro Sniper] Nitro Code sent by {message.author}.")
            print(f"[Nitro Sniper] Message Content: {message.content}")
            print(f"[Nitro Sniper] Server: {message.guild}")
            print(f"[Nitro Sniper] Channel: {message.channel}"       )
            print(f"[Nitro Sniper] Status: Unknown Code")
            print(f"[Nitro Sniper] Date: {datetime.datetime.now().strftime('%H:%M:%S %p')}")
            print(f"[Nitro Sniper] Elapsed: {elapsed}\n\n")

        else:
            pass
        
@client.listen('on_message')
async def slotbot(message):
    if message.author.id == 346353957029019648:
        if 'Hurry and pick it up' in message.content:
            await message.channel.send('~grab')
    else:
        pass
    
@client.event  
async def on_command_error(ctx, error):
    pass

clear()
client.run(token, bot=False)