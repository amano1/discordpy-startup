# discordpy-startup
# -*- coding: utf-8 -*-
import sys
import discord
import random
import asyncio
import time
import datetime
import urllib.request
import json
import re
import os
import traceback
import math

from discord.ext import tasks
from datetime import datetime, timedelta, timezone

import logging

# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), 'JST')

client = discord.Client()
TOKEN = os.environ['DISCORD_BOT_TOKEN']
server_number = len(client.guilds)


user_dic = {}
user_list = []

deleuser = None
delech = None


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="起動中( ˘ω˘ ) ｽﾔｧ…"))
    
    #メンバーとpointのリスト作成
    global user_dic
    guild = client.get_guild(674983696977362965)
    members = list(guild.members)
    for member in members:
        id = [446610711230152706,
              690901325298401291,
              446610711230152706]
        pattern = r'^(\［(\d{1,})］)'
        result = re.search(pattern,member.display_name)
        if result:
            point = int(result.group(2))
            user_dic[member.id]=point
            print(f"{member.name}:match [point]")
        elif not (member.id in id) or not member.bot:
            print(f"{member.name}:didnt match")
            user_dic[member.id]=0
            try:
                await member.edit(nick = f"［0］{member.name}")
            except:
                print(f"❌┃{member}のニックネームを変更できませんでした")
            else:
                print(f"⭕┃{member}のニックネームにPoint:0を追加")
    else:
        user_list = sorted(user_dic.items(), key=lambda x:x[1], reverse=True)
        print(user_list)
        ch_1 = client.get_channel(701803530566238290)
        ch_2 = client.get_channel(701803756571983893)
        ch_3 = client.get_channel(701803622811435028)
        num1_set = list(list(user_list)[0])
        num2_set = list(list(user_list)[1])
        num3_set = list(list(user_list)[2])
        print(num1_set)
        print(num2_set)
        print(num3_set)
        user_1 = client.get_user(num1_set[0])
        user_2 = client.get_user(num2_set[0])
        user_3 = client.get_user(num3_set[0])
        await ch_1.edit(name = f"🥇{num1_set[1]}|{user_1.name}")
        await ch_2.edit(name = f"🥈{num2_set[1]}|{user_2.name}")
        await ch_3.edit(name = f"🥉{num3_set[1]}|{user_3.name}")
        print(ch_1.name)
        print(ch_2.name)
        print(ch_3.name)
        
        
        #起動ログを指定のチャンネルに送信
        ready_chid = 701739744320553015
        ready_ch = client.get_channel(ready_chid)
        dateTime = datetime.now(JST)
        embed = discord.Embed(
            title = "起動ログ",
            description = f"{dateTime}")
        await ready_ch.send(embed = embed)
        num = len(guild.members)
        await client.change_presence(activity=discord.Game(name=f"{num}members in this server"))
        loop.start()
        print("―――――――――――――――――――――――――――――――――――――")

        
@tasks.loop(seconds=10)
async def loop():
    print(datetime.now(JST))
    global user_dic
    global user_list
    '''
    num = len(guild.members)
    await client.change_presence(activity=discord.Game(name=f"{num}members in this server║{datetime.now(JST)}"))
    user_list = sorted(user_dic.items(), key=lambda x:x[1], reverse=True)
    ch_1 = client.get_channel(701803530566238290)
    ch_2 = client.get_channel(701803756571983893)
    ch_3 = client.get_channel(701803622811435028)
    num1_set = list(list(user_list)[0])
    num2_set = list(list(user_list)[1])
    num3_set = list(list(user_list)[2])
    user_1 = client.get_user(num1_set[0])
    user_2 = client.get_user(num2_set[0])
    user_3 = client.get_user(num3_set[0])
    await ch_1.edit(name = f"🥇{num1_set[1]}|{user_1.name}")
    await ch_2.edit(name = f"🥈{num2_set[1]}|{user_2.name}")
    await ch_3.edit(name = f"🥉{num3_set[1]}|{user_3.name}")
    print(ch_1.name)
    print(ch_2.name)
    print(ch_3.name)
    '''
    
@client.event
async def on_message(message):
    amano = client.get_user(690901325298401291)
    global user_dic
    
    if message.content.startswith("i)point "):
        u = None
        try:
            user_id = int(message.content.split("i)point ")[1])
        except:        
            user_mention = message.content.split("i)point ")[1]
            u = discord.utils.get(message.guild.members,mention = user_mention)
        else:
            u = client.get_user(user_id)
        user = u
        if user:
            point = user_dic[user.id]
            embed = discord.Embed(
                title = f"{user}さんのPointは{point}です")
        

    if message.embeds and message.channel.category.id == 674983811850960916:
        if not message.embeds[0].title:
            return
        if not message.embeds[0].description:
            return
        em_title = message.embeds[0].title
        em_desc = message.embeds[0].description
        pattern = r"(.{1,})は(\d{1,})経験値を獲得"
        result = re.search(pattern,em_desc)
        if not result:
            print("didnt match A")
            return
        mention = result.group(1)
        exp = result.group(2)
        user = discord.utils.get(client.users,mention = mention)
        if not user:
            print("didnt match B")
            return
        if user.id in user_dic:
            user_dic[user.id] = int(user_dic[user.id]) + 1
        else:
            user_dic[user.id] = 1
        member = message.guild.get_member(user.id)
        try:
            await member.edit(nick = f"［{user_dic[user.id]}］{member.name}")
        except:
            pass
        else:
            pass
            
            
    if message.content == "i)reward":
        ch_id = 701721786592657461
        ch = client.get_channel(ch_id)
        user = message.author
        if {user_dic[user.id]} == 0:
            await message.channel.send("Pointが無いんだけど?")
            return
        await ch.send(f"reward [{user.id}] [{user_dic[user.id]}]")
        user_dic[user,id] = 0
        def check(msg):
            if msg.author.id != 172002275412279296:
                return 0
            if msg.channel.id != ch_id:
                return 0
            if not "deducted" in msg.content:
                return 0
            if not amano.name in msg.content:
                return 0
            return 1
        try:
            resp = await client.wait_for("message",timeout = 5,check = check)
        except:
            embed = discord.Embed(
                title = f"あちゃーごめん{user.name}。\nなんか報酬配布がうまくいかなかったわ",
                color = discord.Color.red())
            await message.channel.send(embed = embed)
        else:        
            pattern = r":yen: (\d{1,}) has been deducted"
            result = re.sub(pattern,"match",resp)
            print(result)
            if result != "match":
                embed = discord.Embed(
                    title = f"あちゃーごめん{user.name}。\nなんか報酬配布がうまくいかなかったわ",
                    color = discord.Color.red())
                await message.channel.send(embed = embed)
                return
            if point != result.group(2):
                member = message.guild.member(user.id)
                await member.edit(nick = f"［0］{member.name}")
                embed = discord.Embed(
                    title = f"{user.name}に**{point}TCredit**を配布したよ！。\nおめでとう！(Pointがリセットされました)",
                    color = discord.Color.green())
                await message.channel.send(embed = embed)
    
    global deleuser
    global delech
    if deleuser and delech and message.channel==delech and message.author==deleuser:
        await message.delete()
        embed = discord.Embed(
            title = f"{deleuser}の発言",
            description = f"||{message.content}||")
        await message.channel.send(embed = embed)
    if message.content.startswith('i)dele'):
        deleuser_id=int(message.content.split(' ')[1])
        deleuser=client.get_user(deleuser_id)
        delech_id=int(message.content.split(' ')[2])
        delech=client.get_channel(delech_id)
        await message.channel.send(embed = discord.Embed(title = f"{deleuser}を{delech.name}で全力ミュートします"))

    if message.content=='i)deleNone':
        delech=None
        deleuser=None
    
    
client.run(TOKEN)
