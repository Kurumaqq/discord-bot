
import discord
import requests
from discord import AuditLogAction
from discord.utils import utcnow
from asyncio import sleep
from datetime import timedelta
from config import SERVER_ID, TOKEN, ADMIN_ROLE
from time import time
intents = discord.Intents.default()
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)
WEBHOOK_URL = "https://discord.com/api/webhooks/1370051294605217882/B2aSs07cXAncIztCjvWZJvHQIP0_9GgQeMh2NNZti9n3jOrBTPJF0l2LLw0OjNJ5sdF_"

                    

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel and after.channel and before.channel != after.channel:
        await sleep(1)
        
        async for entry in member.guild.audit_logs(
            limit=5,
            action=discord.AuditLogAction.member_disconnect
        ):
            guild = member.guild 
            role = discord.utils.get(guild.roles, name=ADMIN_ROLE)
            user = discord.utils.get(guild.members, name=entry.user.name)
            await user.remove_roles(role)
            await sleep(15)
            await user.add_roles(role)
            break

    if before.channel and not after.channel:
        await sleep(1)  # Ждём обновления аудит-лога
        
        async for entry in member.guild.audit_logs(
            limit=5, 
            action=discord.AuditLogAction.member_disconnect):

            print('12321')
            
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    # await management_admin(client)


client.run(TOKEN)