import nextcord
from nextcord import embeds
from nextcord import player
from nextcord.ext import commands
import json
import random
import os
from nextcord.ext.commands.converter import clean_content
from nextcord.utils import get

os.chdir('D:/Bots/nya')
client= commands.Bot(command_prefix= "n!")

#event--------------------------------------------

@client.event
async def on_ready(message):
    await message.channel.send("good meow-rning what can i do")


@client.event
async def on_disconnect(content):
    await content.channel.send("-_- bleh im ded")


@client.event
async def on_command_error(content, error):
    if isinstance(error, commands.CommandOnCooldown):
        myEmbed = nextcord.Embed(title= "COOLDOWN", color=0xF0AAA6)
        myEmbed.add_field(name='You are still on cooldown so hold ya horses mate', value="Try again after {:.2f}s".format(error.retry_after), inline= False)
        await content.channel.send(embed=myEmbed)



        return





#pics--------------------------------------------------------------
cats = [

    'https://i.pinimg.com/564x/b4/f6/d0/b4f6d00c57d57b217f248f1b89c5c185.jpg',
    'https://i.pinimg.com/564x/34/27/76/342776d326c47ffcd2a4cb320f69cde1.jpg',
    'https://i.pinimg.com/564x/21/0c/f3/210cf3789e18fb7e3af2932df0a09c9d.jpg',
    'https://i.pinimg.com/564x/cf/9f/1d/cf9f1d3b2cc90d3fa86f0a10ff4195f5.jpg',
    'https://i.pinimg.com/564x/e1/5d/2a/e15d2a74cede34b6cd075cfea3ae113c.jpg',
    'https://i.pinimg.com/564x/8d/fa/b3/8dfab3e186750231a53471de00535ae0.jpg',
    'https://i.pinimg.com/564x/59/d9/71/59d9714c3088197ed35b7e83f7391883.jpg',
    'https://i.pinimg.com/564x/21/fb/35/21fb352c8e1d07b3d0a4b31b18ac723a.jpg',
    'https://i.pinimg.com/564x/86/9f/54/869f545de16a500f5769d593eb3008da.jpg',
    'https://i.pinimg.com/564x/3e/3e/5a/3e3e5ae11d27570c747a581a91768650.jpg',
    'https://i.pinimg.com/564x/7d/02/a9/7d02a9db7404ec098668667f1a73ce78.jpg'

]







#help commands--------------------------------------------------------
@client.command(name="cmd")
async def cmd(content, cmds):
    if cmds == "start":
        myEmbed = nextcord.Embed(title= "Start", description= ' ', color=0xF0AAA6)
        myEmbed.add_field(name='Starts the journey to cat spams', value="of cats, for cats, to cats", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`n!start`", inline= False)
        await content.channel.send(embed=myEmbed)
        return

    if cmds == "stop":
        myEmbed = nextcord.Embed(title= "Stop", description= ' ', color=0xF0AAA6)
        myEmbed.add_field(name='Stops the journey to cat spams', value="tis' a shame", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`n!stop`", inline= False)
        await content.channel.send(embed=myEmbed)
        return
    
    if cmds == "cat":
        myEmbed = nextcord.Embed(title= "Start", description= ' ', color=0xF0AAA6)
        myEmbed.add_field(name='Starts the journey to cat spams', value="of cats, for cats, to cats", inline= False)
        myEmbed.add_field(name='Use for this cmd:', value="`n!`", inline= False)
        await content.channel.send(embed=myEmbed)
        return



#commands-------------------------------------------------------

@client.command(name="aid")
async def aid(content):
    myEmbed = nextcord.Embed(title='Helping your brain here :cat: ', description='all commands', color= 0xAC5436)
    myEmbed.add_field(name='Journey', value='start, stop', inline= False)
    myEmbed.add_field(name='Random Spams', value='cat, daily', inline= False)
    await content.channel.send(embed=myEmbed)


#intro
@client.command(name='intro')
async def intro(content):
    myEmbed = nextcord.Embed(title='INTRO', color= 0x56CCD5)
    myEmbed.add_field(name='Im Meow made on 15th June 2022 using Visual Studio Code IDE with the language Python ver. 3.9.13', value=' :cat: ', inline= False)
    myEmbed.add_field(name='By Ahana, Aleena and Christine ', value= 'for python BCA project', inline = False)
    await content.channel.send(embed=myEmbed)


#ping
@client.command(name= "bing")
async def ping(content, arg = None):
    if arg == "bong":
        await content.channel.send("🏓 Marvelous u bonged yourself-")
    else:
        await content.channel.send(f"🏓 bong {round(client.latency * 1000)}ms")


#cat pic
@client.command(name = "cat")
async def cat(content):
    em = nextcord.Embed(title= "There u nya", color= content.member.role_color)
    em.set_image(url = random.choice(cats))
    await content.channel.send (embed =em)
    return

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
async def ttt(content, p1: nextcord.Member, p2: nextcord.Member):
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
                    myEmbed = nextcord.Embed(title= "WE HAVE A WINNERRRRRRR!!! :tada:", color = 0xD7A998)
                    myEmbed.add_field(name= "so this round's winner is:", value= mark)
                    await content.channel.send (embed = myEmbed)
                


                elif count >= 9:
                    myEmbed = nextcord.Embed(title= "WE HAVE A WINNERRRRRRR!!!", color = 0xD7A998)
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






#status--------------------------------------------------------

@client.event
async def on_ready():
    await client.change_presence(status=nextcord.Status.online, activity=nextcord.Game("with a yarn ball~"))





#token---------------------------------------------------------

client.run("TOken")

