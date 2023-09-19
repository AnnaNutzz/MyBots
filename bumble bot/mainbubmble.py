import discord
from discord import embeds
from discord import player
from discord.ext import commands
import json
import random
import os
#from discord.ext.commands.converter import clean_content
#from discord.utils import get

os.chdir('/Users/ahanakaur/Desktop/Bots/Bumble Bot')
client= commands.Bot(command_prefix= "?")


#variables---------------------------------------




#event--------------------------------------------

@client.event
async def on_ready(message):
    await message.channel.send("yo im on")


@client.event
async def on_disconnect(content):
    await content.channel.send("-_- bleh im ded")


@client.event
async def on_command_error(content, error):
    if isinstance(error, commands.CommandOnCooldown):
        myEmbed = discord.Embed(title= "COOLDOWN", color=0xF0AAA6)
        myEmbed.add_field(name='You are still on cooldown so hold ya horses mate', value="Try again after {:.2f}s".format(error.retry_after), inline= False)
        await content.channel.send(embed=myEmbed)




#lockdown----------------------------------------------------------

#lockdown
@client.command(name="lockdown")
@commands.has_permissions(manage_channels = True)
async def lockdown(content):
    await content.channel.set_permissions(content.guild.default_role, send_messages = False)
    await content.channel.send(content.channel.mention + " is now on lockdown.")


#unlock
@client.command(name="unlock")
@commands.has_permissions(manage_channels = True)
async def unlock(content):
    await content.channel.set_permissions(content.guild.default_role, send_messages = True)
    await content.channel.send(content.channel.mention + " is now on unlocked.")





#help commands--------------------------------------------------------
@client.command(name="cmd")
async def cmd(content, cmds):
    if cmds == "bal":
        myEmbed = discord.Embed(title= "Balance", description= 'the way to your wallet 😌 not your heart but if money is your love then yes', color=0xF0AAA6)
        myEmbed.add_field(name='Opens your balance... nothing more okay?', value="The currency is called Bums ❖", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?bal`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "pbal":
        myEmbed = discord.Embed(title= "Panty Balance", description= 'the way to your panty collection', color=0x4781F8)
        myEmbed.add_field(name='Opens your balance of panties', value="Lewd", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?pbal`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "beg":
        myEmbed = discord.Embed(title= "Begging", description= 'a way to earn your money lazy way~', color=0xA942D9)
        myEmbed.add_field(name='You beg, You get money, easy peasy lemon squeazy', value="You might get lucky and get the highest amount", inline =False)
        myEmbed.add_field(name='Use for this cmd:', value="`?beg`", inline =False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "withd":
        myEmbed = discord.Embed(title= "Withdraw", color=0x6C6DE3)
        myEmbed.add_field(name='You can withdraw money from your bank', value="Not other's bank ok?", inline= False)
        myEmbed.add_field(name="Use for this cmd:", value="`?withd <amount>`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "dep":
        myEmbed = discord.Embed(title= "Deposit", color=0x716BD3)
        myEmbed.add_field(name='You need money to in bank for safe keeping', value="You cant withdraw without an empty bank right?", inline= False)
        myEmbed.add_field(name='Use for depositing your amount:',  value="`?dep <amount>`",inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "share":
        myEmbed = discord.Embed(title= "Sharing", description= 'when sharing is caring', color=0x5485D8)
        myEmbed.add_field(name='You can send some money as a gift to anyone in their bank from your bank', value="not other's bank ok", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?share @<the user you want to send> <amount>`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "intro":
        myEmbed = discord.Embed(title= "Introductions", description= 'introductions first, dont be rude', color=0x1EBFBA)
        myEmbed.add_field(name='Just a introductions of me and my creator', value="everything you NEED to know", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?intro`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "stitch":
        myEmbed = discord.Embed(title= "Stitching", color=0xA7CC52)
        myEmbed.add_field(name="A way to stitch panties and later steal other's and sell for a good amount", value="at request", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?stitch`", inline= False)
        await content.channel.send(embed=myEmbed)
        return
        
    if cmds == "sac":
        myEmbed = discord.Embed(title= "Sacrifice", color=0x37FA76)
        myEmbed.add_field(name="All panties need a sacrifice", value=" You can sacrifice panties to the bot owner for getting Bums", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?sac <amount>`", inline= False)
        await content.channel.send(embed=myEmbed)
        return
        
    if cmds == "stealp":
        myEmbed = discord.Embed(title= "Stealing Panties", color=0xBDEDEC)
        myEmbed.add_field(name="Well if you can sell panties to the bot owner you can steal and sell more!", value="Lewd Thief", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?stealp <user>`", inline= False)
        await content.channel.send(embed=myEmbed)
        return
        
    if cmds == "steal":
        myEmbed = discord.Embed(title= "Stealing", color=0x673FF6)
        myEmbed.add_field(name="Well be robbers if your broke ¯\_(ツ)_/¯", value="Thief tsk tsk tsk", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?steal <user>`", inline= False)
        await content.channel.send(embed=myEmbed)
        return
        
    if cmds == "buy":
        myEmbed = discord.Embed(title= "Buying", color=0xB39DE0)
        myEmbed.add_field(name="You can buy stuff from the shop", value="I mean- this is self explaintory", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?buy <itemname> <amount>`", inline= False)
        await content.channel.send(embed=myEmbed)
        return
        
    if cmds == "shop":
        myEmbed = discord.Embed(title= "Shop", color=0x76E38E)
        myEmbed.add_field(name="Opens up a shop menu which isnt that wide ranged rn", value="Well we do need things to powerup or keep safe", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?shop`", inline= False)
        await content.channel.send(embed=myEmbed)
        return
        
    if cmds == "inv":
        myEmbed = discord.Embed(title= "Inventory", color=0xC1E982)
        myEmbed.add_field(name="Opens up a way to your inventory", value="Its unlimited unlike Minecraft until you use Shulker Boxes", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?inv`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "sell":
        myEmbed = discord.Embed(title= "Selling", color=0x7948FA)
        myEmbed.add_field(name="Well some things are a hassale to keep", value="Why not sell and rather earn money", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?sell <itemname> <amount>`", inline= False)
        await content.channel.send(embed=myEmbed)
        return
    
    if cmds == "daily":
        myEmbed = discord.Embed(title= "Daily earnings", color=0xC9C7F2)
        myEmbed.add_field(name="Well who doesnt like free money? ", value="Earn 20k Bums daily", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?daily`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "lb":
        myEmbed = discord.Embed(title= "Leaderboards", color=0xA88830)
        myEmbed.add_field(name="Which currency bot doesnt have leaderboards?", value="Certainly not this one *oh goodness me* :eyes:", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?lb`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "lockdown":
        myEmbed = discord.Embed(title= "Lockdown", color=0x9C89A7)
        myEmbed.add_field(name="Disables the permission for everyone to not send messages", value="its a quick command", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?lockdown`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "unlock":
        myEmbed = discord.Embed(title= "Unlocking", color=0x6BEBD6)
        myEmbed.add_field(name="Its unlocks the Lockdown procedure", value="well you cnt keep a channel on lockdown always", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?unlock`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "invite":
        myEmbed = discord.Embed(title= "Inviting Me", color=0xB2B99C)
        myEmbed.add_field(name="I know im not that great", value="but if you want me in another server use this command", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?invite`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "av":
        myEmbed = discord.Embed(title= "Avatar", color=0x9BF080)
        myEmbed.add_field(name="Well to see the avatar's of users", value="in big picture", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?av <user>`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "ttt":
        myEmbed = discord.Embed(title= "TicTacToe", color=0x9BF080)
        myEmbed.add_field(name="Wanna earn some free money", value="play tictactoe (both players get same amount)", inline= False)
        myEmbed.add_field(name="To place your knot or cross use cmd:", value="`?put <the number of postion from 1 to 9>`", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?ttt <yourself> <another user>`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "whois":
        myEmbed = discord.Embed(title= "Who is this mannnn *or woman*", color=0x9BF080)
        myEmbed.add_field(name="Wanna know about some user", value="You came to the right place", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`?whois <user>`", inline= False)
        await content.channel.send(embed=myEmbed)
        return



#commands-------------------------------------------------------

@client.command(name="aid")
async def aid(content):
    myEmbed = discord.Embed(title='Helping your brain here <a:twerk:831598005710618684>', description='all commands', color= 0xAC5436)
    myEmbed.add_field(name='Miscellaneous', value='intro, lb, invite', inline= False)
    myEmbed.add_field(name='Currency', value='bal, beg, withd, dep, share, steal, daily', inline= False)
    myEmbed.add_field(name='Shop', value='shop, sell, buy, inv', inline= False)
    myEmbed.add_field(name='Panties', value='pbal, stitch, sac, stealp', inline= False)
    myEmbed.add_field(name='Fun', value='av, ttt, whois', inline= False)
    myEmbed.add_field(name='Moderation', value='lockdown, unlock', inline= False)
    myEmbed.set_footer(text='if you need more help then use ?cmd <cmd name>')
    await content.channel.send(embed=myEmbed)
#    myEmbed.set_author(name= 'Bumble#2302', icon_url='https://imgur.com/233c2fbb-e5b3-48c4-b018-b8e6c756ac46')



#intro
@client.command(name='intro')
async def intro(content):
    myEmbed = discord.Embed(title='INTRO', color= 0x56CCD5)
    myEmbed.add_field(name='Im Bumble made by AnnaNutzz#6682 on 20th June 2021 using Visual Studio Code IDE with the language Python ver. 3.9.5', value=' 🙈 ', inline= False)
    myEmbed.add_field(name='Bots made by her:', value= 'Quak, Bumble Bot', inline = False)
    myEmbed.set_footer(text='(she doesnt like python that much)')
    myEmbed.set_author(name= 'AnnaNutzz#6682', icon_url='https://i.pinimg.com/564x/42/cb/a7/42cba7cdd9447cb77289e575bfe14216.jpg')
    await content.channel.send(embed=myEmbed)



#invite
@client.command(name='invite')
async def invite(content):
    myEmbed = discord.Embed(title= "Invite Link", color=0xF0AAA6)
    myEmbed.add_field(name='Here is the invite: ', value="https://discord.com/oauth2/authorize?client_id=856070316001329153&scope=bot&permissions=1946680443", inline= False)
    myEmbed.set_footer(text='your welcome and thanks 👀')
    myEmbed.set_author(name= 'AnnaNutzz#6682', icon_url='https://i.pinimg.com/564x/42/cb/a7/42cba7cdd9447cb77289e575bfe14216.jpg')
    myEmbed.set_thumbnail(url= client.user.avatar_url)
    await content.channel.send(embed=myEmbed)
    return



#avatar
@client.command(name='av')
async def av(content, member: discord.Member = None):
    member = content.author if not member else member
    myEmbed = discord.Embed(title= "Avatar ", color=0x000000)
    myEmbed.set_image(url = member.avatar_url)
    myEmbed.set_footer(text= member.name + "'s avatar 〜(꒪꒳꒪)〜")
    await content.channel.send(embed=myEmbed)
    return



#whois
@client.command(name='whois')
async def whois(content, member: discord.Member = None):
    member = content.author if not member else member
    myEmbed = discord.Embed(title= member.display_name, color= member.color)
    myEmbed.add_field(name= "ID", value=member.id, inline= False)
    myEmbed.add_field(name= "Is this a bot?", value=member.bot, inline= False)
    myEmbed.add_field(name= "When account created?", value=member.created_at, inline= False)
    myEmbed.set_thumbnail(url= member.avatar_url)
    myEmbed.set_footer(text= member.name + "'s info 〜(꒪꒳꒪)〜")
    await content.channel.send(embed=myEmbed)
    return



#ping
@client.command(name= "ping")
async def ping(content, arg = None):
    if arg == "pong":
        await content.channel.send("🏓 Marvelous u ponged yourself-")
    else:
        await content.channel.send(f"🏓 Pong {round(client.latency * 1000)}ms")



#balance
@client.command(name='bal')
async def bal(content, member: discord.Member = None):
    member = content.author if not member else member
    await open_account(member)
    user = member
    
    users = await get_bank_data()
    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title=f"{member.name}'s balance", color= 0x4B4D8B)
    em.add_field(name= "Bums Wallet", value = wallet_amt )
    em.add_field(name= "Bums Bank", value = bank_amt )
    await content.channel.send(embed = em)



#daily
@client.command(name='daily')
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(content):
    await open_account(content.author)
    user = content.author
    
    users = await get_bank_data()
    users[str(user.id)]["wallet"] += 2000
    with open("masterbank.json", "w") as f:
        json.dump(users,f)


    em = discord.Embed(title="Daily", color= 0x4B4D8B)
    em.add_field(name= "Here is your daily amount", value = "❖ 2,000 Bums" )
    em.add_field(name= "Come back 24 hours later", value = "to collect another ❖2k Bums")
    await content.channel.send(embed = em)





#leaderboards----------------------------------------


#leaderboard
@client.command(name='lb')
async def lb(content, x = 3):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amt = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amt] = name 
        total.append(total_amt)

    total = sorted(total,reverse=True)
    em = discord.Embed(title = f"TOP {x} RICHEST PEOPLE", description= "calculated by your wallet and bank", color = 0x4DE649)
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}.{name}", value = f"{amt}", inline= False)
        if index == x:
            break
        else:
            index += 1

    await content.channel.send(embed = em)





#earn---------------------------------------------------


#beg
@client.command(name='beg')
@commands.cooldown(1, 20, commands.BucketType.user)
async def beg(content):
    await open_account(content.author)
    user = content.author

    users = await get_bank_data()
    earnings = random.randrange(0, 501)
    earn= (f"Someone gave you ❖{earnings} Bums T^T", f"You found ❖{earnings} on the floor 〜(꒪꒳꒪)〜", f"Sounds like a bad day you got nothing")

    await content.channel.send(random.choice(earn))
    
    users[str(user.id)]["wallet"] += earnings
    with open("masterbank.json", "w") as f:
        json.dump(users,f)





# opening accounts======================================================================
async def open_account(user):
   users = await get_bank_data()
  
   if str(user.id) in users:
       return False
   else:
       users[str(user.id)] = {}
       users[str(user.id)]["wallet"] = 0
       users[str(user.id)]["bank"] = 0
 
   with open("masterbank.json", "w") as f:
       json.dump(users,f)
   return True
 
async def update_bank(user,change = 0, mode = 'wallet'):
   users = await get_bank_data()
  
   users[str(user.id)][mode] += change
 
   with open("masterbank.json", "w") as f:
       json.dump(users,f)
  
   bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
   return bal

async def get_bank_data():
   with open("masterbank.json", "r") as f:
       users = json.load(f)
  
   return users
# opening accounts======================================================================





#bank------------------------------------------------------



#withdraw
@client.command(name= "withd")
async def withd(content, amount = None):
    await open_account(content.author)
    if amount == None:
        await content.channel.send("I can't add air to your Wallet right? Or can I?")
        return
    bal = await update_bank(content.author)

    amount = int(amount)
    if amount > bal [1]:
        await content.channel.send("Ahhh you're broke, check your balance")
        return
    if amount<0:
        await content.channel.send("Ah yes dont make your money's personality negative like your's")
        return

    await update_bank(content.author, amount)
    await update_bank(content.author, -1*amount, "bank")

    await content.channel.send(f"You withdrew ❖ {amount} Bums!")

    

#deposit
@client.command(name= "dep")
async def dep(content, amount = None):
    await open_account(content.author)
    if amount == None:
        await content.channel.send("I can't add air to your Wallet right? Or can I?")
        return
    bal = await update_bank(content.author)

    amount = int(amount)
    if amount > bal [0]:
        await content.channel.send("Ahhh you're broke, check your balance")
        return
    if amount<0:
        await content.channel.send("Ah yes dont make your money's personality negative like your's")
        return

    await update_bank(content.author, -1*amount)
    await update_bank(content.author, amount, "bank")

    await content.channel.send(f"You deposited ❖ {amount} Bums!")



#share
@client.command(name= "share")
async def share(content, member: discord.Member, amount = None):
    await open_account(content.author)
    await open_account(member)
    if amount == None:
        await content.channel.send("I can't add air to your Wallet right? Or can I?")
        return

    bal = await update_bank(content.author)
    amount = int(amount)
    if amount > bal [1]:
        await content.channel.send("Ahhh you're broke, check your balance")
        return
    if amount<0:
        await content.channel.send("Ah yes dont make your money's personality negative like your's")
        return

    await update_bank(content.author, -1*amount, "bank")
    await update_bank(member, amount, "bank")

    await content.channel.send(f"You gave ❖ {amount} Bums!")



#steal
@client.command(name= "steal")
@commands.cooldown(5, 60, commands.BucketType.user)
async def steal(content, victim: discord.Member = None):
    con = content.author
    await open_account(con)
    await open_account(victim)  
    
    data = await get_bank_data()

    if victim == None:
        return await content.channel.send("You stole from yourself and gave back to yourself too... PING SOMEONE")
    
    if data[str(victim.id)]["wallet"] < 100:
        return await content.channel.send("They broke, You broke, #brokegang")

    coninv = data[str(con.id)]["inv"]
    vicinv = data[str(victim.id)]["inv"]   

    lilrob = random.randrange (0, bal[100])
    fullrob = data[str(victim.id)]["wallet"]
    rob = random.choice(lilrob, fullrob)

    if 'Lock' in vicinv:
        if "Cutter" in coninv:
            myEmbed = discord.Embed(title= "Wow Just Made It", color= content.author.color)
            myEmbed.add_field(name='They had a lock but you can cut through it with your bolt cutters', value=f"You stole ❖{rob} Bums :money_mouth:", inline= False)
            await content.channel.send(embed=myEmbed)
            
            await update_bank(content.author, rob, "wallet")
            await update_bank(victim, -1*rob, "wallet")
            
            return 
        else:
            myEmbed = discord.Embed(title= "Tried Never The Less", color= content.author.color)
            myEmbed.add_field(name='They had a lock and you couldnt get in :lock:', value= "Try buying a cutter", inline= False)
            await content.channel.send(embed=myEmbed)
            return 
    else:
        myEmbed = discord.Embed(title= "Easy Peasy", color= content.author.color)
        myEmbed.add_field(name='They had no lock, its free real estate :sparkle:', value=f"You stole ❖{rob} Bums :money_mouth:", inline= False)
        await content.channel.send(embed=myEmbed)
        
        await update_bank(content.author, rob, "wallet")
        await update_bank(victim, -1*rob, "wallet")
        
        return 



#shop variables---------------------------------------------------

mainshop = [{"emoji": ":shirt: ","name": "Wardrobe", "price": 10000, "description": "Keeps your panties safe"},
            {"emoji": ":lock: ","name": "Lock", "price": 15000, "description": "Keeps your Bank safe"},    
            {"emoji": ":pd_boltcutters: ","name": "Cutter", "price": 25000, "description": "Helps you keep other's Banks unsafe"}, 
            {"emoji": ":red_car: ","name": "Car", "price": 1000000000000, "description": "Turns you into a Bumblebee"}]
  


#shop--------------------------------------------------------------


#opening shop
@client.command(name="shop")
async def shop(content):
    em = discord.Embed(title= "Shop")

    for item in mainshop:
        emoji = item["emoji"]
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = emoji + name, value = f"❖{price} Bums | {desc}", inline = False)

    await content.channel.send(embed = em)



#inv
@client.command(name= "inv")
async def inv(content, user: discord.Member = None):
    if user is None:
        user = content.author
    await open_account(user)

    data = await get_bank_data()

    inv = data[str(user.id)].get(key="inv", default=[])

    em = discord.Embed(title = "INVENTORY", color = 0x8E62B5)
    for item in inv:
        name = item["item"]
        amount = item["amount"]
        em.add_field(name = name, value = amount)
    await content.channel.send(embed = em)

#inv
@client.command(name= "inv")
async def inv(content, member: discord.Member = None):
    member = content.author if not member else member
    await open_account(member)
    user = member
    users = await get_bank_data()
    try:
        inv = users[str(user.id)]["inv"]
    except:
        inv = []
    em = discord.Embed(title = "INVENTORY", color = 0x8E62B5)
    for item in inv:
        name = item["item"]
        amount = item["amount"]
        em.add_field(name = name, value = amount)
    await content.channel.send(embed = em)

#buy
@client.command(name="buy")
async def buy(content, item, amount = 1):
    await open_account(content.author)

    res = await buy_this(content.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await content.channel.send("Nah we dont have it here.")
            return
        if res[1]==2:
            await content.channel.send(f"Your broke :clown: earn some or steal some to buy this")
            return

    await content.channel.send(f"You just bought {amount} {item}, use well~")


async def buy_this(user, item_name, amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]
    
    cost = price*amount
    users = await get_bank_data()
    bal = await update_bank(user)
    
    if bal[0]<cost:
        return [False,2]
    
    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["inv"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["inv"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            obj = {"item": item_name, "amount": amount}
            users[str(user.id)]["inv"].append(obj)
    except:
        obj = {"item": item_name, "amount": amount}
        users[str(user.id)]["inv"] = [obj]

    with open("masterbank.json", "w") as f:
        json.dump(users,f)

    await update_bank(user, cost*-1, "wallet")

    return [True,"Worked"]



#sell
@client.command(name="sell")
async def sell(content, item, amount = 1):
    await open_account(content.author)

    res = await sell_this(content.author,item,amount)

     
    if not res[0]:
        if res[1]==1:
            await content.channel.send("Nah we dont have it here.")
            return
        if res[1]==2:
            await content.channel.send(f"You dont have {amount} {item} in your inventory :clown:")
            return
        if res[1]==3:
            await content.channel.send(f"You dont have item in your inventory :clown:")
            

    await content.channel.send(f"You sold {amount} {item}, use the money well~")


async def sell_this(user, item_name, amount, price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price == None:
                price = 0.9*item["price"]
            break

    if name_ == None:
        return [False,1]
    
    cost = price*amount
    users = await get_bank_data()
    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]
    
    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["inv"]:
            n = thing ["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return[False,2]
                users[str(user.id)]["inv"][index]["amount"] = new_amt
                t = 1
                break
            index += 1
        if t == None:
            return [False, 3]
    except:
        return [False, 3]

    with open("masterbank.json", "w") as f:
        json.dump(users,f)
    

    await update_bank(user, cost, "wallet")

    return [True,"Worked"]





#panty--------------------------------------------------------------


#pantybal
@client.command(name='pbal')
async def pbal(content, member: discord.Member = None):
    member = content.author if not member else member
    await open_paccount(member)
    user = member
    
    users = await get_panty_data()
    panty_amt= users[str(user.id)]["panties"]

    em = discord.Embed(title=f"{member.name}'s panty balance", color= 0x4B4D8B)
    em.add_field(name= "Panties", value = panty_amt)
    await content.channel.send(embed = em)



#stitch
@client.command(name='stitch')
@commands.cooldown(1, 20, commands.BucketType.user)
async def stitch(content):
    await open_paccount(content.author)
    user = content.author
    
    users = await get_panty_data()
    panties = random.randrange(0, 51)
    await content.channel.send(f"You stitched {panties} panties... lewd ///UwU///")
    
    users[str(user.id)]["panties"] += panties
    with open("mainpanty.json", "w") as f:
        json.dump(users,f)



async def open_paccount(user):
   users = await get_panty_data()
  
   if str(user.id) in users:
       return False
   else:
       users[str(user.id)] = {}
       users[str(user.id)]["panties"] = 0
 
   with open("masterpanty.json", "w") as f:
       json.dump(users,f)
   return True
 
 
async def update_panty(user,change = 0, mode = 'panties'):
   users = await get_panty_data()
  
   users[str(user.id)][mode] += change
 
   with open("masterpanty.json", "w") as f:
       json.dump(users,f)
  
   bal = [users[str(user.id)]["panties"]]
   return bal


async def get_panty_data():
   with open("masterpanty.json", "r") as f:
       users = json.load(f)
  
   return users



#sac
@client.command(name= "sac")
async def sac(content, panty = None):
    await open_paccount(content.author)
    if panty == None:
        await content.channel.send("I can't sell air to the onwer right? Or can I?")
        return
    panties = await update_panty(content.author)

    panty = int(panty)
    if panty > panties [1]:
        await content.channel.send("Ahhh you didnt stitch or steal")
        return
    if panty<0:
        await content.channel.send("Ah yes dont make your panty's personality negative like your's")
        return
    
    if panty<50:
        pmon = random.randrange(90,101)
    if panty<100:
        pmon = random.randrange(400,501)
    if panty<500:
        pmon = random.randrange(900,1001)
    if panty<1000:
        pmon = random.randrange(4000,5001)
    if panty<5000:
        pmon = random.randrange(900,10001)
    if panty<10000:
        pmon = random.randrange(4000,50001)
    if panty<50000:
        pmon = random.randrange(9000,100001)
    if panty<100000:
        pmon = random.randrange(4000,500001)
    if panty<500000:
        pmon = random.randrange(90000,1000001)
    if panty<1000000:
        pmon = random.randrange(40000,5000001)
    if panty<5000000:
        pmon = random.randrange(900000,10000001)
    if panty<10000000:
        pmon = random.randrange(400000,50000001)
    if panty<50000000:
        pmon = random.randrange(9000000,100000001)


    await update_panty(content.author, -1*panty, "panties")
    await update_bank(content.author, pmon, "bank")

    await content.channel.send(f"You sacrificed {panty} panties to the owner and gained ❖{pmon} Bums!!")


#stealp
@client.command(name= "stealp")
@commands.cooldown(10, 120, commands.BucketType.user)
async def stealp(content, member: discord.Member):
    await open_paccount(content.author)
    await open_paccount(member)
    
    pbal = await update_panty(member)
    if pbal[0]<100:
        await content.channel.send("They broke, You broke, #brokegang")
        return
    
    probbed = random.randrange (0, pbal[0])

    await update_panty(content.author, probbed, "panties")
    await update_panty(member, -1*probbed, "panties")

    await content.channel.send(f"You stole {probbed} panties from {member}! I will keep my mouth zipped~")






#tictactoe-------------------------------------------------

#variables

player1 = ""
player2 = ""
turn = ""
gameover = True

board = []



#wins

wins = [

[0, 1, 2],
[3, 4, 5],
[6, 7, 8],
[0, 4, 8],
[2, 4, 6],
[0, 3, 6],
[1, 4, 7],
[2, 5, 8],

]


@client.command(name= "ttt")
async def ttt(content, p1: discord.Member, p2: discord.Member):
    global player1
    global player2
    global turn
    global gameover
    global count

    if gameover:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]

        turn =""
        gameover = False
        count = 0

        player1 = p1
        player2 = p2


    #board

        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x ==8:
                line += " " + board[x]
                await content.channel.send(line)
                line = ""
            else:
                line += " " + board[x]

    #players

        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await content.channel.send(" Its <@" + str(player1.id) + ">'s turn so let the match begin")
        elif num == 2:
            turn = player2
            await content.channel.send(" Its <@" + str(player2.id) + ">'s turn so let the match begin")

    else:
       await content.channel.send("At least finish the last pending game")



#playing

@client.command(name= "put")
async def put(content, pos: int):
    global turn 
    global player1
    global player2
    global board
    global count

    if not gameover:
        mark = ""
        if turn == content.author:
            if turn == player1:
                mark = ":x:"
            elif turn == player2:
                mark = ":o:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1

                #board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x ==8:
                        line += " " + board[x]
                        await content.channel.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkwinner(wins, mark)
                if gameover:
                    myEmbed = discord.Embed(title= "WE HAVE A WINNERRRRRRR!!! :tada:", color = 0xD7A998)
                    myEmbed.add_field(name= "so this round's winner is:", value= mark)
                    myEmbed.add_field(name= "But you both will recieve:", value= "❖300 Bums! 〜(꒪꒳꒪)〜")
                    await content.channel.send (embed = myEmbed)
                    win = 300
                    await update_bank(player1, win, "wallet")
                    await update_bank(player2, win, "wallet")


                elif count >= 9:
                    myEmbed = discord.Embed(title= "WE HAVE A WINNERRRRRRR!!!", color = 0xD7A998)
                    myEmbed.add_field(name= "so this round's winner is:", value= "No one because its a tie!")
                    await content.channel.send (embed = myEmbed)


                #turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1


            else:
                 await content.channel.send("put you knot or cross on a valid position!")
        else:
             await content.channel.send("Hold your horses, it aint your turn")
    else:
        await content.channel.send("At least start a game with the command `=ttt`")



#winner

def checkwinner(wins, mark):
    global gameover
    for condition in wins:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameover = True



#errors

@ttt.error
async def tictactoe_error(content, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await content.channel.send("Mention someone, you can't play on your own can you now? ;-;")
    elif isinstance(error, commands.BadArgument):
        await content.channel.send("Mention someone, you can't play on your own can you now? ;-;")


@put.error
async def put_error(content, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await content.channel.send("Mention a position to put")
    elif isinstance(error, commands.BadArgument):
        await content.channel.send("Mention integers")





#coinflip------------------------------------------------------


@client.command(name = "cf")
@commands.cooldown(1, 20, commands.BucketType.user)
async def cf(content, side):
    em = discord.Embed(title=f"You chose {side}", color= 0x4B4D8B)
    em.set_image(url="https://upload.wikimedia.org/wikipedia/commons/f/f8/Stylized_uwu_emoticon.svg")
    win= 400
    lose= -400
    
    won=   [em.add_field(name= f'You got {side}!', value=":tada: Congratulations"),
            await update_bank(content.author, win, "wallet")]

    lost=  [em.add_field(name= f'You got {side}!', value=':pensive: sorry'),
            await update_bank(content.author, lose, "wallet")]

    cfaction = random.choice(won, lost)

    if side == "t" or side == 'h' :
        em.add_field(cfaction)
        await content.channel.send (embed =em)
        





#status--------------------------------------------------------

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Minecraft with Anna | helping your soul with =aid"))





#token---------------------------------------------------------

client.run("ODU2MDcwMzE2MDAxMzI5MTUz.YM7rnA.-6_vNgZ2owadLbt2ClVAQZSqccw")


#currency symbol : ❖ ◎ 
