# 파이썬의 기본 내장 함수가 아닌 다른 함수 혹은 다른 기능이 필요할 때 사용함
import discord, asyncio, datetime, pytz

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("떼빙알림 봇")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("도움말"))

@client.event
async def on_message(message):
    if message.content == "테스트": # 메세지 감지
        await message.channel.send ("봇이 정상작동중 입니다.".format(message.author, message.author.mention))

    if message.content == "떼빙알림": # 메세지 감지
        embed = discord.Embed(title="떼빙알림", description="2021년 9월 3일 떼빙",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0100FF)
       
        embed.add_field(name="서버/집결지", value="SGP Simulation / 뒤스부르크 차고지", inline=False)
        embed.add_field(name="집결/출발 시간", value="오후 8시 10분 / 오후 8시 30분", inline=False)
        embed.add_field(name="경로길이", value="1,518km", inline=False)
        embed.add_field(name="출발지", value="뒤스부르크 차고지", inline=False)
        embed.add_field(name="1차 경유지", value="칼레 정비소", inline=False)
        embed.add_field(name="2차 경유지", value="뒤스부르크 주유소", inline=False)
        embed.add_field(name="목적지", value="영국 도버 항구", inline=False)
        embed.add_field(name="출발순서", value="Jeep > KTM > Hyundai > LoveWay > LIFΣ > KEColud", inline=False)

        embed.set_footer(text="Bot Made by. Jeongyeon #7777", icon_url="https://cdn.discordapp.com/attachments/883209993745227837/883245242684416080/e7085a86467b4adb.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883209993745227837/883245242684416080/e7085a86467b4adb.jpg")
        await message.channel.send (embed=embed)

    if message.content == "공지사항": # 메세지 감지
        embed = discord.Embed(title="떼빙 주의사항", description="아래의 사항들은 꼭 지켜주시기 바랍니다.",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)  

        embed.add_field(name="주의사항", value="●최소 출발 10분전까지는 집결해주시기 바랍니다.\n●떼빙 진행중 경광등 및 채팅도배는 자제 바랍니다.\n●떼빙중 경적 및 에어혼 사용은 자제 바랍니다.\n●스코다(TMP차량)는 사용 금지 입니다.\n●더블 및 트리플 트레일러는 사용 금지 입니다.\n●멀티핑, PC가 좋지 않은분들은 맨뒤로 이동하여 참여 바랍니다.\n●떼빙 진행간에 고의보복, 트롤, 위협등은 금지 합니다.", inline=False)

        embed.set_footer(text="Bot Made by. Jeongyeon #7777", icon_url="https://cdn.discordapp.com/attachments/883209993745227837/883245242684416080/e7085a86467b4adb.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883209993745227837/883245242684416080/e7085a86467b4adb.jpg") 
        await message.channel.send (embed=embed)

    if message.content == "떼빙경로": # 메세지 감지
        embed = discord.Embed(title="떼빙경로", description="2021년 9월 3일 떼빙 경로",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xFF0000)
       
        embed.add_field(name="전체경로", value="1,518km", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/883209993745227837/883291844455317514/28b54876d6c5d7fe.png")
        
        embed.set_footer(text="Bot Made by. Jeongyeon #7777", icon_url="https://cdn.discordapp.com/attachments/883209993745227837/883245242684416080/e7085a86467b4adb.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883209993745227837/883245242684416080/e7085a86467b4adb.jpg")
        await message.channel.send (embed=embed)    

    if message.content == "집결지": # 메세지 감지
        embed = discord.Embed(title="집결지", description="2021년 9월 3일 떼빙 집결지",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xFF8224)
       
        embed.add_field(name="집결지", value="뒤스부르크 차고지", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/883293942483935312/883300989686386728/7c5e6768c3ae119d.png")
        
        embed.set_footer(text="Bot Made by. Jeongyeon #7777", icon_url="https://cdn.discordapp.com/attachments/883209993745227837/883245242684416080/e7085a86467b4adb.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883209993745227837/883245242684416080/e7085a86467b4adb.jpg")
        await message.channel.send (embed=embed)      

    if message.content == "1차경유지": # 메세지 감지
        embed = discord.Embed(title="1차경유지", description="2021년 9월 3일 떼빙 1차 경유지",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x7ED2FF)
       
        embed.add_field(name="1차경유지", value="칼레 정비소", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/883293942483935312/883304582153916456/1.png")
        
        embed.set_footer(text="Bot Made by. Jeongyeon #7777", icon_url="https://cdn.discordapp.com/attachments/883209993745227837/883245242684416080/e7085a86467b4adb.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883209993745227837/883245242684416080/e7085a86467b4adb.jpg")
        await message.channel.send (embed=embed)      

    if message.content == "2차경유지": # 메세지 감지
        embed = discord.Embed(title="2차경유지", description="2021년 9월 3일 떼빙 2차 경유지",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x7ED2FF)
       
        embed.add_field(name="2차경유지", value="뒤스부르크 주유소", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/883293942483935312/883305846308737044/2.png")
        
        embed.set_footer(text="Bot Made by. Jeongyeon #7777", icon_url="https://cdn.discordapp.com/attachments/883209993745227837/883245242684416080/e7085a86467b4adb.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883209993745227837/883245242684416080/e7085a86467b4adb.jpg")
        await message.channel.send (embed=embed)   
        
    if message.content == "최종목적지": # 메세지 감지
        embed = discord.Embed(title="최종 목적지", description="2021년 9월 3일 떼빙 최종 목적지",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xFF8224)
       
        embed.add_field(name="최종 목적지", value="영국 도버 항구", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/883293942483935312/883308763728195625/b1ac64611792b9eb.png")    

        embed.set_footer(text="Bot Made by. Jeongyeon #7777", icon_url="https://cdn.discordapp.com/attachments/883209993745227837/883245242684416080/e7085a86467b4adb.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883209993745227837/883245242684416080/e7085a86467b4adb.jpg")
        await message.channel.send (embed=embed)     

    if message.content == "도움말": # 메세지 감지
       embed = discord.Embed(title="도움말", description="떼빙알림봇 도움말",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x0100FF)
       
       embed.add_field(name="도움말", value="봇사용 도움말을 봅니다.", inline=False)
       embed.add_field(name="테스트", value="봇이 정상작동하는지 확인 합니다.", inline=False)
       embed.add_field(name="떼빙알림", value="떼빙정보를 확인 합니다.", inline=False)
       embed.add_field(name="공지사항", value="떼빙 주의사항을 확인 합니다.", inline=False)
       embed.add_field(name="떼빙경로", value="떼빙경로를 확인 합니다.", inline=False)
       embed.add_field(name="집결지", value="떼빙 집결지를 확인 합니다.", inline=False)
       embed.add_field(name="1차경유지", value="떼빙 1차 경유지를 확인 합니다.", inline=False)
       embed.add_field(name="2차경유지", value="떼빙 2차 경유지를 확인 합니다.", inline=False)
       embed.add_field(name="최종목적지", value="떼빙 최종 목적지를 확인 합니다.", inline=False)

       embed.set_footer(text="Bot Made by. Jeongyeon #7777", icon_url="https://cdn.discordapp.com/attachments/883209993745227837/883245242684416080/e7085a86467b4adb.jpg")
       embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883209993745227837/883245242684416080/e7085a86467b4adb.jpg")
       await message.channel.send (embed=embed)           

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('ODgzMjIzMzg0MzY2OTM2MTA0.YTGz4A.h4qoBUtbxMed4XTXTU31U7uVHnQ')