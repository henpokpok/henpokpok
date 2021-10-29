
import discord 
from discord.ext import commands
from datetime import datetime, timezone, timedelta
import table

import os
from dotenv import load_dotenv


load_dotenv('.env')

bot = commands.Bot(command_prefix='a!' )

@bot.event
async def on_ready():
    print('{0.user}'.format(bot), 'is ready2')
    print("==================")
    await bot.change_presence(activity=discord.Game(name="Timetable"))

@bot.event
async def on_message(message):
    await talk_bot(message) 

@bot.event
async def talk_bot(message):   
    tz = timezone(timedelta(hours = 7))
    # Date with timezone
    date = datetime.now(tz=tz) 
    print(date)
    day_today = str(date.today().strftime("%A"))
    time_start = date.today().strftime("%H:%M")  
    if str(time_start) >= "08:10" and str(time_start) <= "08:50":
        x = 0
    elif str(time_start) >= "08:50" and str(time_start) <= "09:30":
        x = 1
    elif str(time_start) >= "09:30" and str(time_start) <= "10:10":
        x = 2
    elif str(time_start) >= "10:10" and str(time_start) <= "10:50":
        x = 3
    elif str(time_start) >= "10:50" and str(time_start) <= "11:30":
        x = 4
    elif str(time_start) >= "11:30" and str(time_start) <= "12:10":
        x = 5
    elif str(time_start) >= "12:10" and str(time_start) <= "13:00":
        x = 6
    elif str(time_start) >= "13:00" and str(time_start) <= "13:40":
        x = 7
    elif str(time_start) >= "13:40" and str(time_start) <= "14:20":
        x = 8
    elif str(time_start) >= "14:20" and str(time_start) <= "15:00":
        x = 9
    else:
        x = 10
    print(day_today)
    print(time_start)
    print(x)

    if 'คาบนี้' in message.content or 'ตอนนี้' in message.content:  
        if day_today in table.day and x < 10:
            embed=discord.Embed(title="คาบนี้" , color=0x84c5e6)
            embed.add_field(name="คาบ", value=f"{table.day[f'{day_today}'][x]} {table.timestart['timestart'][x]} - {table.timestart['timestart'][x+1]}", inline=False)
            embed.add_field(name="ครูผู้สอน", value=f"{table.Teacher[f'{day_today}'][x]} {table.timestart['timestart'][x]} - {table.timestart['timestart'][x+1]}", inline=False)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("อะไรของมึง กวนตีนกูหรอ")

    if 'คาบต่อไป' in message.content or 'คาบหน้า' in message.content:
        if day_today in table.day and x < 10:
            embed=discord.Embed(title="คาบต่อไป" , color=0x84c5e6)
            embed.add_field(name="คาบ", value=f'table.day[f"{day_today}"][x+1]', inline=False)
            embed.add_field(name="ครูผู้สอน", value=f'table.Teacher[f"{day_today}"][x+1]', inline=False)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("ไม่มีเรียน อย่าโง่")
    
    if 'คาบเมื่อกี้' in message.content or 'คาบที่แล้ว' in message.content:  
        if day_today in table.day and x < 10:
            embed=discord.Embed(title="คาบที่แล้ว" , color=0x84c5e6)
            embed.add_field(name="คาบ", value=f'table.day[f"{day_today}"][x-1]', inline=False)
            embed.add_field(name="ครูผู้สอน", value=f'table.Teacher[f"{day_today}"][x-1]', inline=False)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("มึงเอ๋อหรอ")

    if 'ตารางเรียน' in message.content:   
        file = discord.File("ตารางเรียน.jpg")
        await message.channel.send(file = file)

    if message.content == 'a!help':
        embed=discord.Embed(title="Help" , color=0x84c5e6)
        embed.add_field(name="a!help", value="ส่งหน้า Help", inline=False)
        embed.add_field(name="คาบนี้", value="เพื่อดูคาบเรียนปัจจุบัน", inline=False)
        embed.add_field(name="คาบต่อไป", value="เพื่อดูคาบเรียนคาบต่อไป", inline=False)
        embed.add_field(name="คาบที่แล้ว", value="เพื่อดูคาบเรียนคาบที่แล้ว", inline=False)
        embed.add_field(name="ตารางเรียน", value="เพื่อดูตารางสอน", inline=True)
        embed.set_thumbnail(url = bot.user.avatar_url)
        await message.channel.send(embed=embed)


bot.run(os.getenv("TOKEN"))
