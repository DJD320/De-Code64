import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from itertools import cycle
import base64

client = commands.Bot(command_prefix = '.')
status = cycle(['at decoding your codes!', 'with DMs!'])
client.remove_command('help')

@client.event
async def on_ready():
#    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('debug'))
    change_status.start()
    print('The bot is ready.')

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Time:{round(client.latency * 1000)}ms')

@client.command()
async def help(ctx):
    helpEmbed = discord.Embed(
        title = 'De-Code64 | By DJD320',
        description = 'De-Code64 is a custom bot created by DJD320#7656 with the purpose of simplifying the encoding and decoding of text in Base64. Look down for the commands!',
        colour = discord.Colour.green()
    )
    
    helpEmbed.set_image(url='https://cdn.discordapp.com/avatars/765891165382770709/e0b1e90cf6d0a559923a13b724d27b65.png')
    helpEmbed.add_field(name='.help', value="Shows this!" , inline=True)
    helpEmbed.add_field(name='.encode "TextToEncode" / .e "TextToEncode"', value="Encodes your text!" , inline=True)
    helpEmbed.add_field(name='.decode "TextToEncode" / .d "TextToEncode"', value="Decodes your text!" , inline=True)
    helpEmbed.add_field(name='.ping', value="Pong!" , inline=True)
    await ctx.send(embed=helpEmbed)
    

@client.command(aliases=['e'])
# @commands.guild_only()
async def encode(ctx, *, string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes) 
    base64_string = base64_bytes.decode("ascii") 
    await ctx.author.send(f'Non encoded: {string}\nEncoded: {base64_string}')
    await ctx.send(":white_check_mark:")

@client.command(aliases=['d'])
# @commands.guild_only()
async def decode(ctx, *, string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.b64decode(string_bytes) 
    base64_string = base64_bytes.decode("ascii") 
    await ctx.author.send(f'Non-Decoded: {string}\nDecoded: {base64_string}')
    await ctx.send(":white_check_mark:")


# @client.command(aliases=['e'])
# async def encode(ctx, *, nonenc):
#     await ctx.send(f'Non encoded: {nonenc}\nEncoded: {nonenc.encode()}')


client.run('YOUR TOKEN HERE')