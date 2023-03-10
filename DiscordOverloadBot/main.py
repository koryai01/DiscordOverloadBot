import discord
from discord.ext import commands, tasks
from discord.utils import get
from discord import Embed
from pystyle import Colors, Colorate
import datetime
import requests
import wikipedia
import aiohttp
from datetime import datetime, timedelta
import asyncio
import random

prefix = "+" 
bot = commands.Bot(command_prefix=prefix)
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

print(Colorate.Horizontal(Colors.yellow_to_green, """ /$$$$$$$  /$$                                               /$$  /$$$$$$                                /$$                           /$$
| $$__  $$|__/                                              | $$ /$$__  $$                              | $$                          | $$
| $$  \ $$ /$$  /$$$$$$$  /$$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$$| $$  \ $$ /$$    /$$ /$$$$$$   /$$$$$$ | $$  /$$$$$$   /$$$$$$   /$$$$$$$
| $$  | $$| $$ /$$_____/ /$$_____/ /$$__  $$ /$$__  $$ /$$__  $$| $$  | $$|  $$  /$$//$$__  $$ /$$__  $$| $$ /$$__  $$ |____  $$ /$$__  $$
| $$  | $$| $$|  $$$$$$ | $$      | $$  \ $$| $$  \__/| $$  | $$| $$  | $$ \  $$/$$/| $$$$$$$$| $$  \__/| $$| $$  \ $$  /$$$$$$$| $$  | $$
| $$  | $$| $$ \____  $$| $$      | $$  | $$| $$      | $$  | $$| $$  | $$  \  $$$/ | $$_____/| $$      | $$| $$  | $$ /$$__  $$| $$  | $$
| $$$$$$$/| $$ /$$$$$$$/|  $$$$$$$|  $$$$$$/| $$      |  $$$$$$$|  $$$$$$/   \  $/  |  $$$$$$$| $$      | $$|  $$$$$$/|  $$$$$$$|  $$$$$$$
|_______/ |__/|_______/  \_______/ \______/ |__/       \_______/ \______/     \_/    \_______/|__/      |__/ \______/  \_______/ \_______/
                                                                                                                                          
                                                                                                                                          
                                                                                                                                          """, 1))

token = input(Colorate.Horizontal(Colors.yellow_to_green, "Le Token Du Bot ? :", 1))

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1078370942700503064) 
    message = f"Bienvenue {member.mention} sur notre serveur Discord ! Nous esp??rons que tu passeras un bon moment avec nous."
    await channel.send(message)

@bot.command(help='Affiche une aide personnalis??e')
async def myhelp(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title="Aide", description="Liste des commandes du bot DiscordOverload By Koryai", color=discord.Color.blue())
    embed.add_field(name="+statut [@utilisateur]", value="Affiche le statut de l'utilisateur mentionn??.", inline=False)
    embed.add_field(name="+kick [@utilisateur] [raison]", value="Kick l'utilisateur mentionn?? du serveur pour la raison donn??e.", inline=False)
    embed.add_field(name="+ban [@utilisateur] [raison]", value="Banni l'utilisateur mentionn?? du serveur pour la raison donn??e.", inline=False)
    embed.add_field(name="+mute [@utilisateur] [raison]", value="R??duit l'utilisateur mentionn?? au silence sur le serveur pour la raison donn??e.", inline=False)
    embed.add_field(name="+say [message]", value="Le bot r??p??te le message donn?? dans le canal textuel dans lequel la commande a ??t?? envoy??e.", inline=False)
    embed.add_field(name="+mp [@utilisateur] [message]", value="Envoie un message priv?? ?? l'utilisateur mentionn??.", inline=False)
    embed.add_field(name="+clear [nombre]", value="Supprime un nombre de messages donn?? dans le canal textuel dans lequel la commande a ??t?? envoy??e.", inline=False)
    embed.add_field(name="+spam [message] [nombre]", value="Envoie le message donn?? dans tous les canaux textuels du serveur, donn?? un nombre de fois.", inline=False)
    embed.add_field(name="+lockall", value="Verrouille tous les canaux textuels du serveur.", inline=False)
    embed.add_field(name="+lock", value="Verrouille le canal o?? la commande a ??t?? envoy??e.", inline=False)
    embed.add_field(name="+unlock", value="D??verrouille le canal o?? la commande a ??t?? envoy??e.", inline=False)
    embed.add_field(name="+addrole [@utilisateur] [@r??le]", value="Ajoute un r??le ?? un utilisateur.", inline=False)
    embed.add_field(name="+avatar [@utilisateur]", value="Affiche l'avatar de l'utilisateur mentionn?? ou de l'auteur de la commande.", inline=False)
    embed.add_field(name="+ping", value="Affiche le ping du bot", inline=False)
    embed.add_field(name="+logs", value="Cr??e des salons pour les logs des messages supprim??s et ??dit??s.", inline=False)
    embed.add_field(name='+blague', value='Affiche une blague al??atoire en anglais.', inline=False)
    embed.add_field(name='+wikisearch', value='Recherche une page Wikip??dia et renvoie son r??sum?? en anglais.', inline=False)
    embed.add_field(name="+setname", value="Changer le nom du bot (r??serv?? au propri??taire du bot)", inline=False)
    embed.add_field(name="+setavatar", value="Changer l'avatar du bot (r??serv?? au propri??taire du bot)", inline=False)
    embed.add_field(name="+questions [question]",value="R??pond ?? une question.",inline=False)
    embed.set_footer(text=f"Demand?? par {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
 
with open('config.txt', 'r') as f:
    user_id = int(f.read())

@bot.event
async def on_guild_join(guild):
    user = bot.get_user(user_id)
    if user is not None:
        await user.send(f"Je viens de rejoindre le serveur {guild.name} !")
    else:
        print("L'utilisateur n'a pas ??t?? trouv??.")

@bot.event
async def on_message_delete(message):
    if not message.author.bot:
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(f"[{datetime.datetime.now()}] Message deleted from {message.author.name} ({message.author.id}) in {message.channel.name} ({message.channel.id}) with content: {message.content}\n")

@bot.command()
async def statut(ctx, member: discord.Member):
    status = member.status
    await ctx.send(f"Le statut de {member.mention} est {status}.")

@bot.event
async def on_ready():
    print(Colorate.Horizontal(Colors.yellow_to_green, f"Le bot est en ligne !", 1))

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *reason):
    reason1 = " ".join(reason)
    await ctx.guild.kick(user, reason=reason1)
    await ctx.send(f"Le membre {user.name} a bien ??t?? kick du serveur pour raison : {reason1}.")

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *reason):
    reason2 = " ".join(reason)
    await ctx.guild.ban(user, reason=reason2)
    await ctx.send(f"Le membre {user.name} a bien ??t?? banni du serveur pour la raison : {reason2}")

def convert_duration(duration: str) -> int:
    unit = duration[-1]
    time = int(duration[:-1])
    if unit == 'm':
        return time
    elif unit == 'h':
        return time * 60
    elif unit == 'd':
        return time * 1440
    else:
        raise commands.BadArgument("Temp invalide. Peux-tu utiliser les temp suivant : \n 'm', 'h', or 'd'.")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, duration: str):

        try:
            time = convert_duration(duration)
        except commands.BadArgument as e:
            await ctx.send(str(e))
            return
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not role:
            role = await ctx.guild.create_role(name='Muted')
            for channel in ctx.guild.channels:
                await channel.set_permissions(role, speak=False, send_messages=False)

        await member.add_roles(role)
        await ctx.send(f"{member.mention} a ??t?? mute pendant {duration}.")

        await asyncio.sleep(time)

        await member.remove_roles(role)
        await ctx.send(f"{member.mention} a ??t?? demute apr??s {duration}.")

@bot.command()
async def say(ctx, *, message):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"{message}")

@bot.command()
async def mp(ctx, member: discord.Member, *, message: str):
    await member.send(f"Vous Avez Re??u Un Message De La Part De {ctx.author.name} : {message}")
    await ctx.send(f"{ctx.author.mention}, Votre message a bien ??t?? envoy?? ?? {member.mention}")

@bot.command()
@commands.has_permissions(ban_members=True)
async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f"{amount} messages ont ??t?? supprim??s.", delete_after=5)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def spam(ctx, message: str, number: int):
    if not message or not number:
        await ctx.send("Veuillez fournir un message et un nombre valide.")
        return

    guild = ctx.guild
    for channel in guild.text_channels:
        for i in range(number):
            await channel.send(message)

@bot.command(help='Bloque l\'acc??s ?? tous les salons du serveur')
@commands.has_permissions(manage_channels=True)
@commands.has_role("Administrator")
async def lockall(ctx):
        for channel in ctx.guild.channels:
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)
        await ctx.send("Tous les salons ont ??t?? bloqu??s.")

@bot.command()
@commands.has_permissions(manage_channels=True)
@commands.has_role("Administrator")
async def unlock(ctx):
        if ctx.author.id != user_id:
            channel = ctx.channel
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)
            await ctx.send(f"Le salon {channel.mention} a ??t?? d??verrouill??.")

@bot.command()
@commands.has_permissions(administrator=True)
@commands.has_role("Administrator")
async def lock(ctx):
        if ctx.author.id != user_id:
            if not ctx.author.guild_permissions.manage_channels:
                await ctx.send("Vous n'avez pas la permission de verrouiller ce canal.")
                return
            channel = ctx.channel

            await channel.set_permissions(ctx.guild.default_role, read_messages=False, send_messages=False)

            await ctx.send(f"{channel.mention} a ??t?? verrouill??.")

@bot.command(help='Ajoute un r??le ?? un utilisateur')
@commands.has_permissions(manage_roles=True)
@commands.has_role("Administrator")
async def addrole(ctx, member: discord.Member, role: discord.Role):
        if ctx.author.id != user_id:
            await member.add_roles(role)
            await ctx.send(f"Le r??le {role.name} a ??t?? ajout?? ?? {member.mention}")

@bot.command(help='Affiche l\'avatar de l\'utilisateur')
async def avatar(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"Avatar de {member.display_name}", color=member.color.blue())
    embed.set_image(url=member.avatar_url)
    embed.set_author(name=member.name, icon_url=member.avatar_url)
    embed.add_field(name="Lien de l'avatar :", value=f"[Cliquez ici]({member.avatar_url})", inline=False)
    await ctx.send(embed=embed)

@bot.command(help='Cr??e des salons de logs pour les messages supprim??s et modifi??s')
@commands.has_permissions(manage_channels=True)
async def createlogs(ctx):
    if ctx.author.id != user_id:
        guild = ctx.guild

        deleted_logs_channel = await guild.create_text_channel('???????logs-messages-supprimes', category=None, position=0)
        await deleted_logs_channel.set_permissions(guild.default_role, read_messages=False)
        await deleted_logs_channel.set_permissions(bot.user, read_messages=True, send_messages=True)

        edited_logs_channel = await guild.create_text_channel('???????logs-messages-modifies', category=None, position=1)
        await edited_logs_channel.set_permissions(guild.default_role, read_messages=False)
        await edited_logs_channel.set_permissions(bot.user, read_messages=True, send_messages=True)

        await ctx.send('Les salons logs ont ??t?? cr??es avec succ??s !')

@bot.event
async def on_message_delete(message):
    if message.guild is not None:
        deleted_logs_channel = discord.utils.get(message.guild.text_channels, name='???????logs-messages-supprimes')
        if deleted_logs_channel is not None:
            embed = discord.Embed(title="Message supprim??", color=discord.Color.blue())
            embed.add_field(name="Auteur", value=message.author.mention)
            embed.add_field(name="Salon", value=message.channel.mention)
            embed.add_field(name="Contenu", value=message.content)
            await deleted_logs_channel.send(embed=embed)

@bot.event
async def on_message_edit(before, after):
    if before.guild is not None and before.content != after.content:
        edited_logs_channel = discord.utils.get(before.guild.text_channels, name='???????logs-messages-modifies')
        if edited_logs_channel is not None:
            embed = discord.Embed(title="Message modifi??", color=discord.Color.blue())
            embed.add_field(name="Auteur", value=before.author.mention)
            embed.add_field(name="Salon", value=before.channel.mention)
            embed.add_field(name="Avant", value=before.content, inline=False)
            embed.add_field(name="Apr??s", value=after.content, inline=False)
            await edited_logs_channel.send(embed=embed)

@bot.command(help='Affiche le ping du bot')
async def ping(ctx):
    await ctx.message.delete()
    latency = bot.latency * 1000
    embed = discord.Embed(title='Ping du bot', description=f'Le ping du bot est de {int(latency)} ms.', color=discord.Color.blue())
    await ctx.send(embed=embed)

@bot.command()
async def blague(ctx):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    data = response.json()
    setup = data['setup']
    punchline = data['punchline']
    embed = discord.Embed(title="Blague", color=0xffe100)
    embed.add_field(name="Setup", value=setup, inline=False)
    embed.add_field(name="Punchline", value=punchline, inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def wikisearch(ctx, *, search):
    try:
        page = wikipedia.page(search)
        title = page.title
        summary = wikipedia.summary(search, sentences=2)
        link = page.url
        embed = discord.Embed(title=title, description=summary, url=link, color=discord.Color.blue())
        await ctx.send(embed=embed)
    except wikipedia.exceptions.DisambiguationError as e:
        await ctx.send(f"Plusieurs r??sultats ont ??t?? trouv??s pour '{search}'. Essayez d'??tre plus pr??cis.")
    except wikipedia.exceptions.PageError as e:
        await ctx.send(f"Aucun r??sultat trouv?? pour '{search}'. Veuillez r??essayer avec une autre requ??te.")


@bot.command()
async def setname(ctx, *, name: str):
    if ctx.author.id != user_id:
        await ctx.send("D??sol??, vous n'??tes pas autoris?? ?? utiliser cette commande.")
        return
    await bot.user.edit(username=name)
    await ctx.send(f"Le nom du bot a ??t?? chang?? en : {name}")

@bot.command()
async def setavatar(ctx, url: str):
    if ctx.author.id != user_id:
        await ctx.send("D??sol??, vous n'??tes pas autoris?? ?? utiliser cette commande.")
        return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            image_data = await resp.read()
    await bot.user.edit(avatar=image_data)
    await ctx.send("L'avatar du bot a ??t?? mis ?? jour")

@bot.command()
async def questions(ctx, *, question):
    responses = [
        "C'est certain.",
        "Sans aucun doute.",
        "Oui, d??finitivement.",
        "Tu peux compter dessus.",
        "Il est certain.",
        "Oui, oui, oui!",
        "Probablement.",
        "Les perspectives sont bonnes.",
        "Je ne suis pas s??r, demande plus tard.",
        "Je pr??f??re ne pas r??pondre maintenant.",
        "Je ne peux pas pr??dire cela pour le moment.",
        "Concentrez-vous et demandez ?? nouveau.",
        "Ne compte pas dessus.",
        "Ma r??ponse est non.",
        "Mes sources disent non.",
        "Les perspectives ne sont pas si bonnes.",
        "Tr??s douteux."
    ]
    await ctx.send(f"{random.choice(responses)}")

bot.run(token)