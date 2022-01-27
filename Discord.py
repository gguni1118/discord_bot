from email import message
from bs4 import BeautifulSoup
import discord
import asyncio
import time
import random
import datetime
from httpx import request
import pytz
from discord.ext import commands
from youtube_dl import YoutubeDL
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord.player import FFmpegPCMAudio
import googletrans
from googletrans import Translator
from googletrans.constants import LANGCODES, LANGUAGES
from googletrans.models import Detected
import sys
from exitstatus import ExitStatus
from discord.channel import VoiceChannel
import html
import urllib.request
from google.cloud import texttospeech
import hgtk
import pandas as pd
from urllib.request import Request, urlopen

chaton = True #setup
adminlist = ['']
user = 0
history = []
playing = True
blacklist = ['즘', '틱', '늄', '슘', '퓸', '늬', '뺌', '섯', '숍', '튼', '름', '늠', '쁨']
translator = Translator()
sgame = False
path = "cromedriver.exe"
fuck = True
numud = 0
list_fuck = ['ㅗ', 'eeeee', '십알', 'ㅈㄹ', 'ㅅㅂ', 'ㅅ1ㅂ', '시1발', 'ㅄ', '지랄', '씨발', '또라이', '적출', '니미', '매도', '병신', '좆', '버러지', '니엄마', '시11발', '주식', '느금마', '새끼', '주식', '애미', '매입', '시발']
song_tkdtn = "https://www.youtube.com/watch?v=wbHweCdCRQE"
prefix = "!" #접두사
ranud = 0
nums = []
cb = False
wt = False
c = 1
detfuck = False
adminsay = 0
admincheck = 0
admin = []
wtm = False
admin_1 = 0
admin_2 = 0
admin_3 = 0
admin_4 = 0
bothap = 0
driver = webdriver.Chrome("chromedriver.exe")
hook = 0
money = 10000

client = discord.Client()

bot = commands.Bot(command_prefix='!')

token = "OTMxNzQ0MzMzOTkwODU4Nzcz.YeI4iA.jgxBWGb0BNMLKKlwljeWojhCC0g"

voiceChannel: VoiceChannel

if chaton == True:

    @client.event #start
    async def on_ready():
    
        print(client.user.name)
        print('Logged in!')
        game = discord.Game('해당 봇은 공식 봇이 아닙니다 !         ')
        await client.change_presence(status=discord.Status.online, activity=game)
    
    @client.event #command
    async def on_message(message):
        global admincheck
        global c
        global cb
        global voiceChannel
        global prefix
        global ranud
        global user
        global hook
        global sgame
        global wt
        global detfuck
        global bothap
        global money
        if message.content == prefix + "봇":
            await message.channel.send("[!] 현재 봇 상태는 원활 합니다")
            
        if message.content.startswith (prefix + "코로나"):
            print('  ○>> #오늘의 #국내 #코로나19 #현황 \n')
            webpage = urllib.request.urlopen('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98')
            soup = BeautifulSoup(webpage, 'html.parser')
            cph = "https://ifh.cc/g/LHu1Cb.jpg"
            dayconfirm = soup.find('p',"info_num")
            embed = discord.Embed(title="[⚔ 코로나 현황 ⚔]", description="COVID-19", color=0x00ff00)
            embed.add_field(name="일일 확진", value=str(dayconfirm.get_text()) + "명", inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            embed.set_thumbnail(url=cph)
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "날씨"):
            setplace = message.content[4:]
            weatherurl = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=" + setplace +"+날씨"
            soup = BeautifulSoup(weatherurl, 'html.parser')
            placeweather = soup.find('span', "blind")
            embed = discord.Embed(title="[ WEATHER ]", description="INFO", color=0x00ff00)
            embed.add_field(name="현재 " + setplace + " 날씨", value=str(placeweather.get_text()) + "°C", inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
        
        if message.content.startswith (prefix + "날씨"):
            weatherurl = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=시흥+날씨"
            soup = BeautifulSoup(weatherurl, 'html.parser')
            placeweather = soup.find('strong')
            embed = discord.Embed(title="[ WEATHER ]", description="INFO", color=0x00ff00)
            embed.add_field(name="현재 " + setplace + " 날씨", value=str(placeweather.get_text()) + "°C", inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "코인"):
            webpage = urllib.request.urlopen('https://www.google.com/search?q=%EB%8F%84%EC%A7%80%EC%BD%94%EC%9D%B8&ei=gB_xYZGoNtLf2roPvuCiuA4&ved=0ahUKEwiR6NH3l8_1AhXSr1YBHT6wCOcQ4dUDCA4&uact=5&oq=%EB%8F%84%EC%A7%80%EC%BD%94%EC%9D%B8&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHkoECEEYAEoECEYYAFAAWM8EYL8FaAFwAngBgAGDAYgB9QKSAQMwLjOYAQCgAQHAAQE&sclient=gws-wiz')
            soup = BeautifulSoup(webpage, 'html.parser')
            dogecoin = soup.find('span', "pclqee")
            dogecoinup = soup.find('span', "D3VPPe")
            embed = discord.Embed(title="[ DOGECOIN ]", description="DOGE", color=0x00ff00)
            embed.add_field(name="현재 도지코인 가격", value=str(dogecoin.get_text()) + "KRW", inline=False)
            embed.add_field(name="DGC", value=str(dogecoinup.get_text()), inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "로또"):
            lotto1 = random.randint(1,45)
            lotto2 = random.randint(1,45)
            lotto3 = random.randint(1,45)
            lotto4 = random.randint(1,45)
            lotto5 = random.randint(1,45)
            lotto6 = random.randint(1,45)
            if lotto1 == lotto2:
                lotto2 = random.randint(1,45)
            if lotto1 == lotto3:
                lotto3 = random.randint(1,45)
            if lotto1 == lotto4:
                lotto4 = random.randint(1,45)
            if lotto1 == lotto5:
                lotto5 = random.randint(1,45)
            if lotto1 == lotto6:
                lotto6 = random.randint(1,45)
            if lotto2 == lotto3:
                lotto3 = random.randint(1,45)
            if lotto2 == lotto4:
                lotto4 = random.randint(1,45)
            if lotto2 == lotto5:
                lotto5 = random.randint(1,45)
            if lotto2 == lotto6:
                lotto6 = random.randint(1,45)
            if lotto3 == lotto4:
                lotto4 = random.randint(1,45)
            if lotto3 == lotto5:
                lotto5 = random.randint(1,45)
            if lotto3 == lotto6:
                lotto6 = random.randint(1,45)
            if lotto4 == lotto5:
                lotto5 = random.randint(1,45)
            if lotto4 == lotto6:
                lotto6 = random.randint(1,45)
            if lotto5 == lotto6:
                lotto6 = random.randint(1,45)
            embed = discord.Embed(title="[ LOTTO ]", description="LOTTO", color=0x00ff00)
            embed.add_field(name="첫번째", value="||" + str(lotto1) + "||", inline=True)
            embed.add_field(name="두번째", value="||" + str(lotto2) + "||", inline=False)
            embed.add_field(name="세번째", value="||" + str(lotto3) + "||", inline=True)
            embed.add_field(name="네번째", value="||" + str(lotto4) + "||", inline=False)
            embed.add_field(name="다섯번째", value="||" + str(lotto5) + "||", inline=True)
            embed.add_field(name="여섯번째", value="||" + str(lotto6) + "||", inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "롣도"):
            webpage = urllib.request.urlopen('https://dhlottery.co.kr/gameResult.do?method=byWin')
            soup = BeautifulSoup(webpage, 'html.parser')
            befor = soup.find_all('span', "ball_645 lrg ball1")
            for befor in soup.find_all('span', "ball_645 lrg ball1"):
                before = befor.get_text()
            for befor1 in soup.find_all('span', "ball_645 lrg ball2"):
                before1 = befor1.get_text()
            before2 = soup.find('span', "ball_645 lrg ball3")
            round1 = soup.find("strong")
            embed = discord.Embed(title="[" + str(round1) + " 회차" + "]", description="LOTTO", color=0x00ff00)
            embed.add_field(name="로또", value=str(before) + str(before1) + str(before2.get_text()), inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "s"):
            embed = discord.Embed(title="[ GAME ]", description="GAME-01", color=0x00ff00)
            embed.add_field(name="START", value="게임을 시작합니다\n!g n/n으로 진행하세요", inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            time.sleep(1)
            await message.channel.send("🔠1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣\n🇦🟨🟨🟨🟨🟨🟨🟨\n🇧🟨🟨🟨🟨🟨🟨🟨\n🇨🟨🟨🟨🟨🟨🟨🟨\n🇩🟨🟨🟨🟨🟨🟨🟨\n🇪🟨🟨🟨🟨🟨🟨🟨\n🇫🟨🟨🟨🟨🟨🟨🟨")
            sgame = True
            
        if message.content.startswith (prefix + "g"):
            if sgame == True:
                play1 = message.content[3:3]
                play2 = message.content[5:5]
                if play1 == "a":
                    if play2 == 1:
                        await message.channel.send("🔠1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣\n🇦🟥🟨🟨🟨🟨🟨🟨\n🇧🟨🟨🟨🟨🟨🟨🟨\n🇨🟨🟨🟨🟨🟨🟨🟨\n🇩🟨🟨🟨🟨🟨🟨🟨\n🇪🟨🟨🟨🟨🟨🟨🟨\n🇫🟨🟨🟨🟨🟨🟨🟨")
            
        if message.content == prefix + "업초":
            s = 0
            m = 0
            h = 0
                
        if message.content.startswith == prefix + "중지":
            wt = False
            
        if message.content.startswith == prefix + "밴키":
            if detfuck != False:
                detfuck = False
                await message.channel.send("[!] 욕 감지를 종료합니다")
            elif detfuck == False:
                detfuck = True
                await message.channel.send("[!] 욕 감지를 시작합니다")
            
        if message.content.startswith ("ㅗ"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("십알"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("ㅈㄹ"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("ㅅㅂ"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("ㅅ1ㅂ"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("시1발"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("ㅄ"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("지랄"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("씨발"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("또라이"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("적출"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("니미"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("매도"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("병신"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("좆"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("버러지"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("니엄마"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("시11발"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("주식"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("느금마"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("개새끼"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("주식"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("애미"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
        if message.content.startswith ("시발"):
            embed = discord.Embed(title="[!] 욕설이 감지되었습니다", description=message.author.mention,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            await message.delete()
                                    
        if message.content == prefix + "도배":
            await message.channel.send("시룬뎁 :(")
            
        if message.content.startswith (prefix + "아이디"):
            id = message.author.id
            embed = discord.Embed(title="[!] 아이디", description="<@"+str(id)+"> 당신의 아이디가 맞는지 멘션으로 확인하세요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(id)
            await message.channel.send(embed=embed)
            
        if message.content.startswith ("Dev"):
            id = message.author.id
            if id == 931741804544532510:
                await message.channel.send("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B4%80%EB%A6%AC%EC%9E%90")

                        
        if message.content == prefix + "노래 명사수":
            await message.channel.send(song_tkdtn)
            
        if message.content == "d":
            print("d")
            
        if message.content.startswith (prefix + "청소"):
            i = (message.author.guild_permissions.administrator)

            if i is True:
                amount = message.content[4:]
                await message.channel.purge(limit=2)
                await message.channel.purge(limit=int(amount))

                embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
        
            if i is False:
                await message.channel.purge(limit=1)
                await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))
                
        if message.content == "-업다운":
            ranud = random.randint(1, 10)
            embed = discord.Embed(title="업다운", description="-업다운 n으로 게임을 진행하세요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            await message.channel.send (embed=embed)
            if message.content.startswith ("-업다운 "):
                updown = message.content[6:]
                await message.channel.send(limit=1)
                await message.channel.send(limit=int(updown))
                if updown < ranud:
                    await message.channel.send("up")
                elif updown > ranud:
                    await message.channel.send("up")
                elif updown == ranud:
                    embed = discord.Embed(title="업다운", description="정답입니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    await message.channel.send(embed=embed)
        
        if message.content == prefix + "뽑기":
            a = random.randint(0, 100)
            a += 1
            if a == 1:
                b = "당첨"
                embed = discord.Embed(title="뽑기 도박", description="당첨입니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            else:
                b = "꽝"
                embed = discord.Embed(title="뽑기 도박", description="꽝.. 다시 시도해봐요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
                
        if message.content.startswith (prefix + "인증 "):
            if message.author.guild_permissions.administrator:
                await message.delete()
                user = message.mentions[0]

                embed = discord.Embed(title="인증 시스템", description="인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
                embed.add_field(name="인증 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
                embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
                embed.set_footer(text="Bot Made by. Bot_Developer#4371")
                await message.author.send (embed=embed)
                role = discord.utils.get(message.guild.roles, name = '[멤버]')
                await user.add_roles(role)

            else:
                await message.delete()
                await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))
            
        if message.content == prefix + "off":
            await message.channel.send("OFF")
            chaton = False
            
        if message.content == prefix + "명령어":
            await message.channel.send("[ ! ] 현재, 명령어 종류입니다!\n\n" + "-명령어\n" + "명령어 목록을 가져옵니다\n\n" + "-봇\n" + "봇 작동 여부를 확인합니다\n\n" + "-뽑기\n" + "1%확률의 뽑기를 합니다\n\n" + "-")
        
        if message.content == prefix + "접두사 .":
            prefix = "."
            await message.channel.send("봇의 접두사를 " + prefix + " 로 바꿨습니다")
            print(prefix + " 현재 접두사 입니다!")
        
        if message.content == prefix + "접두사 !":
            prefix = "!"
            await message.channel.send("봇의 접두사를 " + prefix + " 로 바꿨습니다")
            print(prefix + " 현재 접두사 입니다!")
            
        if message.content == prefix + "접두사 -":
            prefix = "-"
            await message.channel.send("봇의 접두사를 " + prefix + " 로 바꿨습니다")
            print(prefix + " 현재 접두사 입니다!")
            
        if message.content.startswith (prefix + "코로나"):
            await message.channel.send("오늘 코로나 확진자수: ", sum(nums), "명")
            
        if message.content.startswith (prefix + "유튜브"):
            song = message.content[5:]
            embed = discord.Embed(title="[ 유튜브 ]", description="https://www.youtube.com/results?search_query=" + song,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="[ 명령어 ]", description="띄어쓰기가 있는 노래는 띄어쓰기 대신 + 로 표기해 주세요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "네이버"):
            naver = message.content[5:]
            navereplace = naver.replace(" ","+")
            embed = discord.Embed(title="[ 네이버 ]", description=naver + "의 네이버 검색 결과입니다" + naver,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.add_field(name="[ 검색 결과 ]", value = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=" + navereplace + ">)" + "를 클릭해 검색 결과로 이동하세요", inline=True)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content == "ㄷㅂㄱ":
            gambling = random.randint(1, 2000)
            money = int(money) + int(gambling)
            embed = discord.Embed(title="[ 돈 벌기 ]", description="카지노",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.add_field(name="[ 남은 돈 ]", value = str(money) + "원", inline = True)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            time.sleep(3)
            
        if message.content == "올인":
            gambling = random.randint(1, 5)
            if gambling == 1:
                money = int(money) * 100
                embed = discord.Embed(title="[ 도박 ]", description="성공",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.add_field(name="[ 남은 돈 ]", value = str(money) + "원", inline = True)
                embed.add_field(name="[ 배 ]", value = "100배", inline = True)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            else:
                money = 0
                embed = discord.Embed(title="[ 도박 ]", description="실패",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.add_field(name="[ 남은 돈 ]", value = str(money) + "원", inline = True)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            if money == 0:
                embed = discord.Embed(title="[ 도박 ]", description="돈 부족",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.add_field(name="[ 남은 돈 ]", value = str(money) + "원", inline = True)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            
        if message.content.startswith ("ㄷㅂ "):
            setmoney = message.content[3:]
            if int(setmoney) > int(money):
                await message.channel.send("[ ErRor - 1293 ] 돈 부족")
            if int(setmoney) < int(money):
                
                money = int(money) - int(setmoney)
                gambling = random.randint(1,20)
                if gambling < 10:
                    money = int(money) + int(setmoney) * int(gambling)
                    embed = discord.Embed(title="[ 도박 ]", description="성공",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.add_field(name="[ 남은 돈 ]", value = str(money) + "원", inline = True)
                    embed.add_field(name="[ 배 ]", value = str(gambling) + "배", inline = True)
                    embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                    await message.channel.send(embed=embed)
                else:
                    embed = discord.Embed(title="[ 도박 ]", description="실패",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.add_field(name="[ 남은 돈 ]", value = str(money) + "원", inline = True)
                    embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                    await message.channel.send(embed=embed)
                    
            
        if message.content.startswith (prefix + "구글"):
            google = message.content[4:]
            googlereplace = google.replace(" ","+")
            embed = discord.Embed(title="[ 구글 ]", description=google + "의 구글 검색 결과입니다",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.add_field(name="[ 검색 결과 ]", value = "[여기](<https://www.google.com/search?q=" + googlereplace + ">)" + "를 클릭해 검색 결과로 이동하세요", inline=True)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content == prefix + "어드민리스트":
            await message.channel.send(admin)
            
        if message.content == prefix + "인증":
            id = message.author.id
            user = message.author
            fp = random.randint(1, 9)
            sp = random.randint(1, 9)
            tp = random.randint(1, 9)
            pw = str(fp) + str(sp) + str(tp)
            print(pw)
            pwq = input(f"{user.name}님이 관리자 권한을 요청하셨습니다 허용하시겠습니까? (y, n)")
            if pwq == "y":
                admin.append(user.name)
                await message.channel.send(f"{user.display_name} 님이 새로운 관리자가 되셨습니다")

            elif pwq == "n":
                await message.channel.send(f"{user.display_name} 님의 관리자 인증 요청이 거부되었습니다")
            
        if message.content == prefix + "종료":
            proex = input("종료하시겠습니까? : ")
            if proex == "네":
                embed = discord.Embed(title="[ 봇 ]", description="종료합니다",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
                print(message.author.mention + "process excited by")
                sys.exit(ExitStatus.success)
            else:
                embed = discord.Embed(title="[ 봇 ]", description="종료를 거부하였습니다",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            
            
        if message.content.startswith (prefix + "tts"):
            mestts = message.content[5:]
            await message.channel.send(mestts, tts=True)
            
        if message.content == prefix + "욕":
            await message.channel.send("귀여운 DISCORD_BOT_001은 욕을 몰라서 못해요 ><")
        
        if message.content.startswith ("?"):
            hook += 1
            embed = discord.Embed(title="[ 갈고리 수집 ]", description=str("갈고리수집 : ") + str(hook),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content == "고?속":
            hook += 500
            embed = discord.Embed(title="[ 갈고리 수집 ]", description=str("갈고리수집 : ") + str(hook),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "멘도"):
            user = message.content[4:]
            wtm = True
            while wtm:
                i = 0
                await message.channel.send("[", i, "]",  "<@"+str(user)+">")
                i = i + 1
                
        if message.content == prefix + "중지":
            wtm = False
            
        if message.content.startswith ("야"):
            id = message.author.id
            embed = discord.Embed(title="[ 방장 호출 ]", description="<@"+str(id)+"> 님이 " + "<@"+str(931741804544532510)+"> 님을 호출하였습니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "따라해"):
            reply = message.content[5:]
            if reply.startswith("ㅗ"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("십알"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("ㅈㄹ"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("ㅅㅂ"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("ㅅ1ㅂ"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("ㅂㅅ"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("ㅄ"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("지랄"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("씨발"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("또라이"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("적출"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("니미"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("매도"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("병신"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("좆"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("버러지"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("느금마"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("니애미"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("니엄마"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("시11발"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("주식"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("개"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("새끼"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("주식"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("애미"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("매입"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif reply.startswith("시발"):
                embed = discord.Embed(title="[ 따라하기 ]", description="욕설은 따라할 수 없어요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(title="[ 따라하기 ]", description=reply,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
                
        if message.content.startswith (prefix + "임베드"):
            emti = message.content[5:]
            embed = discord.Embed(title="[ 임베드 ]", description=emti,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "디코"):
            searchroom = message.content[4:]
            embed = discord.Embed(title="[ 디스코드 ]", description="https://discord.com/guild-discovery?query=" + searchroom + "&offset=0&limit=12&preferredLocale=ko&categoryId=-1&tag=",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            embed = discord.Embed(title="[ 명령어 ]", description="띄어쓰기가 있는 검색어는 띄어쓰기 대신 + 로 표기해 주세요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "IP"):
            await message.channel.send("https://iplogger.org/2LHYf7")
            
        if message.content.startswith (prefix + "도배"):
            user = message.author
            if user.name in admin:
                wtf = message.content[4:]
                wt = True
            else:
                await message.channel.send("[!] 해당 명령어를 사용할 권한이 없습니다")
            
        if wt != False:
            if message.content != (prefix):
                while wt:
                    await message.channel.send(wtf)
                    await message.channel.send(wtf)
                
                
        if message.content == prefix:
            wt = False
            wtf = []
            
        if message.content.startswith (prefix + "번역"):
            langs = message.content[4:]
            langs = translator.translate(langs, src='ko', dest='en')
            embed = discord.Embed(title="[ Translator ]", description="[ Translator ] " + langs.text,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "번역"):
            langs = message.content[4:]
            langs = translator.translate(langs, src='ko', dest='en')
            embed = discord.Embed(title="[ Translator ]", description="[ Translator ] " + langs.text,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "trans"):
            langs = message.content[4:]
            langs = translator.translate(langs, src='en', dest='ko')
            embed = discord.Embed(title="[ Translator ]", description="[ Translator ]" + langs.text,timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content == prefix + "시작":
            ranud = random.randint(1, 1000)
            embed = discord.Embed(title="업다운", description="[ GAME ] 업다운 게임이 시작되었어요\n1~1000까지의 숫자 중 골라주세요",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            
        if message.content == prefix + "포기":
            ranud = 0
            udis = 0
            embed = discord.Embed(title="업다운", description="게임을 포기하셨습니다",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            await message.channel.send(embed=embed)
            time.sleep(1)
            
        if message.content == prefix + "정보":
            user = message.author
            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
            pfp = user.avatar_url
            id = message.author.id
            embed = discord.Embed(title=f"{user.display_name} 님의 유저 정보", description="INFORMATION", color=0x00ff00)
            embed.add_field(name="유저 태그", value=f"{user}", inline=False)
            embed.add_field(name="유저 이름", value=f"{user.name}", inline=False)
            embed.add_field(name="유저 가입일", value=f"{date.year}년 {date.month}월 {date.day}일", inline=False)
            embed.add_field(name="유저 아이디", value=f"{user.id}", inline=False)
            embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
            embed.set_thumbnail(url=pfp)
            await message.channel.send(embed=embed)
            
        if message.content.startswith ("몰?루"):
            pfp = "https://ifh.cc/g/fe7w3r.jpg"
            embed = discord.Embed(title="몰루티콘", description="몰?루", color=0x00ff00)
            embed.set_thumbnail(url=pfp)
            await message.delete()
            await message.channel.send(embed=embed)
            
        if message.content == prefix + "업타임":
            embed = discord.Embed(title="봇의 업타임 정보", description="INFORMATION", color=0x00ff00)
            embed.add_field(name="시간", value=h, inline=False)
            embed.add_field(name="분", value=m, inline=False)
            embed.add_field(name="초", value=s, inline=False)
            await message.channel.send(embed=embed)
            
        if message.content.startswith (prefix + "Ek "):
            Ek = message.content[4:]
            await message.channel.send(Ek)

        if message.content.startswith (prefix + "dm "):
            dmm = message.content[4:]
            dm = await message.author.create_dm()
            await dm.send("Bot이 보낸 메시지 : " + dmm)
            
        if message.content.startswith (prefix + "갠챗 "):
            dmm = message.content[4:]
            dm = await dmm.create_dm()
            sendm = input(dmm + " 님께 보낼 메시지를 입력해 주세요 - ")
            await dm.send("Bot이 보낸 메시지 : " + sendm)
            
        if message.content.startswith (prefix + "업다운 "):
            if ranud == 0:
                embed = discord.Embed(title="업다운", description="게임을 먼저 시작해주세요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif ranud != 0:
                udis = int(message.content[5:])
                if udis < ranud:
                    embed = discord.Embed(title="업다운", description="[ UP ] 정답이 아니에요",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                    await message.channel.send(embed=embed)
                    udis = 0
                elif udis > ranud:
                    embed = discord.Embed(title="업다운", description="[ DOWN ] 정답이 아니에요",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                    await message.channel.send(embed=embed)
                    udis = 0
                elif udis == ranud:
                    embed = discord.Embed(title="업다운", description="[ CORRECT ] " + message.author.mention + " 정답이에요!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                    await message.channel.send(embed=embed)
                    udis = 0
                    ranud = 0
                else:
                    embed = discord.Embed(title="업다운", description="[ ERROR ] ErRor_CoDE_1329",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                    embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                    await message.channel.send(embed=embed)
                    
        if message.content.startswith (prefix + '홀짝 '):
            evod = message.content[4:5]
            paymo = int(message.content[6:])
            money = money - paymo
            even = random.randint(1, 2)
            if even == 1:
                evodmo = "홀"
            if even == 2:
                evodmo = "짝"
            if evod == evodmo:
                money += paymo * 2
                embed = discord.Embed(title="홀짝도박", description="[ 성공 ] 홀짝도박에 성공하였습니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.add_field(name="남은 돈", value=f"{money}", inline=False)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
            elif evod != evodmo:
                embed = discord.Embed(title="홀짝도박", description="[ 실패 ] 홀짝도박에 실패하였습니다!",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
                embed.add_field(name="남은 돈", value=f"{money}", inline=False)
                embed.set_footer(text="Bot Made by. Bot_Developer #4371", icon_url="https://ifh.cc/g/cKAlOE.jpg")
                await message.channel.send(embed=embed)
                    
        if cb != False:
            if message.content != prefix + "시비중지":
                await message.channel.send("ㅋ")
                await message.channel.send("아무고토모타쥬?")
                
        if message.content == prefix + "시비털기":
            cb = True
            
        if message.content == prefix + "시비중지":
            cb = False
                 
elif chaton == False:
    @client.event #command
    async def on_message(message):
        await message.channel.send("현재는 봇 작동중이 아니에요!")
    
        if message.content == "-on": #hiden command
            await message.channel.send("ON")
            chaton = True
            
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
            
client.run(token)