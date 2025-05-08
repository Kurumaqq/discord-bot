
import discord
from discord import AuditLogAction
from discord.utils import utcnow
from asyncio import sleep
from datetime import timedelta
from config import TRIGER_ACTION, SERVER_ID, TOKEN, ADMIN_ROLE
intents = discord.Intents.default()
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)

async def add_admin_role(client : discord.Client, user_id : int, timer: int):
    for guild in client.guilds:
        if guild.id == SERVER_ID:
            for user in guild.members:
                if user.id == user_id:
                    for i in range(1, timer+1):
                        role = discord.utils.get(guild.roles, name=f'{ADMIN_ROLE} ({i})')
                        await user.add_roles(role)
                        await sleep(1)
                        await user.remove_roles(role)
                    role = discord.utils.get(guild.roles, name=ADMIN_ROLE)
                    await user.add_roles(role)


async def management_admin(client : discord.Client):
    while True:
        await sleep(0.5)
        guild = client.get_guild(SERVER_ID)  # Получаем гильдию напрямую
        if not guild:
            continue

        async for entry in guild.audit_logs(limit=20):  # Увеличиваем лимит
            if (utcnow() - entry.created_at) > timedelta(seconds=0.7):
                continue  # Пропускаем старые события
            
            if entry.user.id == 1369303169804271696:  # ID бота (если нужно игнорировать его)
                continue

            print(f"{entry.user} совершил действие: {entry.action} на {entry.target}")
            role = discord.utils.get(guild.roles, name=ADMIN_ROLE)
            await entry.user.remove_roles(role)
            await sleep(15)
            await entry.user.add_roles(role)
                    

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await management_admin(client)


client.run(TOKEN)