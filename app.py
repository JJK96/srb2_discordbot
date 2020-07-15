from discord import Embed, Colour
from discord.ext import commands
import api_connector as con
from credentials import TOKEN

# initialize a Client instance
bot = commands.Bot(command_prefix="!")
bot.remove_command('help')

# when the bot starts running
@bot.event
async def on_ready():
    # print the bot's username
    print('Logged in as '+ bot.user.name)

# race!leaderboard command received
@bot.command()
async def leaderboard(ctx):
    await ctx.send(con.get_leaderboard())
    
# race!status command received
@bot.command()
async def status(ctx):
    await ctx.send(con.get_status())

# race!search command received
@bot.command()
async def search(ctx, map=None, skin=None, player=None):
    await ctx.send(con.get_search_result(map, skin, player))

# race!help command received
@bot.command()
async def help(ctx):
    # create an embed message
    embed = Embed(colour=Colour.orange())
    
    # set the title
    embed.set_author(name="Help")
    
    # set the commands with descriptions
    embed.add_field(name="race!status", value="Returns the server status", inline=False)
    embed.add_field(name="race!leaderboard", value="Returns the player leaderboard", inline=False)
    embed.add_field(name="race!search", value=('Usage: race!search "<map name>" "[skin name]" "[username]"\n''All parameters can be submitted with no "" if they '"don't require spaces"), inline=False)
    
    # get the command sender
    member = ctx.message.author
    
    # if it exists
    if member:
        # get the bot - user dm channel
        channel = member.dm_channel
        # if the dm channel hasn't yet been created
        if not channel:
            # create the dm channel
            channel = await member.create_dm()
        # send the message
        await channel.send(embed=embed)

# run
if __name__== "__main__":
    # connect the client to the bot
    bot.run(TOKEN)
