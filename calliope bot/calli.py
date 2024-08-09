import discord
from discord.ext import tasks, commands
from random import choice
import os 
import DiscordUtils
#from discord_slash import SlashCommand



os.chdir('/Users/ahanakaur/Desktop/Bots/Calliope')
client= commands.Bot(command_prefix= "~")


def is_it_me(content):
    return content.author.id == 747361529896239134



#variables======================================================

status = ["~help", "Help to let loners feel less lonely", "Levi loner boner", "I sing better than Rii", "Nicki accidentally sent hentai bcuz she horny god", "Jazz being drop dead gorgeous!!", "Ace stop twerking", "Teddy lookin fine!!","Jazz got Talont","Jazz accidently kicks people"]

music = DiscordUtils.Music()

#slash = SlashCommand(client, sync_commands=True)


#event==========================================================


@client.event
async def on_ready():
    change_status.start()
    print ('bot online')


@client.event
async def on_disconnect(ctx):
    await ctx.channel.send("-_- bleh im ded")



'''@slash.slash(name="prefix", description="Reminds u of the prefix")
async def prefix(ctx):    
    await ctx.send("The prefix is `~`")'''



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
    myEmbed.add_field(name='Yo', value='`~yo` - tht time i wanted to check if it actually even responds or not-', inline= False)
    myEmbed.add_field(name='Perms', value='`~perms` - only i can do this- ;-;', inline= False)
    myEmbed.add_field(name='Join', value='`~j`, `~join`, `~chotokoe`, `~come`, `~cum` - bot be like *cumming senpapi*', inline= False)
    myEmbed.add_field(name='Play', value='`~play`, `~p`, `~sing` - ... do i need to explain?', inline= False)
    myEmbed.add_field(name='Queue', value='`~queue`, `~q`, `~list` - ur queue UwU if its empty nothing will pop up', inline= False)
    myEmbed.add_field(name='Stop', value='`~stop`, `~s`, `~shush` - stop... get some help', inline= False)
    myEmbed.add_field(name='Leave', value='`~shoo`, `~l`, `~leave` - shoooooo', inline= False)
    myEmbed.add_field(name='Resume', value='`~resume`, `~r` - need to explain?', inline= False)
    myEmbed.add_field(name='Pause', value='`~pause`, `~pp`- yes pp what u gonna do about it?? huh? yeah that what i thot', inline= False)
    #myEmbed.add_field(name='Extras', value='in slash cmds there is a way to find the prefix', inline= False)
    await ctx.channel.send(embed=myEmbed)



#ping==========================================================
@client.command(name= "ping", help="checks latency/sped ponging u in ur brain")
async def ping(ctx, arg = None):
    if arg == "pong":
        await ctx.channel.send("🏓 Marvelous u ponged yourself-")
    else:
        await ctx.channel.send(f"🏓 Pong {round(client.latency * 1000)}ms")



#checking---------------------------------
@client.command(name= "yo")
async def yo(ctx):
    await ctx.channel.send('OOF')



#perms----------------------
@client.command(name = "perms")
@commands.check(is_it_me)
async def perms(content):
    em = discord.Embed(title= "Permissions asked", color= content.author.color)
    em.add_field(name= "By default", value= 'add reactions, priority speaker, stream, see channel, send messages, send tts messages, manage messages, embed links, attach files, read message history, mention everyone, use external emojis, connect, speak, mute members, deafen members, move members, use vad, change nickname', inline= False)
    await content.channel.send(embed= em)
    return




#commands=======================================================


#join---------------------
@client.command(name= "join", help= "to join u in ur drugs adventure", aliases= ["j", "cum", "come", "chotokoe"])
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    
    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()



#play-----------------------
@client.command(name= "play", help= "placing drugs in ur lap", aliases= ["p", "sing"])
async def play(ctx, *, url):
    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)

    if not ctx.voice_client.is_playing():
        await player.queue(url, search=True)
        song = await player.play()

        myEmbed = discord.Embed(title= "PLAYING", color= ctx.author.color)
        myEmbed.add_field(name='**Now playing:**', value=f'{song.name}', inline= False)
        await ctx.send(embed=myEmbed)
     
    else:
        song = await player.queue(url, search =True)
        await ctx.send(f"`{song.name}` has been added to list")



#queue---------------------
@client.command(name="queue", help='queue songs... not ur ass in guild war', aliases= ['q', 'list'])
async def queue(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    await ctx.send(f"{', '.join([song.name for song in player.current_queue()])}")



#stop------------------------
@client.command(name='stop', help='stop... get some help...', aliases = ['s', 'shush'])
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.stop()
    myEmbed = discord.Embed(title= "Stop", color= ctx.author.color)
    myEmbed.add_field(name='Shutting my mouth up', value='at least i shut up in like other ppl', inline= False)
    await ctx.channel.send(embed=myEmbed)
    return



#leave------------------------
@client.command(name='leave', help='When u dont need me', aliases = ["l", "yeet", "shoo", "poof", "dc"])
async def leave(ctx):
    await ctx.voice_client.disconnect()
    
    myEmbed = discord.Embed(title= "Leave", color= ctx.author.color)
    myEmbed.add_field(name='When ur high on drugs that u dont want anymore', value='Let me rest', inline= False)
    await ctx.channel.send(embed=myEmbed)
    return    



#pause------------------------
@client.command(name='pause', help='pauses ur intake of drugs', aliases = ['pp'])
async def pause(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song= await player.pause()

    myEmbed = discord.Embed(title= "Pause", color= ctx.author.color)
    myEmbed.add_field(name=f'Paused `{song.name}', value='To resume use `r`, to leave use `l`, to stop use `s`', inline= False)
    await ctx.channel.send(embed=myEmbed)
    return



#resume------------------------
@client.command(name='resume', help='continues to give u ur drugs',aliases = ['r'])
async def resume(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    song= await player.resume()

    myEmbed = discord.Embed(title= "Resume", color= ctx.author.color)
    myEmbed.add_field(name=f'Re-supplied ur drugs, `{song.name}`', value='To pause use `pp`, to leave use `l`, to stop use `s`', inline= False)
    await ctx.channel.send(embed=myEmbed)
    return





#status==========================================================


@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(choice(status)))



#token==========================================================

client.run("TOken")
