import discord
from discord.ext import commands
import os
import asyncio
import random
import urllib
from bs4 import BeautifulSoup
from urllib.request import Request
from urllib import parse
import bs4
import time

client = discord.Client()

owner = ['724769557759393837']


@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))


@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))
    while True:
        user = len(client.users)
        server = len(client.guilds)
        messages = ["제 접두사는 하루야 입니다!", "좋은 하루입니다 그렇게 생각하지 않나요 ?", "TEAM ML ", str(user) + "분이 저를 사용중입니다.",
                    str(server) + "개의 서버에 제가 일하고 있어요 ! "]
        for (m) in range(5):
            await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=messages[(m)],
                                                                                              type=discord.ActivityType.watching))
            await asyncio.sleep(4)


@client.event
async def on_message(message):
    if message.content == '하루야 안녕':
        await message.channel.send('네 안녕하세요? 무엇이든 물어보세요 😊')


@client.event
async def on_message(message):
    if message.content == '하루야 빠이':
        await message.channel.send('빠이 빠이 ! 🌈')


@client.event
async def on_message(message):
    if message.content == '하루야 ㅃ2':
        await message.channel.send('빠이 빠이 ! 🌈')


@client.event
async def on_message(message):
    if message.content == '하루야 잘가':
        await message.channel.send('빠이 빠이 ! 🌈')


@client.event
async def on_message(message):
    if message.content == '하루야 꺼져':
        await message.channel.send('뭐죠? 기분이 나쁘네요 😓 우리 좋게 말해요 :) ')


@client.event
async def on_message(message):
    if message.content == '하루야 ㅎㅇ':
        await message.channel.send('하이하이 ! 📢 ')


@client.event
async def on_message(message):
    if message.content == '하루야 하이':
        await message.channel.send('하이하이 ! 📢 ')


@client.event
async def on_message(message):
    if message.content == '하루야 하잉':
        await message.channel.send('하이하이 ! 📢 ')


@client.event
async def on_message(message):
    if message.content == '하루야 헬로':
        await message.channel.send('하이하이 ! 📢 ')

    if message.content == '하루야 봇정보':
        user = len(client.users)
        server = len(client.guilds)
        embed = discord.Embed(title="📘ㅣ하루 정보 ", timestamp=message.created_at,
                              colour=discord.Colour.green()
                              )
        embed.add_field(name="개발 언어", value="Python", inline=False)
        embed.add_field(name="개발 시작 일자", value="2020. 9 . 9", inline=False)
        embed.add_field(name="서버 수", value=str(server), inline=False)
        embed.add_field(name="유저 수", value=str(user), inline=False)
        embed.add_field(name="개발자 나이", value="초등학교 4학년, inline=False)
        await message.channel.send(embed=embed)

        if message.content.startswith("하루야 eval"):
            if
        message.author.id in owner:
        a = message.content[6:]

        if message.content in ['output', 'token', 'file=', 'os', 'logout', 'login', 'quit', 'exit', 'sys', 'shell',
                               'dir']:
            embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
        embed.add_field(name="Error!", value=f'{message.content} 그 명령어는 금지된 단어가 포함되어있습니다.', inline=True)
        embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        return None

        try:
            msg = await message.channel.send(
                embed=discord.Embed(color=0x85CFFF, title="evaling...", description=f"""📥INPUT📥
    ```py
    {a}
    ```
    📤OUTPUT📤
    ```py
    evaling...
    ```"""))
            aa = await eval(a)
        except Exception as e:
            await msg.edit(embed=discord.Embed(color=0x85CFFF, title="eval", description=f"""📥INPUT📥

    ```py
    {a}          
    ```
    📤OUTPUT📤
    ```py
    {e}
    ```"""))
            try:
                aa = eval(a)
            except Exception as e:
                await msg.edit(embed=discord.Embed(color=0x85CFFF, title="eval", description=f"""📥INPUT📥

    ```py
    {a}
    ```
    📤OUTPUT📤
    ```py
    {e}
    ```"""))
            else:
                await msg.edit(embed=discord.Embed(color=0x85CFFF, title=f"eval", description=f"""📥INPUT📥
    ```py
    {a}
    ```
    📤OUTPUT📤
    ```py
    {aa}
    ```"""))
        else:
            await msg.edit(embed=discord.Embed(color=0x85CFFF, title="eval", description=f"""📥INPUT📥
    ```py
    {a}
    ```
    📤OUTPUT📤
    ```py
    {aa}
    ```"""))
    else:
        await message.channel.send("권환이 부족해요! 흐억 권환이 어딨는지 찾아봐요 🔰")


@client.event
async def on_member_join(member):
    syschannel = member.guild.system_channel.id
    try:
        embed = discord.Embed(
            title=f'멤버 입장',
            description=f'{member}님이{member.guild}에 입장 했습니다. 다들 환영해주세요 ! \n현재 서버 인원수: {str(len(member.guild.members))}명입니다! 와 대단해요 !',
            colour=0x00ff00
        )
        embed.set_thumbnail(url=member.avatar_url)
        await client.get_channel(syschannel).send(embed=embed)
    except:
        return None


@client.event
async def on_member_remove(member):
    syschannel = member.guild.system_channel.id
    try:
        embed = discord.Embed(
            title=f'멤버 퇴장',
            description=f'{member}님이{member.guild}에 나갔어요! 왜 나가요! .\n현재 서버 인원수: {str(len(member.guild.members))}명으로 줄었어요 😓',
            colour=discord.Colour.red()
        )
        embed.set_thumbnail(url=member.avatar_url)
        await client.get_channel(syschannel).send(embed=embed)
    except:
        return None


@client.event
async def on_message(message):
    if message.content.startswith("하루야 핑"):
        la = client.latency
        embed = discord.Embed(title="팡팡!")
        embed.add_field(name="반응 속도", value=str(round(la * 1000)) + "ms")
        embed.set_footer(text=message.author.name + " | 와 좋고 좋았어요 ! 😊 ", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith('하루야 정보'):
        print(f'{message.guild.name}/{message.author} (' + f'{message.author.id}) : {message.content}')
        user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
        roles = [role for role in user.roles]
        embed = discord.Embed(colour=user.color, timestamp=message.created_at)
        embed.set_author(name=f"{user}님의 정보!")
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text=f"{message.author}님에 정보를 깨짐 발생 인식 되지 않게 가져왔어요 :)ㅌ.", icon_url=message.author.avatar_url)
        embed.add_field(name="ID", value=user.id, inline=False)
        embed.add_field(name="닉네임", value=user.display_name, inline=False)
        embed.add_field(name="계정 생성 시간", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name="가입 시간", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
        embed.add_field(name=f"소유한 역할 ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=False)
        embed.add_field(name="가장 높은등급인 역할", value=user.top_role.mention, inline=False)
        embed.add_field(name="상태", value=user.status, inline=False)
        await message.channel.send(embed=embed)

    if (message.content.split(" ")[0] == "하루야 밴"):
        if (message.author.guild_permissions.ban_members):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                reason = message.content[22:]
                if (len(message.content.split(" ")) == 2):
                    reason = "None"
                await user.send(embed=discord.Embed(title="💥 당신은 이 컴퓨터로 이제 차단당한 서버에 못 들어갑니다.",
                                                    description=f'당신은 **{message.guild.name}** 서버에서 IP차단을 하였습니다. 사유는 다음과 같습니다. ```{reason}```',
                                                    color=0xff0000))
                await user.ban(reason=reason)
                await message.channel.send(embed=discord.Embed(title="ip Ban Success",
                                                               description=f"{message.author.mention} 님, 성공적으로 차단했어요 IP 차단이 됬어요. 사유:```{reason}```",
                                                               color=0x00ff00))
            except Exception as e:
                await message.channel.send(
                    embed=discord.Embed(title="❌ 에러 발생 에러는 하루 사이트에서 볼 수 있어요", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="⚡ 권한 부족 ⚡",
                                                           description=message.author.mention + "님은 유저를 차단할 수 있어요 :( 할려면 최소 ``**관리자**`` 가 켜저 있어야해요",
                                                           color=0xff0000))
            return

    if message.content == '하루야 서버정보':
        rnrrk = message.guild.region
        print(message.guild.region)
        embed = discord.Embed(colour=0x85CFFF, timestamp=message.created_at, title=f"{message.guild.name}")
        embed.set_thumbnail(url=message.guild.icon_url)
        embed.add_field(name="서버 이름", value=message.guild.name, inline=False)
        embed.add_field(name="서버 ID", value=message.guild.id, inline=False)
        embed.add_field(name="서버 국가", value=rnrrk, inline=False)
        embed.add_field(name="서버 Owner", value=f'<@{message.guild.owner.id}>', inline=False)
        embed.add_field(name="서버 Owner ID", value=message.guild.owner.id, inline=False)
        embed.add_field(name="서버 멤버 수",
                        value=f'{len(message.guild.members)}명 (봇 : {len(list(filter(lambda x: x.bot, message.guild.members)))}명 | 유저 : {len(list(filter(lambda x: not x.bot, message.guild.members)))}명)',
                        inline=False)
        embed.add_field(name="서버 채널 수",
                        value=f'전체 채널: {len(message.guild.channels)}개 (채팅채널 : {len(message.guild.text_channels)}개 | 음성채널 : {len(message.guild.voice_channels)}개 | 카테고리 : {len(message.guild.categories)}개)',
                        inline=False)
        embed.add_field(name="서버 부스트 레벨", value=f'{message.guild.premium_tier}레벨', inline=False)
        embed.add_field(name="서버 부스트 횟수", value=f'{message.guild.premium_subscription_count}번', inline=False)
        if message.guild.afk_channel != None:
            embed.add_field(name=f'잠수 채널',
                            value=f'<#{message.guild.afk_channel.id}> \n ( 시간 제한 : {message.guild.afk_timeout} 초 )',
                            inline=False)
        else:
            embed.add_field(name="잠수 채널", value="잠수 채널이 없습니다.")
        if message.guild.system_channel != None:
            embed.add_field(name=f'시스템 채널', value=f'<#{message.guild.system_channel.id}>', inline=False)
        else:
            embed.add_field(name="잠수 채널", value="시스템 채널이 없습니다.")
        embed.set_footer(text=f"{message.author}, 인증됨 | 준홍봇님의 코드를 참고했어요!", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("하루야 계산"):
        global calcResult
        param = message.content.split()
        try:
            if param[1].startswith("더하기"):
                calcResult = int(param[2]) + int(param[3])
                if calcResult < 1000000000:
                    embed = discord.Embed(title="하루에 결과 : 계산 더하기 결과 ",
                                          description="계산 결과는 [ " + str(calcResult) + " ] 인것 같아요!")
                    await message.channel.send(embed=embed)
                elif calcResult >= 1000000000:
                    embed = discord.Embed(title="하루의 에러 : 계산 더하기 결과 ",
                                          description="계산 결과가 [ 1, 000, 000, 000 ] 을 넘었어요!",
                                          timestamp=message.created_at,
                                          colour=discord.Colour.red()
                                          )
                    await message.channel.send(embed=embed)
            if param[1].startswith("빼기"):
                calcResult = int(param[2]) - int(param[3])
                if calcResult < 100000000:
                    embed = discord.Embed(title="하루에 결과 : 계산 빼기 결과 ",
                                          description="계산 결과는 [ " + str(calcResult) + " ] 인것 같아요!")
                    await message.channel.send(embed=embed)
                elif calcResult >= 100000000:
                    embed = discord.Embed(title="하루의 에러 : 계산 빼기 결과 ", description="계산 결과가 [ 100, 000, 000 ] 을 넘었어요!",
                                          timestamp=message.created_at,
                                          colour=discord.Colour.red()
                                          )
                    await message.channel.send(embed=embed)
            if param[1].startswith("곱하기"):
                calcResult = int(param[2]) * int(param[3])
                if calcResult < 10000000000:
                    embed = discord.Embed(title="하루에 결과 : 계산 곱하기 결과 ",
                                          description="계산 결과는 [ " + str(calcResult) + " ] 인것 같아요!")
                    await message.channel.send(embed=embed)
                elif calcResult >= 10000000000:
                    embed = discord.Embed(title="하루의 에러: 계산 곱하기 결과 ",
                                          description="계산 결과가 [ 10, 000, 000, 000 ] 을 넘었어요!",
                                          timestamp=message.created_at,
                                          colour=discord.Colour.red()
                                          )
                    await message.channel.send(embed=embed)
            if param[1].startswith("나누기"):
                calcResult = int(param[2]) / int(param[3])
                if calcResult < 100000000:
                    embed = discord.Embed(title="하루에 결과: 계산 나누기 결과 ",
                                          description="계산 결과는 [ " + str(calcResult) + " ] 인것 같아요!")
                    await message.channel.send(embed=embed)
                elif calcResult >= 100000000:
                    embed = discord.Embed(title="하루의 에러 : 계산 나누기 결과 에러 삐빅 🚫 ",
                                          description="계산 결과가 [ 100, 000, 000 ] 을 넘었어요! ", timestamp=message.created_at,
                                          colour=discord.Colour.red()
                                          )
                    await message.channel.send(embed=embed)
        except IndexError:
            embed = discord.Embed(title="하루 : 계산 오류", description="2개의 숫자가 포함되지 않았어요!", timestamp=message.created_at,
                                  colour=discord.Colour.dark_red()
                                  )
            await message.channel.send(embed=embed)
        except ValueError:
            await message.channel.send("숫자로 넣어주세요.")
        except ZeroDivisionError:
            await message.channel.send("You can't divide with 0.")

    if (message.content.split(" ")[0] == "젤로야 킥"):
        if (message.author.guild_permissions.kick_members):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][2:20]))
                reason = message.content[22:]
                if (len(message.content.split(" ")) == 2):
                    reason = "None"
                await user.send(embed=discord.Embed(title="💥 서버 추방",
                                                    description=f'당신은 **{message.guild.name}** 서버에서 추방되었습니다. 다시 링크를 찾으셨다면 들어가실수 있습니다. 사유는 다음과 같습니다. ```{reason}```',
                                                    color=0xff0000))
                await user.kick(reason=reason)
                await message.channel.send(embed=discord.Embed(title="Kick Success",
                                                               description=f"{message.author.mention} 님, 성공적으로 추방시켰습니다. 사유:```{reason}```",
                                                               color=0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="❌ 에러 발생", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(
                embed=discord.Embed(title="⚠ 권한 부족", description=message.author.mention + "님은 유저를 추방할 수 있는 권한이 없습니다.",
                                    color=0xff0000))
            return

    if message.content.startswith('하루야 가위바위보'):
        m = await message.channel.send(f"<@{message.author.id}>\n 안내면 진다 가위바위보 ! ")
        await m.add_reaction('✌')
        await m.add_reaction('✊')
        await m.add_reaction('🖐')
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=20,
                                                   check=lambda reaction, user: user == message.author and str(
                                                       reaction.emoji) in ['✌', '✊', '🖐'])
        except asyncio.TimeoutError:
            await message.channel.send(f'<@{message.author.id}>\n 왜 않내요! 와 어쨋든 제가 승리했네요 😊')
        else:
            if str(reaction.emoji) == "✌":
                a = ['가위', '보', '바위']
                c = random.choice(a)
                if c == '가위':
                    embed = discord.Embed(title=f"와 아까워..", color=0xe4f05a, timestamp=message.created_at)
                    embed.add_field(name=f"제작자 FOR#1234", value=f"가위✌", inline=True)
                    embed.add_field(name=f"{message.author}", value=f"가위✌", inline=True)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                if c == '보':
                    embed = discord.Embed(title=f"{message.author} 흐억 지다니..", color=0xff00,
                                          timestamp=message.created_at)
                    embed.add_field(name=f"제작자 FOR#1234", value=f"보🤚", inline=True)
                    embed.add_field(name=f"{message.author}", value=f"가위✌", inline=True)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                if c == '바위':
                    embed = discord.Embed(title=f"{message.author}와! 이겼다 ! 너무 못해요 저랑은 상대하면 안되겠는데요?",
                                          color=discord.Colour.red(), timestamp=message.created_at)
                    embed.add_field(name=f"제작자 FOR#1234", value=f"바위✊", inline=True)
                    embed.add_field(name=f"{message.author}", value=f"가위✌", inline=True)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
            elif str(reaction.emoji) == "✊":
                a = ['가위', '보', '바위']
                c = random.choice(a)
                if c == '가위':
                    embed = discord.Embed(title=f"{message.author} 흐억 지다니", color=0xff00, timestamp=message.created_at)
                    embed.add_field(name=f"하루", value=f"가위✌", inline=True)
                    embed.add_field(name=f"{message.author}", value=f"바위✊", inline=True)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                if c == '보':
                    embed = discord.Embed(title=f"{message.author} 하하 ! 제가 이겼네요 너무 못 하세요!", color=discord.Colour.red(),
                                          timestamp=message.created_at)
                    embed.add_field(name=f"하루", value=f"보🤚", inline=True)
                    embed.add_field(name=f"{message.author}", value=f"바위✊", inline=True)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                if c == '바위':
                    embed = discord.Embed(title=f"아깝게 비겼네요..", color=0xe4f05a, timestamp=message.created_at)
                    embed.add_field(name=f"하루", value=f"바위✊", inline=True)
                    embed.add_field(name=f"{message.author}", value=f"바위✊", inline=True)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
            elif str(reaction.emoji) == "🖐":
                a = ['가위', '보', '바위']
                c = random.choice(a)
                if c == '가위':
                    embed = discord.Embed(title=f"{message.author} 와 ! 이겼다 너무 못하시는거 아니예요? 크크",
                                          color=discord.Colour.red(), timestamp=message.created_at)
                    embed.add_field(name=f"하루", value=f"가위✌", inline=True)
                    embed.add_field(name=f"{message.author}", value=f"보🤚", inline=True)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                if c == '보':
                    embed = discord.Embed(title=f"아깝게 비겼군", color=0xe4f05a, timestamp=message.created_at)
                    embed.add_field(name=f"하루", value=f"보🤚", inline=True)
                    embed.add_field(name=f"{message.author}", value=f"보🤚", inline=True)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                if c == '바위':
                    embed = discord.Embed(title=f"{message.author} 흐엉 ㅠ 내가 지다니..", color=0xff00,
                                          timestamp=message.created_at)
                    embed.add_field(name=f"하루", value=f"바위✊", inline=True)
                    embed.add_field(name=f"{message.author}", value=f"보🤚", inline=True)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)