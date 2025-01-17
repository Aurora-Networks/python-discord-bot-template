from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return '''<body style="margin: 0; padding: 0;">
    <iframe width="100%" height="100%" src="https://axocoder.vercel.app/" frameborder="0" allowfullscreen></iframe>
  </body>'''

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()

keep_alive()
print("Server Running Because of Axo")
import discord
from discord.ext import commands
import requests

token = YOUR_BOT_PREFIX_HERE
prefix = YOUR_BOT_TOKEN_HERE

client = commands.Bot(command_prefix= prefix)
client.remove_command("help") #to remove the default boring help command


@client.event
async def on_ready():
    print("We have logged in as {0.user} ".format(client)) 
    activity = discord.Game(name=".help", type=3)               # this is to writing prefix in playing a game.(optional)
    await client.change_presence(status=discord.Status.online, activity=activity) # this is for making the status as an online and writing prefix in playing a game.(optional)  
                            
                            
                            
                            
#Help commands
@client.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title="IndianDesiMemer Help Center ✨",color=0xF49726)
    embed.add_field(name="Command Categories :",value="🐸 `memes    :` Image generation with a memey twist.\n" + "🔧 `utility  :` Bot utility zone\n😏 `nsfw     :` Image generation with a memey twist.\n\nTo view the commands of a category, send `.help <category>`" ,inline=False)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Help requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)
                            

#Sub-help command of memes
@help.command ()
async def memes(ctx):
    embed=discord.Embed(title="IndianDesiMemer Help Center ✨", description="Commands of **meme** \n`.meme:`Memes",inline=False)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Command requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)
                            

#Sub-help commands of nsfw                           
@help.command ()
async def nsfw(ctx) :
    embed=discord.Embed(title="IndianDesiMemer Help Center ✨", description="Commands of **nsfw** \n`.nsfw:`NSFW", color=0xF49726)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Command requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)


#Sub-help commands of utility                           
@help.command ()
async def utility(ctx) :
    embed=discord.Embed(title="IndianDesiMemer Help Center ✨", description="Commands of **utility** \n`.ping:`Latency", color=0xF49726)
    embed.set_footer(icon_url=ctx.author.avatar_url,text="Command requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)                            


# it is used for the cooldown to prevent the bot from spam attack                             
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("**Try after {0} second ".format(round(error.retry_after, 2)))                            
                            
                            
#meme command                            
@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel) # it is used for the cooldown to prevent the bot from spam attack                            
async def meme(ctx):
    
    response = requests.get("https://meme-api.herokuapp.com/gimme/"+"memes"+"memes"+"?t=all?hot")
    
    m = response.json()
    postLink = (m["postLink"])
    subreddit = (m["subreddit"])
    title = (m["title"])
    imageUrl =  (m["url"])
    upVote = (m["ups"])
    uv = str(upVote)

    embed=discord.Embed(title= title, url=postLink,color=0xF49726)
    embed.set_image(url=imageUrl)
    embed.set_footer(text="\n👍\t"+ uv+ "  By :r/"+subreddit)
    await ctx.send(embed=embed)                            
                            
#nsfw command
@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel)
async def nsfw(ctx):
  if ctx.channel.is_nsfw():
     print("nsfw work!!")
  else:
    print("You can use this command in a nsfw channel only !")                            
                            
                            
#ping command                            
@client.command()
@commands.cooldown(1, 10, commands.BucketType.channel) # it is used for the cooldown to prevent the bot from spam attack                            
async def ping(ctx):
    await ctx.send('Ping! **{0}**ms'.format(round(client.latency, 1)))
                            
                      
client.run(MTIwODAxOTIzMzAxNTk4ODMzNQ.GjDPIl.xqUaxd4asSSysDAdvW4voT4qu_FtG_MAPDkKEQ)    
                            
                            
                            
