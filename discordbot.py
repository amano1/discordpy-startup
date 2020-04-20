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
        if "║Point：" in member.display_name:
            point = int((member.display_name).split("║Point：")[1])
            user_dic[member.id]=point
        elif member_id != 690901325298401291 and not member.bot:
            user_dic[member.id]=0
            await member.edit(nick = f"{member.name}║Point：0")
    print(user_dic)

    
    loop_30.start
    
    #起動ログを指定のチャンネルに送信
    ready_chid = 701739744320553015
    ready_ch = client.get_channel(ready_chid)
    dateTime = datetime.now(JST)
    embed = discord.Embed(
        title = "起動ログ",
        description = f"{dateTime}")
    await ready_ch.send(embed = embed)
    await client.change_presence(activity=discord.Game(name="動作中(^w^三^w^)おっおっおっ"))

    
@tasks.loop(seconds=30)
async def loop_30():
    pass
    

@client.event
async def on_message(message):
    global user_dic
    
    if message.content.startswith("i)point "):
        user_id = int(message.content.split("i)point ")[1])
        user_mention = message.content.split("i)point ")[1]
        user = None
        try:
            u = client.get_user(user_id)
        except:
            pass
        else:
            user = u
        try:
            u = discord.utils.get(message.guild.members,mention = user_mention)
        except:
            pass
        else:
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
        if not "戦闘結果" in em_title:
            return
        print("戦闘結果")
        mention = (em_desc.split("\n")[2]).split("は")[0]
        user = discord.utils.get(client.users,mention = mention)
        if not user or user.id == 690901325298401291:
            return
        if user.id in user_dic:
            user_dic[user.id] = int(user_dic[user.id]) + 1
        else:
            user_dic[user.id] = 1
        print(f"{user.name}:{user_dic[user.id]}")
        member = message.guild.get_member(user.id)
        await member.edit(nick = f"{user.name}║Point：{user_dic[user.id]}")
        
    if message.content == "a)reward":
        user = message.author
        ch_id = 701721786592657461
        ch = client.get_channel(ch_id)
        await ch.send(f"t!credit {user.id} {user_dic[user.id]}")
        def check(msg):
            if msg.author.id != 172002275412279296:
                return 0
            if not msg.content.startswith("Transferring"):
                return 0
            if msg.channel != ch:
                return 0
            return 1
        try:
            t_msg=await client.wait_for('message',timeout=5,check = check)
        except asyncio.TimeoutError:
            await ch.send('…ん？竜巻返事ない。謎ｗ')
        else:
            code = t_msg.content.split("To confirm, type `")[1].split("` or type")[0]
            await ch.send(code)
            user_dic[user.id] = 0
            member = message.guild.get_member(user.id)
            await member.edit(nick = f"{user.name}║Point：{user_dic[user.id]}")            

    
    
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
    
    
client.run(OKEN)
