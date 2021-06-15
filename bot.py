import discord
from discord.ext import commands
import json
import random

from discord.ext.commands.converter import MemberConverter


with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)





intents = discord.Intents.all()
bot = commands.Bot(command_prefix='+' , intents=intents)
client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(">>心心 code-92 上線了")
   




@bot.event
async def on_member_join(member):
    channel = bot.get_channel(805371305855025184)
    await channel.send(f"{member.mention} 加入了! (踩")
    
    
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(834079223802232853)
    await channel.send(f'{member.mention} 離開了! (踢')

@bot.command()
async def love(ctx):
    love = random.choice(jdata['hug'])
    await ctx.send(love)



@bot.command()
async def ping(ctx):
    await ctx.send(f'心心code-92延遲為{round(bot.latency*1000)}ms')



@bot.command()
async def stomp(ctx):
    pic = random.choice(jdata['sttomp'])
    await ctx.send('就那麼想被心心我踩嗎?色小鬼?')
    await ctx.send(pic)
   

@bot.command()
async def food(ctx):
    ranndom_pic = random.choice(jdata['food pic'])
    await ctx.send('心心主廚上菜啦')
    await ctx.send(ranndom_pic)

@bot.command()
async def roll(ctx):
    roll_pic = random.choice(jdata['roll_number6'])
    await ctx.send('你骰到')
    await ctx.send(roll_pic)







bot.run('ODU0MjMyMDc1MDIwMjcxNjI1.YMg7nQ.sjTJFkFULDDBbkKqTIbihpgE_RM')