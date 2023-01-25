import discord
import asyncio

from discord.ext import commands

intents= discord.Intents.all()
client = commands.Bot(command_prefix ="!", intents=intents)
 
@client.event
async def on_ready():
    print('Olá, Mundo!')
    print('LANGOs BOT ONLINE')
    print('Bot interativo, para duvidas.')
    print(client.user.name)
    print(client.user.id)
    print('------------LANGO------------')

@client.event  
async def on_member_enter(member):
    serverchannel = member.server.defaut_channel
    message="Forte é a força em você. Um jedi um dia você sera".format(member.name)
    await client.send_message(serverchannel, message)

@client.event  
async def on_member_remove(member):
    serverchannel = member.server.defaut_channel
    message="Que a força esteja com você jovem PADAWAN. Adeus...".format(member.name)
    await client.send_message(serverchannel, message)



@client.event  
async def on_message(message):
    if message.content.lowet().startswith("!help"):
        await client.send_message(message.channel, "Estamos a procura de novos rebeldes para formar a nova Republica nos ajude a encontrar quem procuramos")
   
    if message.content.lowet().startswith("!OldRepublic"):
        await client.send_message(message.channel, "Old Republic foi um governo galáctico que existia antes do estabelecimento da República Galáctica")
    
    if message.content.lowet().startswith("!Lango"):
        await client.send_message(message.channel, "O agraciado com a força além de 8000, esta a procura de novos padawans")
    
    if message.content.lowet().startswith("!Owners"):
        await client.send_message(message.channel, "@🛠️Master Builder são os criadores da nossa fortaleza impenetravel")
    
    if message.content.lowet().startswith("!Força"):
        await client.send_message(message.channel, "A Força é definida como um campo de energia misterioso criado pela vida que une toda a galáxia")


@client.event
async def on_message(message):
     contents = message.content.split("")
     for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                await client.delete_message(message)
                await client.sent_message(message.channel, "**HEY você esta tentando fazer algo ilicito por não ter permissão para divulgar aqui.")






client.run('MTA2NzkzMjg3MDc5MTkzODA1OA.GjdZ5g.44VDd9BBI8oO6WztqvB93obk5qHubJvN9pQLiI')