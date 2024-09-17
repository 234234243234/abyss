import discord, os, asyncio, ctypes, random, string, json
from pystyle import Center
from colorama import Fore, init
from discord.ext import commands


init()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="=", intents=intents)


@bot.event
async def on_ready():
     await main()

with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)
def resize():
   if os.name == "nt":
      os.system("mode con: cols=60 lines=35")
   else:
      pass
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def title():
     if os.name == "nt":
          ctypes.windll.kernel32.SetConsoleTitleW(f"abyss | NYX tools | dsc.gg/nyxtools | nyxtools.sellauth.com")
     else:
         pass

async def run_bot(token):
    try:
        await bot.start(token)
    except Exception as e:
        print(e)

async def loader():
    resize()
    clear()
    print(Fore.LIGHTMAGENTA_EX + Center.XCenter("loading config..."))
    btk = config["token"]
    await run_bot(btk)
    await main()

def art():
    art = """
           _                   
     /\   | |                  
    /  \  | |__  _   _ ___ ___ 
   / /\ \ | '_ \| | | / __/ __|
  / ____ \| |_) | |_| \__ \__ \\
 /_/    \_\_.__/ \__, |___/___/
                  __/ |        
                 |___/         """
    print(Center.XCenter(Fore.LIGHTMAGENTA_EX + art + "\n"))
    print(Fore.RED + "\n         01 > " + Fore.LIGHTMAGENTA_EX + "create channels" + Fore.RED + "      06 > " + Fore.LIGHTMAGENTA_EX + "rename guild")
    print(Fore.RED + "         02 > " + Fore.LIGHTMAGENTA_EX + "delete channels" + Fore.RED + "      07 > " + Fore.LIGHTMAGENTA_EX + "ban members")
    print(Fore.RED + "         03 > " + Fore.LIGHTMAGENTA_EX + "create roles" + Fore.RED + "         08 > " + Fore.LIGHTMAGENTA_EX + "kick members")
    print(Fore.RED + "         04 > " + Fore.LIGHTMAGENTA_EX + "delete roles" + Fore.RED + "         09 > " + Fore.LIGHTMAGENTA_EX + "mass dm")
    print(Fore.RED + "         05 > " + Fore.LIGHTMAGENTA_EX + "channel spammer\n" + Fore.RESET)

async def main():
    clear()
    title()
    art()
    choice = input(Fore.LIGHTMAGENTA_EX + "                         choice: " + Fore.RED)
    
    if choice == "1" or choice == "01":
        guild = int(input(Fore.LIGHTMAGENTA_EX + Center.XCenter("guild: " + Fore.RED)))
        guild = bot.get_guild(guild)

        cnames = input(Fore.LIGHTMAGENTA_EX + Center.XCenter("name: " + Fore.RED))
        amount = int(input(Fore.LIGHTMAGENTA_EX + Center.XCenter("amount: " + Fore.RED)))    
        c_tasks = []
        for i in range(amount):
            c_task = asyncio.create_task(guild.create_text_channel(name=cnames))
            print(Fore.LIGHTMAGENTA_EX + Center.XCenter("created | " + Fore.RED + cnames))
            c_tasks.append(c_task)
        await asyncio.gather(*c_tasks)
        await asyncio.sleep(2)
        await main()

    elif choice == "2" or choice == "02":
        guild = int(input(Fore.LIGHTMAGENTA_EX + Center.XCenter("guild: " + Fore.RED)))
        guild = bot.get_guild(guild)

        del_c_tasks = []
        for channel in guild.channels:
            del_task = asyncio.create_task(channel.delete())
            print(Fore.LIGHTMAGENTA_EX + Center.XCenter("deleted | " + Fore.RED + channel.name))
            del_c_tasks.append(del_task)
        await asyncio.gather(*del_c_tasks)
        await asyncio.sleep(1)
        await main()
    elif choice == "3" or choice == "03":
        guild = int(input(Fore.LIGHTMAGENTA_EX + Center.XCenter("guild: " + Fore.RED)))
        guild = bot.get_guild(guild)

        roles_name = input(Fore.LIGHTMAGENTA_EX + Center.XCenter("name: " + Fore.RED))
        roles_amount = int(input(Fore.LIGHTMAGENTA_EX + Center.XCenter("amount: " + Fore.RED)))
        roles_tasks = []
        for i in range(roles_amount):
            role_task = asyncio.create_task(guild.create_role(name=roles_name))
            print(Fore.LIGHTMAGENTA_EX + Center.XCenter("created | " + Fore.RED + roles_name))
            roles_tasks.append(role_task)
        await asyncio.gather(*roles_tasks)
        await asyncio.sleep(1)
        await main()
    elif choice == "4" or choice == "04":
        guild = int(input(Fore.LIGHTMAGENTA_EX + Center.XCenter("guild: " + Fore.RED)))
        guild = bot.get_guild(guild)

        del_r_tasks = []
        for role in guild.roles:
            if role.name == "@everyone":
                continue

            role_d_task = asyncio.create_task(role.delete())
            print(Fore.LIGHTMAGENTA_EX + Center.XCenter("deleted | " + Fore.RED + role.name))
            del_r_tasks.append(role_d_task)
        await asyncio.gather(*del_r_tasks)
        await asyncio.sleep(1)
        await main()
    elif choice == "5" or choice == "05":
        guild = int(input(Fore.LIGHTMAGENTA_EX + Center.XCenter("guild: " + Fore.RED)))
        guild = bot.get_guild(guild)

        msg = input(Fore.LIGHTMAGENTA_EX + Center.XCenter("message: " + Fore.RED))

        spammsg_tasks = []

        for channel in guild.channels:
            for i in range(25):
                spammsg_task = asyncio.create_task(channel.send(msg))
                print(Fore.LIGHTMAGENTA_EX + Center.XCenter("sent message | " + Fore.RED + str(channel.id)))
                spammsg_tasks.append(spammsg_task)

        await asyncio.gather(*spammsg_tasks)
        await asyncio.sleep(1)
        await main()
    elif choice == "6" or choice == "06":
        guild = int(input(Fore.LIGHTMAGENTA_EX + Center.XCenter("guild: " + Fore.RED)))
        guild = bot.get_guild(guild)

        newna = input(Fore.LIGHTMAGENTA_EX + Center.XCenter("name: " + Fore.RED))
        r = input(Fore.LIGHTMAGENTA_EX + Center.XCenter("string[y/n]: " + Fore.RED))
        if r.lower() == "y":
            random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
            newname = f"{newna} | [{random_string}]"
            await guild.edit(name=newname)
            print(Fore.LIGHTMAGENTA_EX + Center.XCenter("renamed to | " + Fore.RED + newname))
            await asyncio.sleep(1)
            await main()
        elif r.lower() == "n":
            await guild.edit(name=newna)
            print(Fore.LIGHTMAGENTA_EX + Center.XCenter("renamed to | " + Fore.RED + newna))
            await asyncio.sleep(1)
            await main()
    elif choice == "7" or choice == "07":
        guild = int(input(Fore.LIGHTMAGENTA_EX + Center.XCenter("guild: " + Fore.RED)))
        guild = bot.get_guild(guild)

        ban_reason = input(Fore.LIGHTMAGENTA_EX + Center.XCenter("reason: " + Fore.RED))
        ban_tasks = []
        for member in guild.members:
            ban_task = asyncio.create_task(member.ban(reason=ban_reason))
            print(Fore.LIGHTMAGENTA_EX + Center.XCenter("banned | " + Fore.RED + str(member.id)))
            ban_tasks.append(ban_task)
        await asyncio.gather(*ban_tasks)
        await asyncio.sleep(1)
        await main()

    elif choice == "8" or choice == "08":
        guild = int(input(Fore.LIGHTMAGENTA_EX + Center.XCenter("guild: " + Fore.RED)))
        guild = bot.get_guild(guild)

        kick_reason = input(Fore.LIGHTMAGENTA_EX + Center.XCenter("reason: " + Fore.RED))
        kick_tasks = []
        for member in guild.members:
            kick_task = asyncio.create_task(member.kick(reason=kick_reason))
            print(Fore.LIGHTMAGENTA_EX + Center.XCenter("kicked | " + Fore.RED + str(member.id)))
            kick_tasks.append(kick_task)
        await asyncio.gather(*kick_tasks) 
        await asyncio.sleep(1)
        await main()

    elif choice == "9" or choice == "09":
        guild = int(input(Fore.LIGHTMAGENTA_EX + Center.XCenter("guild: " + Fore.RED)))
        guild = bot.get_guild(guild)
        spam_tasks = []

        msg = input(Fore.LIGHTMAGENTA_EX + Center.XCenter("message: " + Fore.RED))
        for member in guild.members:
            try:
                spam_task = asyncio.create_task(member.send(msg))
                print(Fore.LIGHTMAGENTA_EX + Center.XCenter("dmed | " + Fore.RED + str(member)))
                spam_tasks.append(spam_task)
            except discord.Forbidden:
                print(Fore.RED + Center.XCenter(f"failed to dm user | {member}"))
        await asyncio.gather(*spam_tasks, return_exceptions=True)
        await asyncio.sleep(1)
        await main()

    else:
        await main() 
          
if __name__ == "__main__":
     asyncio.run(loader())
