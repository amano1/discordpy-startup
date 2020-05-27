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
    guild = client.get_guild(674983696977362965)
    members = list(guild.members)
    user_dic = {}
    #起動ログを指定のチャンネルに送信
    ready_chid = 715106478423539774
    ready_ch = client.get_channel(ready_chid)
    dateTime = datetime.now(JST)
    embed = discord.Embed(
        title = "起動ログ",
        description = f"{dateTime}")
    embed.add_field(
        name = "Information",
        value = "None")
    
    await ready_ch.send(embed = embed)
    num = len(guild.members)
    await client.change_presence(activity=discord.Game(name=f"{num}members in this server"))
    loop.start()
    
@client.event
async def on_member_join(member): 
    embed = discord.Embed(
        title = "Amano's Macro Serverへようこそ！！",
        description = "まずは[ホームページ](https://tsukumoshimo.wixsite.com/amsserver)を確認してね！^ω^)9",
        color = discord.Color.green())
    await member.send(embed = embed)
    ch = client.get_channel(715106478423539774)
    await ch.send(f"{member.mention}が入船しました。現在錨泊中です。")
    embed = discord.Embed(
        title = "招待状が届きました!!",
        description = "[🎫](https://discord.gg/PeV2tek)←クリック")
    await member.send(embed = embed)
    
@client.event
async def on_member_remove(member): 
    ch = client.get_channel(715106478423539774)
    await ch.send(f"{member.mention}({member})がAMSを去りました、( ´Д｀)ﾉ~ﾊﾞｲﾊﾞｲ")
@tasks.loop(seconds=1)
async def loop():
    
    guild = client.get_guild(674983696977362965)
    await guild.edit(name = f"Amano's Macro Server {datetime.now(JST)}")

    '''
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
                nick = f"［0］{member.name}"
                if 32 < len(list(nick)):
                    nick = nick[:(len(list(nick))) - 1] + "…"
                await member.edit(nick = nick)
            except:
                print(f"❌┃{member}のニックネームを変更できませんでした")
            else:
                print(f"⭕┃{member}のニックネームにPoint:0を追加")
    num = len(guild.members)
    await client.change_presence(activity=discord.Game(name=f"i)help║{num}members in AMS"))
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
    if mob_num == 0:
        return
    await ch_mob.edit(name = f"エネミー║{num+mob_num}")
    mob_num -= mob_num_sub
    '''
    
@client.event
async def on_message(message):
    try:
        amano = client.get_user(690901325298401291)
        global user_dic
        guild = client.get_guild(674983696977362965)

        m_ctt = message.content
        m_ch = message.channel
        m_author = message.author

        if m_ctt.startswith("i)kick "):
            if not "mano" in m_author.name:
                return
            id = int(m_ctt.split(" ")[1])
            user = client.get_user(id)
            await guild.kick(user)
            ch = client.get_channel(715106478423539774)
            await ch.send(f"{user}をKick")

        ran = random.randint(0,20)
        if int(ran) == 10:
            embed = discord.Embed(
                title = "Error",
                description = "found the unsatisfactory system\n<type:AkiyamaNaoto>")
            await message.channel.send(embed = embed)


        if not message.channel.guild:
            return


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
                    role = message.guild.get_role(706527459067297864)
                    embed = discord.Embed(
                        title = "超激レア出現！",
                        description = (
                            f"{role.mention}\n{message.channel.mention}で**{result.group(3)}**が出現したよ！" +
                            f"\nLv：`{result.group(4)}`\nHP：`{result.group(5)}`\nExp：`{int(result.group(4)) * 100}`" +
                            f"\n[この{result.group(3)}への直通リンク]({message.jump_url})"))
                    embed.set_thumbnail(url = message.embeds[0].image.url)
                    embed.timestamp = datetime.now(JST)
                    ch = client.get_channel(706931443875708958)
                    await ch.send(embed = embed)
                    num = int(ch.name.split("║")[1])
                    await ch.edit(name =  f"超激レア出現║{num + 1}")
                if message.channel.id == 674983853416251423:
                    await ch.edit(name = f"甲-Lv{result_a.group(4)}")
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


        if message.content.startswith("i)help"):
            embed = None
            member = message.guild.get_member(message.author.id)
            HELP_PAGE = None
            try:
                HELP_PAGE = message.content.split("i)help ")[1]
            except:
                embed = discord.Embed(
                    title = "彩由Help一覧ページ\n",
                    description = (
                        "`i)help コマンド`で各コマンドのヘルプが確認可能です。" +
                        "```ini\n[help,reward,メンバー役職,ヘルパー役職,超激レア通知役職,鯖缶の呟き通知役職]```"
                    ),
                    color = discord.Color.green()
                )
            else:
                if HELP_PAGE == "help":
                    embed = discord.Embed(
                        title = "Command Info\n`i)help`",
                        description = (
                            "各コマンドのヘルプが確認出来る。ヘルプで見れるコマンドには" +
                            "```ini\n[help,reward,メンバー役職,ヘルパー役職,超激レア通知役職,鯖缶の呟き通知役職]```がある"),
                        color = discord.Color.green()
                    )

                elif HELP_PAGE == "reward":        
                    pattern = r'^(\［(\d{1,})］)'
                    result = re.search(pattern,member.display_name)
                    point = None
                    if result:
                        point = int(result.group(2))
                    else:
                        point = "何かよくわかんない"
                    embed = discord.Embed(
                        title = "Command Info\n`i)reward`",
                        description = (
                            "pointをTatsumakiCreditに換金できる。\n" +
                            "pointは`🌙TAO🌙`カテゴリーのチャンネルで敵を倒すと増える。\n" +
                            "名前の横にある[]の中の数字が現在の所持pointである。\n" +
                            f"ちなみに貴方のpointは{point}"+
                            "※現在停止中"),
                        color = discord.Color.green()
                    )
                elif HELP_PAGE == "超激レア通知役職":
                    embed = discord.Embed(
                        title = "Command Info\n`i)超激レア通知役職`",
                        description = "AMSで超激レアキャラが出現したときに通知する役職を付与",
                        color = discord.Color.green()
                    )

                elif HELP_PAGE == "鯖缶呟き通知役職":
                    embed = discord.Embed(
                        title = "Command Info\n`i)鯖缶呟き通知役職`",
                        description = (
                            f"鯖缶({amano.mention})の他愛もない呟きの通知をする役職を付与。\n" +
                            "**※メンション多め(そもそもこの鯖自体メンション多すぎ)**"),
                        color = discord.Color.green()
                    )
                elif HELP_PAGE == "メンバー役職":
                    embed = discord.Embed(
                        title = "Command Info\n`i)メンバー役職`",
                        description = (
                            "鯖のMember役職を付与。\n" +
                            "ぶっちゃけなくても変わりない。"),
                        color = discord.Color.green()
                    )
                elif HELP_PAGE == "ヘルパー役職":
                    ch = client.get_channel(707053103983231007)
                    embed = discord.Embed(
                        title = "Command Info\n`i)ヘルパー役職`",
                        description = (
                            "ServerHelper役職を付与。\n" +
                            f"{ch.mention}で発言できるようになるよ。\n" +
                            "※役職の付与にあたって制限はありません。"),
                        color = discord.Color.green()
                    )
                else:
                    embed = discord.Embed(
                        title = f"Error",
                        description = f"`{HELP_PAGE}`ってコマンドはなかったかなぁ…？",
                        color = discord.Color.red())
            embed.timestamp = datetime.now(JST)
            await message.channel.send(embed = embed)
                
        global r_flag
        if message.content == "i)mlist":
            text = ""
            num = 0
            # 最大で10人ずつ取り出したい
            size = 10
            for start in range(0, len(guild.members), size):
                ms = guild.members[start:start+size]
                mnum_s = guild.members.index(ms[0]) + 1
                mnum_e = guild.members.index(ms[-1]) + 1
                for m in ms:
                    type = ""
                    if m.status == discord.Status.online:
                        text += f"\n+ 〇{m}"
                    elif m.status == discord.Status.dnd:
                        text += f"\n- {m}"
                    elif m.status == discord.Status.idle:
                        text += f"\n- {m}"
                    elif m.status == discord.Status.offline:
                        text += f"\n- {m}"
                embed = discord.Embed(
                    title = f"AMSメンバーリスト",
                    description = f"```diff{text}```")
                embed.set_footer(text = f"{mnum_s}~{mnum_e}/{len(guild.members)}人")
                await message.author.send(embed = embed)
                text = "" 

        if message.channel.id == 707267427624288268:
            if message.embeds:
                return
            await message.delete()
            if message.author == amano:
                role = message.guild.get_role(707270363167326260)
                embed = discord.Embed(
                    title = "",
                    description = f"{message.content}\n{role.mention}",
                    color = discord.Color.blue())
                embed.set_author(name = amano,icon_url = amano.avatar_url)
            else:
                embed = discord.Embed(
                title = "",
                description = f"{message.content}\n{amano.mention}",
                color = discord.Color.green())
                embed.set_author(name = message.author,icon_url = message.author.avatar_url)
            embed.timestamp = datetime.now(JST)
            await message.channel.send(embed = embed)



        if message.content == "i)超激レア通知役職":
            role = message.guild.get_role(706527459067297864)
            m = message.guild.get_member(message.author.id)
            try:
                await m.add_roles(role)
            except:
                await message.channel.send("エラー出たw")     
            else:
                await message.channel.send(f"{message.author.mention}に[超激レア通知役職]をつけたよ(　•̀ω•́)و✧")   


        if message.content == "i)鯖缶の呟き通知役職":
            role = message.guild.get_role(707270363167326260)
            m = message.guild.get_member(message.author.id)
            try:
                await m.add_roles(role)
            except:
                await message.channel.send("エラー出たw")     
            else:
                await message.channel.send(f"\n{message.author.mention}に[鯖缶の呟き通知役職]をつけたよ(　•̀ω•́)و✧")   


        if message.content == "i)メンバー役職":
            role = message.guild.get_role(701963908461887568)
            m = message.guild.get_member(message.author.id)
            try:
                await m.add_roles(role)
            except:
                await message.channel.send("エラー出たw")     
            else:
                await message.channel.send(f"{message.author.mention}に[Member役職]をつけたよ(　•̀ω•́)و✧")  


        if message.content == "i)ヘルパー役職":
            role = message.guild.get_role(707305711813787699)
            m = message.guild.get_member(message.author.id)
            try:
                await m.add_roles(role)
            except:
                await message.channel.send("エラー出たw")     
            else:
                await message.channel.send(f"\n{message.author.mention}に[ServerHelper役職]をつけたよ(　•̀ω•́)و✧")  


        if message.content == "i)thinking役職":
            await message.channel.send(f"thinking役職は封印済みです。\n218桁のコードを送信してください。")  


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

    except Exception as error:
        ERROR = str(error)
        embed = discord.Embed(
            description = ERROR,
            color = discord.Color.red())
        embed.add_field(
            name = "エラーが出たメッセージ",
            value = message.content)
        embed.timestamp = datetime.now(JST)
        await message.channel.send(embed = embed)
    else:
        pass
client.run(TOKEN)
