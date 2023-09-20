import discord
from discord.ext import tasks, commands
from random import choice
import os 
import DiscordUtils

os.chdir('/Users/ahanakaur/Desktop/Bots/RPS')
client= commands.Bot(command_prefix= "+")

def is_it_me(content):
    return content.author.id == 747361529896239134


#variables======================================================

status = ["~help", "Help to let loners feel less lonely"]




#event==========================================================


@client.event
async def on_ready():
    change_status.start()
    print ('bot online')


@client.event
async def on_disconnect(ctx):
    await ctx.channel.send("-_- bleh im ded")



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        myEmbed = discord.Embed(title= "COOLDOWN", color=0xF0AAA6)
        myEmbed.add_field(name='You are still on cooldown so hold ya horses mate', value="Try again after {:.2f}s".format(error.retry_after), inline= False)
        await ctx.channel.send(embed=myEmbed)



#aid==========================================================
@client.command(name="aid", help="the actual help of the bot ok use this")
async def aid(ctx):
    myEmbed = discord.Embed(title='Helping your brain here', description='ALL COMMANDS', color= ctx.author.color)
    myEmbed.add_field(name='Ping', value='`~ping` - it send the speed of the bot :zap:', inline= False)
    myEmbed.add_field(name='Yo', value='`~yo` - tht time i wanted to check if it actually even responds or not- (owner restricted)', inline= False)
    myEmbed.add_field(name='Playing', value='', inline= False)
    myEmbed.add_field(name='Rock', value='`~rock` or `~r` - to play rock', inline= False)
    myEmbed.add_field(name='Paper', value='`~paper` or `~p` - to play paper', inline= False)
    myEmbed.add_field(name='Scissors', value='`~scissors` or `~s` - to play scissors', inline= False)
    await ctx.channel.send(embed=myEmbed)


    
#ping==========================================================
@client.command(name= "ping", help="checks latency/speed bonking u in ur brain")
async def ping(ctx, arg = None):
    if arg == "pong":
        await ctx.channel.send("🏓 Marvelous u bonked yourself-")
    else:
        await ctx.channel.send(f"🏓 Bonk {round(client.latency * 1000)}ms")



#checking---------------------------------
@client.command(name= "yo")
async def yo(ctx):
    await ctx.channel.send('OOF')



#perms----------------------
@client.command(name = "perms")
@commands.check(is_it_me)
async def perms(content):
    em = discord.Embed(title= "Permissions asked", color= content.author.color)
    em.add_field(name= "By default", value= 'change nickname, read msgs, send msgs, send TTS msgs, embed links, add reaction, attach files, read msg history, use external emoji, use external stickers', inline= False)
    await content.channel.send(embed= em)
    return



#invite--------------------------
@client.command(name='invite')
async def invite(content):
    myEmbed = discord.Embed(title= "Invite Link", color=0xF0AAA6)
    myEmbed.add_field(name='Here is the invite: ', value="https://discord.com/api/oauth2/authorize?client_id=959727213744386158&permissions=137506446400&scope=bot", inline= False)
    myEmbed.set_footer(text='your welcome and thanks 👀')
    myEmbed.set_author(name= 'AnnaNutzz#6682', icon_url='https://i.pinimg.com/564x/42/cb/a7/42cba7cdd9447cb77289e575bfe14216.jpg')
    myEmbed.set_thumbnail(url= client.user.avatar_url)
    await content.channel.send(embed=myEmbed)
    return



#avatar----------------------------
@client.command(name='av')
async def av(content, member: discord.Member = None):
    member = content.author if not member else member
    myEmbed = discord.Embed(title= "Avatar ", color=0x000000)
    myEmbed.set_image(url = member.avatar_url)
    myEmbed.set_footer(text= member.name + "'s avatar 〜(꒪꒳꒪)〜")
    await content.channel.send(embed=myEmbed)
    return



#whois-----------------------------
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



#bot plays=======================================================

rock= 

[ 
      myEmbed = discord.Embed(title= "  ", color= content.author.color)
    myEmbed.add_field(name='  ', value="  ", inline= False)
    await content.channel.send(embed=myEmbed)
    return
   ]




#commands=======================================================


@client.command(name= "rock", aliases= ['r', 'ROCK', 'R'])
async def rock(content, member: discord.Member = None):
    await content.channel.send(random.choice(zx))
    return










#status==========================================================


@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(choice(status)))



#token==========================================================

client.run("OTU5NzI3MjEzNzQ0Mzg2MTU4.YkgFng.GoRMkyO336BZtaO6Y9t67rOJJPk")
