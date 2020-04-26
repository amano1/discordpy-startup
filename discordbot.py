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

r_flag = True

mob_num = 0

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="起動中( ˘ω˘ ) ｽﾔｧ…"))
    #メンバーとpointのリスト作成
    guild = client.get_guild(674983696977362965)
    members = list(guild.members)
    user_dic = {}
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
    
@client.event
async def on_member_join(member): 
    embed = discord.Embed(
        title = "Amano's Macro Serverへようこそ！！",
        description = "まずは[ホームページ](https://tsukumoshimo.wixsite.com/amsserver)を確認してね！^w^)9",
        color = discord.Color.green())
    await member.send(embed = embed)
    ch = client.get_channel(681211296297123956)
    ch_2 = client.get_channel(674983698080202797)
    await ch.send(f"{member.mention}が入船しました。現在錨泊中です。")
    await ch_2.send(f"{member.mention}が入船しました。現在錨泊中です。")
    embed = discord.Embed(
        title = "招待状が届きました!!",
        description = "[🎫](https://discord.gg/PeV2tek)←クリック")
    await member.send(embed = embed)
    
@client.event
async def on_member_remove(member): 
    ch = client.get_channel(681211296297123956)
    ch_2 = client.get_channel(674983698080202797)
    await ch.send(f"{member.mention}がAMSを去りました、( ´Д｀)ﾉ~ﾊﾞｲﾊﾞｲ")
    await ch_2.send(f"{member.mention}がAMSを去りました、( ´Д｀)ﾉ~ﾊﾞｲﾊﾞｲ")
@tasks.loop(seconds=10)
async def loop():
    global user_dic,user_list,mob_num
    guild = client.get_guild(674983696977362965)
    members = list(guild.members)
    for member in members:
        id = [446610711230152706,690901325298401291,
              644153226597498890,697262684227371059,
              526620171658330112,172002275412279296,
              674982292111884300,627052576810074112]
        pattern = r'^(\［(\d{1,})］)'
        result = re.search(pattern,member.display_name)
        if result:
            point = int(result.group(2))
            user_dic[member.id]=point
        elif not member.id in id:
            print(f"{member.name}:didnt match")
            user_dic[member.id]=0
            try:
                await member.edit(nick = f"［0］{member.name}")
            except:
                print(f"❌┃{member}のニックネームを変更できませんでした")
            else:
                print(f"⭕┃{member}のニックネームにPoint:0を追加")
    num = len(guild.members)
    await client.change_presence(activity=discord.Game(name=f"{num}members"))
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
    if ch_1.name != f"🥇{num1_set[1]}|{user_1.name}":
        if num1_set[1] == 0:
            await ch_1.edit(name = f"🥇None")
            print(ch_1.name)
            print(ch_2.name)
            return
        await ch_1.edit(name = f"🥇{num1_set[1]}|{user_1.name}")
    if ch_2.name != f"🥈{num1_set[1]}|{user_2.name}":
        if num2_set[1] == 0:
            await ch_2.edit(name = f"🥈None")
            print(ch_1.name)
            print(ch_2.name)
            return
        await ch_2.edit(name = f"🥈{num2_set[1]}|{user_2.name}")
    if ch_3.name != f"🥉{num3_set[1]}|{user_3.name}":
        if num3_set[1] == 0:
            await ch_3.edit(name = f"🥉None")
            return
        await ch_3.edit(name = f"🥉{num3_set[1]}|{user_3.name}") 
        print(ch_3.name)
    ch_mob = client.get_channel(703822197139177495)
    mob_num_sub = mob_num
    num = int(ch_mob.name.split("エネミー║")[1])
    if mob_num == 0"
        return
    await ch_mob.edit(name = f"エネミー║{num+mob_num}")
    mob_num -= mob_num_sub
    
@client.event
async def on_message(message):
    amano = client.get_user(690901325298401291)
    global user_dic
    if not message.channel.guild:
        return
    
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
        em_title = "None"
        em_desc = "None"
        if message.embeds[0].title:
            em_title = message.embeds[0].title
        if message.embeds[0].description:
            em_desc = message.embeds[0].description
        pattern_a = r"^属性:\[(.+)] \| ランク:【(.+)】\n(.+)が待ち構えている...！\nLv\.(\d+)  HP:(\d+)"
        pattern_b = r"(.{1,})は(\d{1,})経験値を獲得"
        result_a = re.search(pattern_a,em_title)
        result_b = re.search(pattern_b,em_desc)
        if result_a:
            global mob_num
            mob_num += 1
            result= result_a
            ch = client.get_channel(703821795387768832)
            if result.group(2) == "超激レア":
                num = int(ch.name.split("超激レア║")[1])
                await ch.edit(name = f"超激レア║{num + 1}")
                embed = discord.Embed(
                    title = "超激レア出現！",)
     
        if result_b:
            result = result_b
            mention = result.group(1)
            exp = result.group(2)
            user = discord.utils.get(client.users,mention = mention)
            if not user or user == amano:
                return
            pattern = r'^(\［(\d{1,})］)'
            member = message.guild.get_member(user.id)
            result_2 = re.search(pattern,member.display_name)
            if not result_2:
                user_dic[user.id] = 1 
                try:
                    await member.edit(nick = f"［0］{member.name}")
                except:
                    pass
                else:
                    pass
                return
            if user.id in user_dic:
                user_dic[user.id] = int(user_dic[user.id]) + 1
            try:
                await member.edit(nick = f"［{user_dic[user.id]}］{member.name}")
            except:
                pass
            else:
                pass
            
    global r_flag
    if message.content == "i)reward":
        if r_flag == False:
            await message.channel.send("CoolDown中")
            return
        r_flag = False
        ch_id = 701721786592657461
        ch = client.get_channel(ch_id)
        user = message.author
        point = user_dic[user.id]
        if user_dic[user.id] == 0:
            await message.channel.send("Pointが無いんだけど?")
            r_flag = True
            return
        await ch.send(f"reward [{user.id}] [{user_dic[user.id]}]")
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
            r_flag = True
        else:        
            pattern = r"(\d{1,}) has been deducted"
            result = re.search(pattern,resp.content)
            if not result:
                embed = discord.Embed(
                    title = f"あちゃーごめん{user.name}。\nなんか報酬配布がうまくいかなかったわ",
                    color = discord.Color.red())
                await message.channel.send(embed = embed)
                r_flag = True
                return
            member = discord.utils.get(message.guild.members,id = user.id)
            await member.edit(nick = f"［0］{member.name}")
            user_dic[user.id] = 0
            print(user_dic[user.id])
            embed = discord.Embed(
                title = f"{user.name}に**{point}TCredit**を配布したよ！。\nおめでとう！(Pointがリセットされました)",
                color = discord.Color.green())
            await message.channel.send(embed = embed)
            await asyncio.sleep(10)
            r_flag = True
    
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
